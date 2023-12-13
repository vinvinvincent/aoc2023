import pytest
from testplan.testing.multitest.result import Result

from data.day9 import PART1_SAMPLE_DATA, PUZZLE_DATA
from aoc2023.day9 import (
    ExtrapolatedDirection,
    get_extrapolated_value_from_sequence,
    get_extrapolated_sum_from_sequences,
    sequences_to_string,
)


class TestDay9:
    @pytest.mark.parametrize(
        'sequence, expected',
        [
            (PART1_SAMPLE_DATA[0], 18),
            (PART1_SAMPLE_DATA[1], 28),
            (PART1_SAMPLE_DATA[2], 68),
        ],
    )
    def test_part1_extrapolated_value(self, env, result: Result, sequence, expected):
        '''Part 1: find the next value for each history'''

        result.log(sequence, description='Sequence')

        prediction, prediction_sequences = get_extrapolated_value_from_sequence(
            sequence
        )
        result.log(
            sequences_to_string(prediction_sequences),
            description='Extrapolated Next Value Calculation',
        )

        result.eq(prediction, expected, description='Expected Extrapolated Next Value')

    @pytest.mark.parametrize(
        'sequences, expected',
        [
            (PART1_SAMPLE_DATA, 114),
            (PUZZLE_DATA, None),  # log result only
        ],
    )
    def test_part1_extrapolated_sum(self, env, result: Result, sequences, expected):
        '''Part 1: sum of all extrapolated next values'''

        result.log(sequences, description='Sequences')

        prediction_sum = get_extrapolated_sum_from_sequences(sequences)
        if expected:
            result.eq(
                prediction_sum,
                expected,
                description='Expected Extrapolated Next Sum',
            )
        else:
            result.log(prediction_sum, description='Extrapolated Next Sum')

    @pytest.mark.parametrize(
        'sequence, expected',
        [
            (PART1_SAMPLE_DATA[0], -3),
            (PART1_SAMPLE_DATA[1], 0),
            (PART1_SAMPLE_DATA[2], 5),
        ],
    )
    def test_part2_extrapolated_value(self, env, result: Result, sequence, expected):
        '''Part 2: find the previous value for each history'''

        result.log(sequence, description='Sequence')

        prediction, prediction_sequences = get_extrapolated_value_from_sequence(
            sequence,
            ExtrapolatedDirection.LEFT,
        )
        result.log(
            sequences_to_string(prediction_sequences),
            description='Extrapolated Previous Value Calculation',
        )

        result.eq(
            prediction, expected, description='Expected Extrapolated Previous Value'
        )

    @pytest.mark.parametrize(
        'sequences, expected',
        [
            (PART1_SAMPLE_DATA, 2),
            (PUZZLE_DATA, None),  # log result only
        ],
    )
    def test_part2_extrapolated_sum(self, env, result: Result, sequences, expected):
        '''Part 2: sum of all extrapolated previous values'''

        result.log(sequences, description='Sequences')

        prediction_sum = get_extrapolated_sum_from_sequences(
            sequences,
            ExtrapolatedDirection.LEFT,
        )
        if expected:
            result.eq(
                prediction_sum,
                expected,
                description='Expected Extrapolated Previous Sum',
            )
        else:
            result.log(prediction_sum, description='Extrapolated Previous Sum')
