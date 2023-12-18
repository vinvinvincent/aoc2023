import pytest
from testplan.testing.multitest.result import Result
from timeout_function_decorator import timeout

from data.day16 import EXPECTED_SAMPLE_ENERGIZED_MAP, SAMPLE_DATA, PUZZLE_DATA
from aoc2023.day16 import Grid

import sys

sys.setrecursionlimit(10000)


class TestDay16:
    @timeout(5)
    @pytest.mark.parametrize(
        'input, expected_val, expected_map',
        [
            (SAMPLE_DATA, 46, EXPECTED_SAMPLE_ENERGIZED_MAP),
            (PUZZLE_DATA, None, None),
        ],
    )
    def test_part1(self, env, result: Result, input, expected_val, expected_map):
        '''Part 1'''

        grid = Grid(input)
        grid.pass_beam()
        actual_val = grid.energized_count
        actual_map = grid.energized_map_as_text

        if expected_val:
            result.eq(actual_val, expected_val, description='energized tile count')
        else:
            result.log(actual_val, description='energized tile count')

        if expected_map:
            result.eq(actual_map, expected_map, description='energized map')
        else:
            result.log(actual_map, description='energized map')
