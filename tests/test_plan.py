#!/usr/bin/env python
import sys
import os

from testplan import test_plan
from testplan.testing import py_test

COVERAGE_OPT='--coverage'
COVERAGE=False

DAYS=[8, 9]

@test_plan(name='AOC 2023', json_path='report.json')
def main(plan):
    for day in DAYS:
        plan.add(
            py_test.PyTest(
                name=f'Day {day}',
                target=[
                    os.path.join(os.path.dirname(__file__), f'test_day{day}.py')
                ],
                extra_args=['--cov=aoc2023'] if COVERAGE else None,
            )
        )

if __name__ == '__main__':
    COVERAGE = COVERAGE_OPT in sys.argv
    if COVERAGE:
        print('INFO: coverage enabled')
        sys.argv.remove(COVERAGE_OPT)
    res = main()
    sys.exit(res.exit_code)