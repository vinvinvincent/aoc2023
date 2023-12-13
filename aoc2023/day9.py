import copy
from enum import Enum


class ExtrapolatedDirection(Enum):
    LEFT = 1
    RIGHT = 2


def get_extrapolated_value_from_sequence(
    initial_sequence, direction: ExtrapolatedDirection = ExtrapolatedDirection.RIGHT
):
    sequences = [copy.deepcopy(initial_sequence)]
    last_sequence = sequences[0]

    # append next sequence until all values in sequence are 0
    while True:
        next_sequence = []
        for i in range(1, len(last_sequence)):
            next_sequence.append(last_sequence[i] - last_sequence[i - 1])
        sequences.append(next_sequence)

        if all(x == 0 for x in next_sequence):
            break
        else:
            last_sequence = next_sequence

    extrapolated_value_idx = -1 if direction == ExtrapolatedDirection.RIGHT else 0
    sequences[-1].append(0)
    for i in reversed(range(len(sequences) - 1)):
        if direction == ExtrapolatedDirection.RIGHT:
            value_left = sequences[i][-1]
            value_below = sequences[i + 1][-1]
            sequences[i].append(value_left + value_below)
        else:
            value_right = sequences[i][0]
            value_below = sequences[i + 1][0]
            sequences[i].insert(0, value_right - value_below)

    return [sequences[0][extrapolated_value_idx], sequences]


def get_extrapolated_sum_from_sequences(
    sequences, direction: ExtrapolatedDirection = ExtrapolatedDirection.RIGHT
):
    extrapolated_sum = 0
    for i in range(len(sequences)):
        extrapolated, _ = get_extrapolated_value_from_sequence(sequences[i], direction)
        extrapolated_sum += extrapolated

    return extrapolated_sum


def sequences_to_string(sequences):
    def seq_to_string(seq):
        return ' '.join(str(x) for x in seq)

    text = ''
    for i in range(len(sequences)):
        text += ' ' * i + seq_to_string(sequences[i]) + '\n'

    return text
