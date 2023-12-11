import pytest

from data.day9 import PART1_SAMPLE_DATA, PUZZLE_DATA
from aoc2023.day9 import get_predicton_from_sequence, get_predicton_sum_from_sequences, sequences_to_string

class TestDay9:

    @pytest.mark.parametrize(
        "sequence, expected_prediction", 
        [
            (PART1_SAMPLE_DATA[0], 18), 
            (PART1_SAMPLE_DATA[1], 28),
            (PART1_SAMPLE_DATA[2], 68),
        ]
    )
    def test_part1_prediction(self, env, result, sequence, expected_prediction):
        result.log(sequence, description='Sequence')

        prediction, prediction_sequences = get_predicton_from_sequence(sequence)
        result.log(sequences_to_string(prediction_sequences), description='Prediction Text')

        result.eq(prediction, expected_prediction, description='Expected Prediction')

    @pytest.mark.parametrize(
        "sequences, expected_prediction_sum", 
        [
            (PART1_SAMPLE_DATA, 114), 
            (PUZZLE_DATA,       None), # log result only
        ]
    )
    def test_part1(self, env, result, sequences, expected_prediction_sum):
        result.log(sequences, description='Sequences')

        prediction_sum = get_predicton_sum_from_sequences(sequences)
        if expected_prediction_sum:
            result.eq(prediction_sum, expected_prediction_sum, description='Expected Prediction Sum')
        else:
            result.log(prediction_sum, description='Prediction Sum')
