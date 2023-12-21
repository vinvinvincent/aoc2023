import pytest
from testplan.testing.multitest.result import Result
from timeout_function_decorator import timeout

from aoc2023.day2 import (
    is_possible_game,
    power_of_set_of_cubes,
    sum_of_all_possible_game_ids,
    sum_of_power_of_set_of_cubes,
)
from data.day2 import (
    SAMPLE_DATA,
    PUZZLE_DATA,
    Cubes,
)
from utils import check_eq_or_log, TIMEOUT_SEC

BAG = Cubes(12, 13, 14)


class TestDay2:
    @timeout(TIMEOUT_SEC)
    @pytest.mark.parametrize(
        'input_game, input_bag, expected',
        [
            (SAMPLE_DATA.get_game_number(1), BAG, True),
            (SAMPLE_DATA.get_game_number(2), BAG, True),
            (SAMPLE_DATA.get_game_number(3), BAG, False),
            (SAMPLE_DATA.get_game_number(4), BAG, False),
            (SAMPLE_DATA.get_game_number(5), BAG, True),
        ],
    )
    def test_part1_possible(self, env, result: Result, input_game, input_bag, expected):
        '''Part 1: possible game'''
        actual = is_possible_game(input_game, input_bag)
        check_eq_or_log(result, actual, expected, 'possible')

    @timeout(TIMEOUT_SEC)
    @pytest.mark.parametrize(
        'input_games, input_bag, expected',
        [
            (SAMPLE_DATA, BAG, 8),
            (PUZZLE_DATA, BAG, None),
        ],
    )
    def test_part1_sum(self, env, result: Result, input_games, input_bag, expected):
        '''Part 1: sum of all possible games'''
        actual = sum_of_all_possible_game_ids(input_games, input_bag)
        check_eq_or_log(result, actual, expected, 'sum')

    @timeout(TIMEOUT_SEC)
    @pytest.mark.parametrize(
        'input_game, expected',
        [
            (SAMPLE_DATA.get_game_number(1), 48),
            (SAMPLE_DATA.get_game_number(2), 12),
            (SAMPLE_DATA.get_game_number(3), 1560),
            (SAMPLE_DATA.get_game_number(4), 630),
            (SAMPLE_DATA.get_game_number(5), 36),
        ],
    )
    def test_part2_power(self, env, result: Result, input_game, expected):
        '''Part 2: power'''
        actual = power_of_set_of_cubes(input_game)
        check_eq_or_log(result, actual, expected, 'possible')

    @timeout(TIMEOUT_SEC)
    @pytest.mark.parametrize(
        'input_games, expected',
        [
            (SAMPLE_DATA, 2286),
            (PUZZLE_DATA, None),
        ],
    )
    def test_part2_sum(self, env, result: Result, input_games, expected):
        '''Part 2: sum of power'''
        actual = sum_of_power_of_set_of_cubes(input_games)
        check_eq_or_log(result, actual, expected, 'sum')
