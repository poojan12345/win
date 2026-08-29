#!/usr/bin/env python3
"""Static acceptance check for the Phase 1 multi-robot namespace contract."""

EXPECTED = [f'/swarm/robot_{i:02d}' for i in range(1, 11)]


def validate_topic_set(topics):
    missing = []
    for ns in EXPECTED:
        for topic in ('scan', 'odom', 'cmd_vel'):
            if f'{ns}/{topic}' not in topics:
                missing.append(f'{ns}/{topic}')
    return missing


if __name__ == '__main__':
    import sys
    supplied = set(sys.argv[1:])
    missing = validate_topic_set(supplied)
    if missing:
        print('FAIL: missing expected namespaced topics:')
        print('\n'.join(missing))
        raise SystemExit(1)
    print('PASS: all 10 robot namespaces expose scan, odom and cmd_vel.')
