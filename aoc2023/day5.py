from data.day5 import Almanac, SourceDestRange, SeedRange
from typing import List


def source_to_dest_num(num: int, range_datas: List[SourceDestRange]):
    for range_data in range_datas:
        diff = num - range_data.source_start
        if diff >= 0 and diff <= range_data.range_length:
            return range_data.destination_start + diff

    # Any source numbers that aren't mapped correspond to the same destination number
    return num


def seed_to_all_types(seed: int, almanac: Almanac):
    soil = source_to_dest_num(seed, almanac.seed_to_soil)
    fertilizer = source_to_dest_num(soil, almanac.soil_to_fertilizer)
    water = source_to_dest_num(fertilizer, almanac.fertilizer_to_water)
    light = source_to_dest_num(water, almanac.water_to_light)
    temperature = source_to_dest_num(light, almanac.light_to_temperature)
    humidity = source_to_dest_num(temperature, almanac.temperature_to_humidity)
    location = source_to_dest_num(humidity, almanac.humidity_to_location)

    return soil, fertilizer, water, light, temperature, humidity, location


def seed_to_location(seed: int, almanac: Almanac):
    *_, location = seed_to_all_types(seed, almanac)
    return location


def get_lowest_location_from_seeds(seeds: List[int], almanac: Almanac):
    locations = [seed_to_location(seed, almanac) for seed in seeds]
    return min(locations)


def get_lowest_location_from_seed_ranges(
    seed_ranges: List[SeedRange], almanac: Almanac
):
    locations = []
    for seed_range in seed_ranges:
        for offset in range(seed_range.length):
            locations.append(seed_to_location(seed_range.start + offset, almanac))
    return min(locations)
