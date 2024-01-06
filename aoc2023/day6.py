from data.day6 import Race


def get_ways_to_win(race: Race):
    ways = 0
    for hold_sec in range(1, race.time + 1):
        remaining_sec = race.time - hold_sec
        # print(
        #     f'hold_sec={hold_sec}, remaining_sec={remaining_sec}, dist={remaining_sec * hold_sec}, race.distance={race.distance}'
        # )
        if remaining_sec > 0:
            if remaining_sec * hold_sec > race.distance:
                ways += 1
            else:
                if ways == 0:
                    continue
                else:
                    return ways
    return ways


def get_product_of_ways(races: list):
    ways = 1
    for i in range(len(races)):
        ways *= get_ways_to_win(races[i])
    return ways


def get_part1(args):
    return get_product_of_ways(args)


def get_part2(args):
    return get_ways_to_win(args)
