import copy

def get_predicton_from_sequence(initial_sequence):
    sequences = [copy.deepcopy(initial_sequence)]
    last_sequence = sequences[0]

    # append next sequence until all values in sequence are 0
    while True:
        next_sequence = []
        for i in range(1, len(last_sequence)):
            next_sequence.append(last_sequence[i] - last_sequence[i-1])

        sequences.append(next_sequence)

        if all(x == 0 for x in next_sequence):
            break
        else:
            last_sequence = next_sequence

    sequences[-1].append(0)
    for i in reversed(range(len(sequences)-1)):
        value_left = sequences[i][-1]
        value_below = sequences[i+1][-1]
        sequences[i].append(value_left+value_below)
    
    return [sequences[0][-1], sequences]

def get_predicton_sum_from_sequences(sequences):
    prediction_sum = 0
    for i in range(len(sequences)):
        prediction, _ = get_predicton_from_sequence(sequences[i])
        prediction_sum += prediction
    
    return prediction_sum

def sequences_to_string(sequences):
    def seq_to_string(seq):
        return ' '.join(str(x) for x in seq)

    text = ''
    for i in range(len(sequences)):
        text += ' ' * i + seq_to_string(sequences[i]) + '\n'

    return text
