from enum import Enum
import math


class Tile(Enum):
    SPACE = '.'
    FWD_MIRROR = '/'
    BACK_MIRROR = '\\'
    VERT_SPLITTER = '|'
    HORI_SPLITTER = '-'


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class Grid:
    def __init__(self, grid):
        # grid is array of string -> self._grid[row][col]
        self._grid = grid
        self._energized_map = list()
        self._history = set()

        for i in range(self.row_count):
            self._energized_map.append([Tile.SPACE.value] * self.col_count)

    def get_tile(self, position):
        return self._grid[position[0]][position[1]]

    @property
    def row_count(self):
        return len(self._grid)

    @property
    def col_count(self):
        return len(self._grid[0])

    @property
    def energized_count(self):
        return self.energized_map_as_text.count('#')

    @property
    def energized_map_as_text(self):
        text = ''
        for row in self._energized_map:
            text += ''.join(c for c in row) + '\n'
        return text[:-1]

    def pass_beam(
        self, position=[0, 0], direction=Direction.RIGHT, recursive=True, verbose=False
    ):
        if verbose:
            print('-' * 10)
            print(
                f'tile={self.get_tile(position)}, direction={direction}, position={position}'
            )

        # block inf. recursion when direction and position exists before
        history = (
            position[0] * math.pow(10, len(str(self.row_count))) + position[1],
            direction,
        )
        if history not in self._history:
            self._history.add(history)
        else:
            return None

        # update energized_map
        self._energized_map[position[0]][position[1]] = '#'
        if verbose:
            print(self.energized_map_as_text)

        # check current tile to determine next tile
        tile = self.get_tile(position)

        new_directions = [direction]

        match tile:
            case Tile.SPACE.value:
                pass

            case Tile.FWD_MIRROR.value:
                match direction:
                    case Direction.UP:
                        new_directions[0] = Direction.RIGHT
                    case Direction.DOWN:
                        new_directions[0] = Direction.LEFT
                    case Direction.LEFT:
                        new_directions[0] = Direction.DOWN
                    case Direction.RIGHT:
                        new_directions[0] = Direction.UP

            case Tile.BACK_MIRROR.value:
                match direction:
                    case Direction.UP:
                        new_directions[0] = Direction.LEFT
                    case Direction.DOWN:
                        new_directions[0] = Direction.RIGHT
                    case Direction.LEFT:
                        new_directions[0] = Direction.UP
                    case Direction.RIGHT:
                        new_directions[0] = Direction.DOWN

            case Tile.VERT_SPLITTER.value:
                match direction:
                    case Direction.UP | Direction.DOWN:
                        pass
                    case Direction.LEFT | Direction.RIGHT:
                        new_directions[0] = Direction.UP
                        new_directions.append(Direction.DOWN)

            case Tile.HORI_SPLITTER.value:
                match direction:
                    case Direction.LEFT | Direction.RIGHT:
                        pass
                    case Direction.UP | Direction.DOWN:
                        new_directions[0] = Direction.LEFT
                        new_directions.append(Direction.RIGHT)

        new_positions = []
        for i in range(len(new_directions)):
            new_position = position.copy()
            new_position[0] += new_directions[i].value[0]
            new_position[1] += new_directions[i].value[1]

            # check if move is ended
            end = False
            if new_position[0] < 0 or new_position[0] >= self.row_count:
                end = True
            if new_position[1] < 0 or new_position[1] >= self.col_count:
                end = True
            new_positions.append(new_position if not end else None)

        # continue the beam(s)
        beams = []
        for i in range(len(new_positions)):
            if new_positions[i]:
                beams.append((new_positions[i], new_directions[i]))

        if verbose:
            print(f'next beams={beams}')

        if recursive:
            for i in range(len(new_positions)):
                if new_positions[i]:
                    self.pass_beam(
                        new_positions[i], new_directions[i], recursive, verbose
                    )
        else:
            return beams
