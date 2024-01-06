import pytest
from testplan.testing.multitest.result import Result
from timeout_function_decorator import timeout
from utils import TIMEOUT_SEC, check_eq_or_log

from data.day6 import (
    SAMPLE_DATA_PART1,
    PUZZLE_DATA_PART1,
    SAMPLE_DATA_PART2,
    PUZZLE_DATA_PART2,
)
from aoc2023.day6 import get_part1, get_part2


class TestDay6:
    @timeout(TIMEOUT_SEC)
    @pytest.mark.parametrize(
        'input, expected',
        [
            (SAMPLE_DATA_PART1, 288),
            (PUZZLE_DATA_PART1, None),
        ],
    )
    def test_part1(self, env, result: Result, input, expected):
        '''Part 1'''
        check_eq_or_log(result, get_part1(input), expected, 'Part 1')

    @timeout(90)
    @pytest.mark.parametrize(
        'input, expected',
        [
            (SAMPLE_DATA_PART2, 71503),
            (PUZZLE_DATA_PART2, None),
        ],
    )
    def test_part2(self, env, result: Result, input, expected):
        '''Part 2'''
        check_eq_or_log(result, get_part2(input), expected, 'Part 2')
