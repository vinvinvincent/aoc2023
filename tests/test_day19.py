import pytest
from testplan.testing.multitest.result import Result
from timeout_function_decorator import timeout

from aoc2023.day19 import (
    check_parts_accepted,
    get_sum_of_all_expected_parts,
)
from data.day19 import (
    SAMPLE_DATA,
    PUZZLE_DATA,
)
from utils import check_eq_or_log, TIMEOUT_SEC


class TestDay19:
    @timeout(TIMEOUT_SEC)
    @pytest.mark.parametrize(
        'input_parts, input_workflow, expected',
        [
            (SAMPLE_DATA.parts_list[0], SAMPLE_DATA.workflows, True),
            (SAMPLE_DATA.parts_list[1], SAMPLE_DATA.workflows, False),
            (SAMPLE_DATA.parts_list[2], SAMPLE_DATA.workflows, True),
            (SAMPLE_DATA.parts_list[3], SAMPLE_DATA.workflows, False),
            (SAMPLE_DATA.parts_list[4], SAMPLE_DATA.workflows, True),
        ],
    )
    def test_part1_check_parts_accepted(
        self, env, result: Result, input_parts, input_workflow, expected
    ):
        '''Part 1: check parts accepted'''
        actual = check_parts_accepted(input_parts, input_workflow, 'in')
        check_eq_or_log(result, actual, expected, 'check parts accepted')

    @timeout(TIMEOUT_SEC)
    @pytest.mark.parametrize(
        'input_parts, input_workflow, expected',
        [
            (SAMPLE_DATA.parts_list, SAMPLE_DATA.workflows, 19114),
            (PUZZLE_DATA.parts_list, PUZZLE_DATA.workflows, None),
        ],
    )
    def test_part1_check_parts_accepted(
        self, env, result: Result, input_parts, input_workflow, expected
    ):
        '''Part 1: sum of all expected parts'''
        actual = get_sum_of_all_expected_parts(input_parts, input_workflow, 'in')
        check_eq_or_log(result, actual, expected, 'sum of all expected parts')
