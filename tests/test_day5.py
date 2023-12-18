import pytest
from testplan.testing.multitest.result import Result
from timeout_function_decorator import timeout

from data.day5 import PART1_SAMPLE_DATA, PUZZLE_DATA, Almanac
from aoc2023.day5 import (
    get_lowest_location_from_seed_ranges,
    get_lowest_location_from_seeds,
    seed_to_all_types,
    source_to_dest_num,
)


class TestDay5:
    @pytest.mark.parametrize(
        'input, expected',
        [
            (79, 81),
            (14, 14),
            (55, 57),
            (13, 13),
        ],
    )
    def test_part1_seed_to_soil(self, env, result: Result, input, expected):
        '''Part 1: seed to soil'''
        actual = source_to_dest_num(input, PART1_SAMPLE_DATA.seed_to_soil)
        result.eq(actual, expected, description='soil')

    @pytest.mark.parametrize(
        'input, expected_soil, expected_fertilizer, expected_water, expected_light, expected_temperature, expected_humidity, expected_location',
        [
            (79, 81, 81, 81, 74, 78, 78, 82),
            (14, 14, 53, 49, 42, 42, 43, 43),
            (55, 57, 57, 53, 46, 82, 82, 86),
            (13, 13, 52, 41, 34, 34, 35, 35),
        ],
    )
    def test_part1_seed_to_all_types(
        self,
        env,
        result: Result,
        input,
        expected_soil,
        expected_fertilizer,
        expected_water,
        expected_light,
        expected_temperature,
        expected_humidity,
        expected_location,
    ):
        '''Part 1: seed to soil, fertilizer, water, light, temperature, humidity, location'''

        labels = (
            'soil, fertilizer, water, light, temperature, humidity, location'.split(
                ', '
            )
        )
        expecteds = [
            expected_soil,
            expected_fertilizer,
            expected_water,
            expected_light,
            expected_temperature,
            expected_humidity,
            expected_location,
        ]
        actuals = seed_to_all_types(input, PART1_SAMPLE_DATA)

        for i in range(len(labels)):
            result.eq(actuals[i], expecteds[i], description=f'{labels[i]}')

    @timeout(5)
    @pytest.mark.parametrize(
        'input, expected',
        [
            (PART1_SAMPLE_DATA, 35),
            (PUZZLE_DATA, None),
        ],
    )
    def test_part1_lowest_location_from_seeds(
        self, env, result: Result, input: Almanac, expected
    ):
        '''Part 1: lowest location from seeds'''
        actual = get_lowest_location_from_seeds(input.seeds, input)
        if expected:
            result.eq(actual, expected, description='lowest location')
        else:
            result.log(actual, description='lowest location')

    @timeout(5)
    @pytest.mark.parametrize(
        'input, expected',
        [
            (PART1_SAMPLE_DATA, 46),
            (PUZZLE_DATA, None),  # log result only
        ],
    )
    def test_part2_lowest_location_from_seed_ranges(
        self, env, result: Result, input: Almanac, expected
    ):
        '''Part 2: lowest location from seed ranges'''
        actual = get_lowest_location_from_seed_ranges(input.seed_ranges, input)
        if expected:
            result.eq(actual, expected, description='lowest location')
        else:
            result.log(actual, description='lowest location')
