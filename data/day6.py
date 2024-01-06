from dataclasses import dataclass


@dataclass
class Race:
    time: int
    distance: int


def parse_race_data(text):
    lines = text.strip().split('\n')
    time_values = [int(value) for value in lines[0].split()[1:]]
    distance_values = [int(value) for value in lines[1].split()[1:]]
    race_list = [
        Race(time, distance) for time, distance in zip(time_values, distance_values)
    ]
    return race_list


SAMPLE_DATA_TEXT = '''
Time:      7  15   30
Distance:  9  40  200'''

PUZZLE_DATA_TEXT = '''Time:        53     83     72     88
Distance:   333   1635   1289   1532'''


SAMPLE_DATA = parse_race_data(SAMPLE_DATA_TEXT)
PUZZLE_DATA = parse_race_data(PUZZLE_DATA_TEXT)

SAMPLE_DATA_PART1 = SAMPLE_DATA
PUZZLE_DATA_PART1 = PUZZLE_DATA

SAMPLE_DATA_PART2 = Race(71530, 940200)
PUZZLE_DATA_PART2 = Race(53837288, 333163512891532)
