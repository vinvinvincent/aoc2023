def get_card_points(set1, set2):
    common_count = len(set1 & set2)
    return 2 ** (common_count - 1) if common_count > 0 else 0


def get_sum_of_card_points(cards: list):
    return sum(get_card_points(card[0], card[1]) for card in cards)


def do_card_game_by_winning_copies(card_idx: int, card: list, card_instances: list):
    common_count = len(card[0] & card[1])

    # win copies of the scratchcards below the winning card
    # equal to the number of matches
    if common_count > 0:
        for i in range(
            card_idx + 1, min(card_idx + 1 + common_count, len(card_instances))
        ):
            card_instances[i] += card_instances[card_idx]


def get_total_cards_by_wining_copies(cards: list):
    count = len(cards)
    card_instances = [1] * count
    for i in range(count):
        do_card_game_by_winning_copies(i, cards[i], card_instances)

    return sum(card_instances)
