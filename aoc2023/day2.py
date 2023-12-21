from data.day2 import Games, Cubes


def is_possible_set(input: Cubes, bag: Cubes):
    return input.blue <= bag.blue and input.red <= bag.red and input.green <= bag.green


def is_possible_game(input: list[Cubes], bag: Cubes):
    return all(is_possible_set(cubes, bag) for cubes in input)


def sum_of_all_possible_game_ids(games: Games, bag: Cubes):
    sum = 0
    for i in range(1, games.total_games() + 1):
        game = games.get_game_number(i)
        sum += i if is_possible_game(game, bag) else 0

    return sum


def power_of_set_of_cubes(input: list[Cubes]):
    red = max([cubes.red for cubes in input])
    green = max([cubes.green for cubes in input])
    blue = max([cubes.blue for cubes in input])
    return red * green * blue


def sum_of_power_of_set_of_cubes(games: Games):
    sum = 0
    for i in range(1, games.total_games() + 1):
        game = games.get_game_number(i)
        power = power_of_set_of_cubes(game)
        sum += power

    return sum
