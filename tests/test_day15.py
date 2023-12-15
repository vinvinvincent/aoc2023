import pytest
from testplan.testing.multitest.result import Result

from data.day15 import SAMPLE_DATA, PUZZLE_DATA
from aoc2023.day15 import (
    calc_hash,
    calc_hash_sum,
    get_focusing_power,
    update_boxes_operations,
)


class TestDay15:
    @pytest.mark.parametrize(
        'input, expected',
        [
            (SAMPLE_DATA[0], 30),
            (SAMPLE_DATA[1], 253),
            (SAMPLE_DATA[2], 97),
            (SAMPLE_DATA[3], 47),
            (SAMPLE_DATA[4], 14),
            (SAMPLE_DATA[5], 180),
            (SAMPLE_DATA[6], 9),
            (SAMPLE_DATA[7], 197),
            (SAMPLE_DATA[8], 48),
            (SAMPLE_DATA[9], 214),
            (SAMPLE_DATA[10], 231),
        ],
    )
    def test_hash_value(self, env, result: Result, input, expected):
        '''Part 1: hash value'''

        result.log(input, description='Input')

        result.eq(calc_hash(input), expected, description='Expected Hash Value')

    @pytest.mark.parametrize(
        'inputs, expected',
        [
            (SAMPLE_DATA, 1320),
            (PUZZLE_DATA, None),  # log result only
        ],
    )
    def test_hash_sum(self, env, result: Result, inputs, expected):
        '''Part 1: sum of all hash values'''

        result.log(inputs, description='Inputs')
        actual = calc_hash_sum(inputs)
        if expected:
            result.eq(actual, expected, description='Expected Hash Sum')
        else:
            result.log(actual, description='Hash Sum')

    @pytest.mark.parametrize(
        'inputs, expected',
        [
            (SAMPLE_DATA[:1], {0: [['rn', 1]]}),
            (SAMPLE_DATA[:2], {0: [['rn', 1]]}),
            (SAMPLE_DATA[:3], {0: [['rn', 1]], 1: [['qp', 3]]}),
            (SAMPLE_DATA[:4], {0: [['rn', 1], ['cm', 2]], 1: [['qp', 3]]}),
            (SAMPLE_DATA[:5], {0: [['rn', 1], ['cm', 2]]}),
            (SAMPLE_DATA[:6], {0: [['rn', 1], ['cm', 2]], 3: [['pc', 4]]}),
            (SAMPLE_DATA[:7], {0: [['rn', 1], ['cm', 2]], 3: [['pc', 4], ['ot', 9]]}),
            (
                SAMPLE_DATA[:8],
                {0: [['rn', 1], ['cm', 2]], 3: [['pc', 4], ['ot', 9], ['ab', 5]]},
            ),
            (SAMPLE_DATA[:9], {0: [['rn', 1], ['cm', 2]], 3: [['ot', 9], ['ab', 5]]}),
            (
                SAMPLE_DATA[:10],
                {0: [['rn', 1], ['cm', 2]], 3: [['ot', 9], ['ab', 5], ['pc', 6]]},
            ),
            (
                SAMPLE_DATA,
                {0: [['rn', 1], ['cm', 2]], 3: [['ot', 7], ['ab', 5], ['pc', 6]]},
            ),
        ],
    )
    def test_part2_update_boxes_operation(self, env, result: Result, inputs, expected):
        '''Part 2: update boxes operation'''

        result.log(inputs, description='Inputs')

        boxes = dict()
        update_boxes_operations(boxes, inputs)

        result.eq(boxes, expected, description='Expected Boxes')

    @pytest.mark.parametrize(
        'inputs, expected',
        [
            (SAMPLE_DATA, 145),
            (PUZZLE_DATA, None),  # log result only
        ],
    )
    def test_part2_get_focusing_power(self, env, result: Result, inputs, expected):
        '''Part 2: get focusing power'''

        result.log(inputs, description='Inputs')

        boxes = dict()
        update_boxes_operations(boxes, inputs)
        actual = get_focusing_power(boxes)

        if expected:
            result.eq(actual, expected, description='Expected Power')
        else:
            result.log(actual, description='Power')
