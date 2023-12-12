def get_calibration_value(input):
    '''
    combining the first digit and the last digit (in that order) 
    to form a single two-digit number'
    '''
    str_len = len(input)
    first, last = None, None
    for i in range(str_len):
        c = input[i]
        if c.isdigit():
            first = c
            break

    for i in range(str_len):
        c = input[-i - 1]
        if c.isdigit():
            last = c
            break

    if not first or not last:
        raise ValueError(f'Invalid Input: {input}')
    
    return int(first + last)

def get_calibration_sum(inputs):
    '''sum all values from each input'''
    sum = 0
    for input in inputs:
        sum += get_calibration_value(input)
    return sum

def transform_word_to_digit(input):

    DIGIT_DICT = {
        'one':'one1one', 'two':'two2two', 'three':'three3three', 
        'four':'four4four', 'five':'five5five', 'six':'six6six', 
        'seven':'seven7seven', 'eight':'eight8eight', 'nine':'nine9nine',
    }
    result = input

    for k, v in DIGIT_DICT.items():
        if k in input:
            result = result.replace(k, v)
            continue

    return result

def get_calibration_sum_with_transform(input):
    new_input = []
    for i in range(len(input)):
        new_input.append(transform_word_to_digit(input[i]))
    
    return get_calibration_sum(new_input)