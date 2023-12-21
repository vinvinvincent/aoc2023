from functools import reduce


def get_number_and_start_end_col_indexes(line):
    result = []
    start_col_idx = None

    for i in range(len(line)):
        if line[i].isdigit():
            if start_col_idx is None:
                start_col_idx = i
        else:
            if start_col_idx is not None:
                result.append([int(line[start_col_idx:i]), start_col_idx, i - 1])
                start_col_idx = None

    # Check if there is a number at the end of the string
    if start_col_idx is not None:
        result.append([int(line[start_col_idx:]), start_col_idx, len(line) - 1])

    return result


def is_symbol_char(c):
    return not c.isdigit() and c != '.'


def is_surrounded_by_symbol(
    lines, row_idx, start_col_idx, end_col_idx, symbol_lambda=is_symbol_char
):
    # top row, bottom row
    row_indices_to_check = []
    if row_idx - 1 >= 0:
        row_indices_to_check.append(row_idx - 1)
    if row_idx + 1 < len(lines):
        row_indices_to_check.append(row_idx + 1)

    for index in row_indices_to_check:
        row = lines[index]

        for i in range(
            start_col_idx - 1 if start_col_idx > 0 else 0,
            min(len(row), end_col_idx + 2),
        ):
            if symbol_lambda(row[i]):
                return [index, i]

    # current row
    row = lines[row_idx]
    col_indices_to_check = []
    if start_col_idx - 1 >= 0:
        col_indices_to_check.append(start_col_idx - 1)
    if end_col_idx + 1 < len(row):
        col_indices_to_check.append(end_col_idx + 1)

    for index in col_indices_to_check:
        if symbol_lambda(row[index]):
            return [row_idx, index]

    return None


def sum_of_all_numbers_surrounded_by_symbol(lines):
    sum = 0
    for row_idx, line in enumerate(lines):
        potentials = get_number_and_start_end_col_indexes(line)
        for number, start_col_idx, end_col_idx in potentials:
            if is_surrounded_by_symbol(lines, row_idx, start_col_idx, end_col_idx):
                sum += number
    return sum


def is_gear_char(c):
    return c == '*'


def sum_of_all_number_products_surrounded_by_gear(lines):
    gear_to_numbers = {}
    for row_idx, line in enumerate(lines):
        potentials = get_number_and_start_end_col_indexes(line)
        for number, start_col_idx, end_col_idx in potentials:
            gear_pos = is_surrounded_by_symbol(
                lines,
                row_idx,
                start_col_idx,
                end_col_idx,
                is_gear_char,
            )
            if gear_pos:
                gear = gear_to_numbers.setdefault(str(gear_pos), set())
                gear.add(number)

    return sum(
        reduce((lambda x, y: x * y), numbers)
        for numbers in gear_to_numbers.values()
        if len(numbers) > 1
    )
