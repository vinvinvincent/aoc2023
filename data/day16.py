import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

SAMPLE_DATA = None
with open(DIR_PATH + '/day16_sample.txt') as f:
    SAMPLE_DATA = f.read().splitlines()

PUZZLE_DATA = None
with open(DIR_PATH + '/day16_puzzle.txt') as f:
    PUZZLE_DATA = f.read().splitlines()

EXPECTED_SAMPLE_ENERGIZED_MAP = '''######....
.#...#....
.#...#####
.#...##...
.#...##...
.#...##...
.#..####..
########..
.#######..
.#...#.#..'''
