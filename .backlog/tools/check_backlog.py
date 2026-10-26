#!/usr/bin/env python3
"""Validate CTX ticket metadata, links and dependency readiness using the stdlib."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
BACKLOG = ROOT / '.backlog'
BASELINE = 'c5ecb434b419d2c473cf2882a3866de9146abdec'
PHASES = {
    1: 'Environment and Fork Isolation',
    2: 'Database, Tenancy and Payment Foundations',
    3: 'Terminal and SDK Customization',
    4: 'Aggregator Console, API Exposure and Production Gates',
}
STATUSES = {'TODO', 'IN_PROGRESS', 'BLOCKED', 'DONE', 'SKIPPED'}
FILENAME = re.compile(r'^(CTX-\d{3})-([a-z0-9]+(?:-[a-z0-9]+)*)--TODO\.md$')
REQUIRED_SECTIONS = (
    'Context and intended outcome', 'Prerequisites and dependency outputs',
    'Relevant code and ownership', 'Implementation plan',
    'Acceptance criteria', 'Validation scenarios', 'Expected deliverables',
    'External inputs and applicability', 'Execution guardrails',
    'Handoff record',
)
REQUIRED_METADATA = (
    'id', 'title', 'status', 'phase', 'priority', 'size', 'repository',
    'component', 'depends_on', 'requires_one_of', 'conflict_domains',
    'external_inputs', 'external_inputs_resolved', 'applicability',
    'applicability_decision', 'source_baseline', 'requires_decisions',
    'conditional_dependencies',
)


def load_tickets():
    tickets = []
    errors = []
    for path in sorted(BACKLOG.glob('CTX-*.md')):
        match = FILENAME.fullmatch(path.name)
        if not match:
            errors.append(f'{path.name}: invalid requested filename format')
            continue
        text = path.read_text()
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            errors.append(f'{path.name}: missing frontmatter')
            continue
        raw, body = text[4:].split('\n---\n', 1)
        metadata = {}
        for line in raw.splitlines():
            key, sep, value = line.partition(':')
            if not sep or key in metadata:
                errors.append(f'{path.name}: invalid/duplicate metadata line {line!r}')
                continue
            try:
                metadata[key] = json.loads(value.strip())
            except json.JSONDecodeError:
                errors.append(f'{path.name}: metadata {key} must be a JSON-compatible YAML value')
        missing = set(REQUIRED_METADATA) - metadata.keys()
        if missing:
            errors.append(f'{path.name}: missing metadata {sorted(missing)}')
            continue
        if metadata['id'] != match.group(1):
            errors.append(f'{path.name}: filename/frontmatter ID mismatch')
        if metadata['status'] not in STATUSES:
            errors.append(f'{path.name}: invalid status')
        if metadata['phase'] not in PHASES:
            errors.append(f'{path.name}: invalid phase')
        if metadata['priority'] not in {'P0', 'P1', 'P2'}:
            errors.append(f'{path.name}: invalid priority')
        if metadata['size'] not in {'S', 'M', 'L'}:
            errors.append(f'{path.name}: invalid relative size')
        if metadata['applicability_decision'] not in {'selected', 'pending', 'deferred'}:
            errors.append(f'{path.name}: invalid applicability decision')
        if not isinstance(metadata['external_inputs_resolved'], bool):
            errors.append(f'{path.name}: external_inputs_resolved must be boolean')
        if not metadata['conflict_domains']:
            errors.append(f'{path.name}: missing conflict ownership domains')
        for field in ('depends_on', 'requires_one_of', 'conflict_domains', 'external_inputs',
                      'requires_decisions', 'conditional_dependencies'):
            if not isinstance(metadata[field], list):
                errors.append(f'{path.name}: {field} must be a list')
        for section in REQUIRED_SECTIONS:
            if f'## {section}\n' not in body:
                errors.append(f'{path.name}: missing {section}')
        for section, minimum in [('Implementation plan', 4), ('Acceptance criteria', 4),
                                 ('Validation scenarios', 3), ('Expected deliverables', 2)]:
            content = body.split(f'## {section}\n', 1)[-1].split('\n## ', 1)[0]
            count = len(re.findall(r'^- (?:\[ \] )?', content, re.M))
            if count < minimum:
                errors.append(f'{path.name}: {section} has {count} items, expected >= {minimum}')
        context = body.split('## Context and intended outcome\n', 1)[-1].split('\n## ', 1)[0]
        if len(context.split()) < 80:
            errors.append(f'{path.name}: insufficient standalone context')
        # Local links should work even when tickets are read outside this conversation.
        for target in re.findall(r'\]\(([^)]+)\)', body):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            target = target.split('#', 1)[0]
            if target and not (path.parent / target).exists():
                errors.append(f'{path.name}: broken local link {target}')
        metadata['file'] = path.name
        tickets.append(metadata)
    return tickets, errors


def validate_graph(tickets):
    errors = []
    by_id = {t['id']: t for t in tickets}
    if len(by_id) != len(tickets):
        errors.append('Duplicate CTX ID')
    graph = {}
    for ticket in tickets:
        ident = ticket['id']
        hard = ticket['depends_on']
        groups = ticket['requires_one_of']
        if len(hard) != len(set(hard)):
            errors.append(f'{ident}: duplicate dependency')
        for group in groups:
            if not isinstance(group, list) or len(group) < 2 or len(set(group)) != len(group):
                errors.append(f'{ident}: one-of group must have >= 2 distinct IDs')
        conditional = [d for rule in ticket['conditional_dependencies'] for d in rule['depends_on']]
        edges = list(hard) + [dep for group in groups for dep in group] + conditional
        graph[ident] = edges
        for dep in edges:
            if dep not in by_id:
                errors.append(f'{ident}: missing dependency {dep}')
            if dep == ident:
                errors.append(f'{ident}: self dependency')
    if errors:
        return errors
    done = set()
    active = []

    def visit(ident):
        if ident in active:
            raise ValueError('Dependency cycle: ' + ' -> '.join(active + [ident]))
        if ident in done:
            return
        active.append(ident)
        for dep in graph[ident]:
            visit(dep)
        active.pop()
        done.add(ident)

    try:
        for ident in graph:
            visit(ident)
    except ValueError as error:
        errors.append(str(error))
    return errors


def load_decisions():
    return json.loads((BACKLOG / 'decisions.json').read_text())['decisions']


def validate_decisions(tickets):
    errors = []
    try:
        decisions = load_decisions()
    except (OSError, json.JSONDecodeError, KeyError):
        return ['Missing or invalid decisions.json']
    by_id = {t['id']: t for t in tickets}
    for key, decision in decisions.items():
        owner = decision.get('owner_ticket')
        if owner not in by_id:
            errors.append(f'{key}: unknown decision owner')
        if decision.get('status') not in {'pending', 'selected'}:
            errors.append(f'{key}: invalid decision status')
        if decision.get('status') == 'selected':
            if decision.get('value') not in decision.get('allowed_values', []):
                errors.append(f'{key}: invalid selected decision value')
            if not decision.get('evidence'):
                errors.append(f'{key}: selected decision requires evidence')
        if owner in by_id and by_id[owner]['status'] == 'DONE' and decision.get('status') != 'selected':
            errors.append(f'{key}: owner {owner} is DONE but decision unresolved')
    for ticket in tickets:
        for key in ticket['requires_decisions']:
            if key not in decisions:
                errors.append(f"{ticket['id']}: unknown required decision {key}")
        for rule in ticket['conditional_dependencies']:
            if rule.get('decision') not in decisions or not isinstance(rule.get('depends_on'), list):
                errors.append(f"{ticket['id']}: invalid conditional dependency")
    return errors


def readiness(ticket, by_id, decisions=None):
    decisions = load_decisions() if decisions is None else decisions
    unresolved = [key for key in ticket['requires_decisions'] if decisions[key]['status'] != 'selected']
    active = []
    for rule in ticket['conditional_dependencies']:
        decision = decisions[rule['decision']]
        if decision['status'] != 'selected':
            unresolved.append(rule['decision'])
        elif decision['value'] == rule['value']:
            active.extend(rule['depends_on'])
    unmet = [d for d in dict.fromkeys(ticket['depends_on'] + active) if by_id[d]['status'] != 'DONE']
    alternatives = []
    for group in ticket['requires_one_of']:
        if set(group) == {'CTX-085', 'CTX-086'}:
            selected = decisions['pilot_terminal_adapter']
            if selected['status'] != 'selected':
                unresolved.append('pilot_terminal_adapter')
                alternatives.append(group)
            elif by_id[selected['value']]['status'] != 'DONE':
                alternatives.append([selected['value']])
        elif not any(by_id[d]['status'] == 'DONE' for d in group):
            alternatives.append(group)
    dependency_ready = not unmet and not alternatives and not unresolved
    external_ready = not ticket['external_inputs'] or ticket['external_inputs_resolved']
    selected = ticket['applicability_decision'] == 'selected'
    return {
        'unmet_dependencies': unmet,
        'unmet_one_of_groups': alternatives,
        'active_conditional_dependencies': sorted(set(active)),
        'unresolved_decisions': sorted(set(unresolved)),
        'dependency_ready': dependency_ready,
        'external_inputs_ready': external_ready,
        'applicability_selected': selected,
        'candidate_for_assignment': ticket['status'] == 'TODO' and dependency_ready
                                    and external_ready and selected,
    }


def manifest(tickets):
    by_id = {t['id']: t for t in tickets}
    decisions = load_decisions()
    return {
        'schema_version': 1,
        'source_baseline': BASELINE,
        'created_from_blueprint_date': '2026-10-22',
        'ticket_count': len(tickets),
        'phase_counts': {str(k): sum(t['phase'] == k for t in tickets) for k in PHASES},
        'status_counts': dict(sorted(Counter(t['status'] for t in tickets).items())),
        'decision_status': {key: value['status'] for key, value in decisions.items()},
        'semantics': {
            'depends_on': 'All listed dependencies must be DONE.',
            'requires_one_of': 'One DONE branch per group; terminal adapter groups require the exact decisions.json/CTX-013-selected branch.',
            'conditional_dependencies': 'Decision-selected features add required DONE dependencies; unresolved relevant decisions block assignment.',
            'conflict_domains': 'Advisory exclusive write domains; check actual changed-file ownership too.',
            'external_inputs_resolved': 'Explicit coordinator-owned evidence flag, never inferred from elapsed time.',
            'applicability_decision': 'selected, pending or deferred; pending/deferred tasks are not automatic assignments.',
        },
        'tickets': [{**t, 'readiness': readiness(t, by_id, decisions)} for t in tickets],
    }


def index_text(tickets):
    lines = [
        '# CTX implementation backlog', '',
        f'{len(tickets)} individually scoped tickets translating the white-label B2B2B payment-platform blueprint into executable work.', '',
        'Start with [RUNBOOK.md](RUNBOOK.md), the [architecture context](context/architecture.md), '
        '[shared contracts](context/contracts.md) and [repository map](context/repository-map.md). '
        'The complete source export has a [portable text snapshot](context/source-blueprint.txt).', '',
        'Use [TRACEABILITY.md](TRACEABILITY.md) to locate requirements and [EXECUTION-PLAN.md](EXECUTION-PLAN.md) '
        'for dependency bands and coordination rules. [manifest.json](manifest.json) is the generated scheduling index; '
        'ticket frontmatter is authoritative.', '',
        '```sh', 'python3 .backlog/tools/check_backlog.py',
        'python3 .backlog/tools/check_backlog.py --ready',
        'python3 .backlog/tools/check_backlog.py --refresh-index', '```', '',
        'All initial task filenames use `CTX-XXX-task-name--TODO.md`. Initial status is `TODO`; '
        'no architecture implementation is claimed by this planning artifact. '
        'Keep filenames stable and use frontmatter for execution status. '
        'External inputs, applicability decisions and conflict domains are separate from dependency readiness.', '',
        'Sizes are relative planning buckets, not dates. P0/P1/P2 indicate importance and sequencing. '
        'Phase is a roadmap grouping; it does not override prerequisite edges. '
        'CTX-139/140 are deferred conditional evolution, not default launch gates. '
        'CTX-085/086 represent integration-dependent adapter paths; downstream one-of groups require the CTX-013-selected path.', '',
        '## Coverage by phase', '', '| Phase | Tickets | Scope |', '|---|---:|---|',
    ]
    for phase, title in PHASES.items():
        ids = [t['id'] for t in tickets if t['phase'] == phase]
        chunks = []
        for ident in ids:
            number = int(ident[4:])
            if chunks and chunks[-1][-1] + 1 == number:
                chunks[-1].append(number)
            else:
                chunks.append([number])
        span = '; '.join(f'CTX-{c[0]:03}' + (f' to CTX-{c[-1]:03}' if len(c) > 1 else '') for c in chunks) or '-'
        lines.append(f'| {phase} | {len(ids)} ({span}) | {title} |')
    lines += ['', '## Current state', '',
              ', '.join(f'**{status}: {n}**' for status, n in sorted(Counter(t['status'] for t in tickets).items())) + '.', '',
              'The validator checks filenames, unique IDs, metadata, concrete sections, links, missing dependencies, '
              'cycles and generated-index consistency. It does not certify code, mark external inputs resolved or approve production actions.', '']
    for phase, title in PHASES.items():
        lines += [f'## Phase {phase}: {title}', '',
                  '| Ticket | Work item | Priority / size | Repository | Prerequisites |',
                  '|---|---|---|---|---|']
        for t in tickets:
            if t['phase'] != phase:
                continue
            deps = ', '.join(t['depends_on']) or 'None'
            for group in t['requires_one_of']:
                deps += '; one of (' + ' / '.join(group) + ')'
            for rule in t['conditional_dependencies']:
                deps += '; if ' + rule['decision'] + '=' + json.dumps(rule['value']) + ': ' + ', '.join(rule['depends_on'])
            conditional = '' if t['applicability'] == 'required' else f" [{t['applicability']}]"
            safe_title = t['title'].replace('|', '/')
            lines.append(f"| [{t['id']}]({t['file']}) | {safe_title}{conditional} | {t['priority']} / {t['size']} | {t['repository']} | {deps} |")
        lines.append('')
    return '\n'.join(lines).rstrip() + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ready', action='store_true', help='Show dependency frontier and assignment candidates.')
    parser.add_argument('--refresh-index', action='store_true', help='Refresh README.md and manifest.json from ticket metadata.')
    args = parser.parse_args()
    tickets, errors = load_tickets()
    if not tickets:
        errors.append('No ticket files found')
    if not errors:
        errors.extend(validate_graph(tickets))
        errors.extend(validate_decisions(tickets))
    if errors:
        for error in errors:
            print('ERROR:', error, file=sys.stderr)
        return 1
    expected = manifest(tickets)
    manifest_path = BACKLOG / 'manifest.json'
    expected_index = index_text(tickets)
    if args.refresh_index:
        manifest_path.write_text(json.dumps(expected, indent=2) + '\n')
        (BACKLOG / 'README.md').write_text(expected_index)
    else:
        try:
            actual = json.loads(manifest_path.read_text())
        except (FileNotFoundError, json.JSONDecodeError):
            actual = None
        if actual != expected or not (BACKLOG / 'README.md').exists() or (BACKLOG / 'README.md').read_text() != expected_index:
            print('ERROR: generated index is stale; use --refresh-index', file=sys.stderr)
            return 1
    print(f'PASS: {len(tickets)} tickets; metadata, sections, links and full dependency graph valid.')
    print('Phase counts:', ', '.join(f'{k}={v}' for k, v in expected['phase_counts'].items()))
    if args.ready:
        frontier = [t for t in expected['tickets'] if t['status'] == 'TODO' and t['readiness']['dependency_ready']]
        candidates = [t for t in expected['tickets'] if t['readiness']['candidate_for_assignment']]
        print('\nDependency frontier (external inputs and applicability may still block):')
        for t in frontier:
            print(f"  {t['id']} {t['title']} | inputs_ready={t['readiness']['external_inputs_ready']} | applicability={t['applicability_decision']}")
        print('\nCandidates for coordinator assignment:')
        for t in candidates:
            print(f"  {t['id']} {t['title']} | conflicts={','.join(t['conflict_domains'])}")
        print('Assignment also requires actual file ownership and prerequisite evidence review.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
