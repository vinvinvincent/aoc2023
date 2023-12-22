import pytest
from testplan.testing.multitest.result import Result
from timeout_function_decorator import timeout

from aoc2023.day4 import (
    get_card_points,
    get_sum_of_card_points,
)
from data.day4 import (
    SAMPLE_DATA,
    PUZZLE_DATA,
)
from utils import check_eq_or_log, TIMEOUT_SEC


class Testday4:
    @timeout(TIMEOUT_SEC)
    @pytest.mark.parametrize(
        'input, expected',
        [
            (SAMPLE_DATA[0], 8),
            (SAMPLE_DATA[1], 2),
            (SAMPLE_DATA[2], 2),
            (SAMPLE_DATA[3], 1),
            (SAMPLE_DATA[4], 0),
            (SAMPLE_DATA[5], 0),
        ],
    )
    def test_part1_card_points(self, env, result: Result, input, expected):
        '''Part 1: card points'''
        actual = get_card_points(input[0], input[1])
        check_eq_or_log(result, actual, expected, 'points')

    @timeout(TIMEOUT_SEC)
    @pytest.mark.parametrize(
        'input, expected',
        [
            (SAMPLE_DATA, 13),
            (PUZZLE_DATA, None),
        ],
    )
    def test_part1_sum(self, env, result: Result, input, expected):
        '''Part 1: sum'''
        actual = get_sum_of_card_points(input)
        check_eq_or_log(result, actual, expected, 'sum')
