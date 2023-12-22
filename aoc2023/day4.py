def get_card_points(set1, set2):
    common_numbers = set1 & set2
    common_count = len(common_numbers)
    return 2 ** (common_count - 1) if common_count > 0 else 0


def get_sum_of_card_points(cards: list):
    return sum(get_card_points(card[0], card[1]) for card in cards)
