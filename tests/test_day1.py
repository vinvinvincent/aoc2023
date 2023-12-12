import pytest
from testplan.testing.multitest.result import Result

from data.day1 import PART1_SAMPLE_DATA, PART2_SAMPLE_DATA, PUZZLE_DATA
from aoc2023.day1 import get_calibration_value, get_calibration_sum, transform_word_to_digit, get_calibration_sum_with_transform

class TestDay1:

    @pytest.mark.parametrize(
        "input, expected", 
        [
            (PART1_SAMPLE_DATA[0], 12), 
            (PART1_SAMPLE_DATA[1], 38),
            (PART1_SAMPLE_DATA[2], 15),
            (PART1_SAMPLE_DATA[3], 77),
            ('',                   ValueError), # throw exception
            ('abcde',              ValueError), # throw exception
        ]
    )
    def test_part1_calibration_value(self, env, result:Result, input, expected):
        result.log(input, description='Input')
        try:
            result.eq(get_calibration_value(input), expected, description='Expected Value')
        except ValueError as e:
            if expected is not ValueError:
                result.fail(f'Unexpected failure {e}')
            else:
                result.log(f'{e}', description='Expected Exception')

    @pytest.mark.parametrize(
        "input, expected", 
        [
            (PART1_SAMPLE_DATA, 142),
            (PUZZLE_DATA,       None), # log result only
        ]
    )
    def test_part1(self, env, result:Result, input, expected):
        result.log(input, description='input')
        if expected is not None:
            result.eq(get_calibration_sum(input), expected, description='Expected Sum')
        else:
            result.log(get_calibration_sum(input), description='Sum')

    @pytest.mark.parametrize(
        "input, expected", 
        [
            (PART2_SAMPLE_DATA[0], 29), 
            (PART2_SAMPLE_DATA[1], 83),
            (PART2_SAMPLE_DATA[2], 13),
            (PART2_SAMPLE_DATA[3], 24),
            (PART2_SAMPLE_DATA[4], 42),
            (PART2_SAMPLE_DATA[5], 14),
            (PART2_SAMPLE_DATA[6], 76),
            ('mht8xndfgprq3eightwol', 82),
            ('ns5twoneg', 51),
        ]
    )
    def test_part2_calibration_value_with_transform(self, env, result:Result, input, expected):
        result.log(input, description='Input')
        result.eq(get_calibration_value(transform_word_to_digit(input)), expected, description='Expected Value')

    @pytest.mark.parametrize(
        "input, expected", 
        [
            (PART2_SAMPLE_DATA, 281), 
            (PUZZLE_DATA,       None), # log result only
        ]
    )
    def test_part2(self, env, result:Result, input, expected):
        result.log(input, description='input')
        if expected is not None:
            result.eq(get_calibration_sum_with_transform(input), expected, description='Expected Sum')
        else:
            result.log(get_calibration_sum_with_transform(input), description='Sum')