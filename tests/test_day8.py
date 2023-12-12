import pytest
from aoc2023.day8 import Part1, Part2
from data.day8 import Part1SampleInput1, Part1SampleInput2, Part2SampleInput, PuzzleInput

class TestDay8:

    @pytest.mark.parametrize(
        "instructions, nodes, expected_steps", 
        [
            (Part1SampleInput1.INSTRUCTIONS, Part1SampleInput1.NODES,  2), 
            (Part1SampleInput2.INSTRUCTIONS, Part1SampleInput2.NODES,  6),
            (PuzzleInput.INSTRUCTIONS,       PuzzleInput.NODES,        None), # log result only
        ]
    )
    def test_part1(self, env, result, instructions, nodes, expected_steps):
        result.log(Part1.NODE_KEY, description='Starting Node')

        if expected_steps:
            result.eq(
                Part1.total_steps(instructions, nodes),
                expected_steps,
                description='Total Steps',
            )
        else:
            result.log(
                Part1.total_steps(instructions, nodes),
                description='Total Steps',
            )

    @pytest.mark.parametrize(
        "instructions, nodes, expected_steps", 
        [
            (Part2SampleInput.INSTRUCTIONS,  Part2SampleInput.NODES,  6),
            (PuzzleInput.INSTRUCTIONS,       PuzzleInput.NODES,       None), # log result only
        ]
    )
    def test_part2(self, env, result, instructions, nodes, expected_steps):
        node_keys = Part2.get_node_keys(nodes)
        result.log(node_keys, description='Starting Nodes')

        if expected_steps:
            result.eq(
                Part2.total_steps(instructions, nodes, node_keys),
                expected_steps,
                description='Expected Total Steps',
            )
        else:
            result.log(
                Part2.total_steps(instructions, nodes, node_keys),
                description='Total Steps',
            )

