import pytest
from testplan.testing.multitest.result import Result
from timeout_function_decorator import timeout

from aoc2023.day3 import (
    sum_of_all_numbers_surrounded_by_symbol,
    sum_of_all_number_products_surrounded_by_gear,
)
from data.day3 import (
    SAMPLE_DATA,
    PUZZLE_DATA,
)
from utils import check_eq_or_log, TIMEOUT_SEC


class TestDay3:
    @timeout(TIMEOUT_SEC)
    @pytest.mark.parametrize(
        'input, expected',
        [
            (SAMPLE_DATA, 4361),
            (PUZZLE_DATA, None),
        ],
    )
    def test_part1(self, env, result: Result, input, expected):
        '''Part 1'''
        actual = sum_of_all_numbers_surrounded_by_symbol(input)
        check_eq_or_log(result, actual, expected, 'sum')

    @timeout(TIMEOUT_SEC)
    @pytest.mark.parametrize(
        'input, expected',
        [
            (SAMPLE_DATA, 467835),
            (PUZZLE_DATA, None),
        ],
    )
    def test_part2(self, env, result: Result, input, expected):
        '''Part 2'''
        actual = sum_of_all_number_products_surrounded_by_gear(input)
        check_eq_or_log(result, actual, expected, 'sum')
