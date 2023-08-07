def card_value(card):
    # Sets the values for the cards going forward
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return card_values[card[1:]]

def check_straight(card1, card2, card3):
    # Checks if cards are straight, and if both straight, then highest value
    cards = [card1, card2, card3]
    cards.sort(key=card_value)
    if card_value(cards[0]) + 1 == card_value(cards[1]) and card_value(cards[1]) + 1 == card_value(cards[2]):
        return card_value(cards[2])
    return 0

def check_3ofa_kind(card1, card2, card3):
    # checks if the cards form a three-of-a-kind and return the value
    if card_value(card1) == card_value(card2) == card_value(card3):
        return card_value(card1)
    return 0

def check_royal_flush(card1, card2, card3):
    #  checks if the cards form a royal flush and return 14 (Ace) or 0
    if check_straight(card1, card2, card3) == 14:
        return 14
    return 0

def play_cards(left1, left2, left3, right1, right2, right3):
    # Basic ideas to determine player cards
    left_straight = check_straight(left1, left2, left3)
    right_straight = check_straight(right1, right2, right3)

    left_3ofa_kind = check_3ofa_kind(left1, left2, left3)
    right_3ofa_kind = check_3ofa_kind(right1, right2, right3)

    left_royal_flush = check_royal_flush(left1, left2, left3)
    right_royal_flush = check_royal_flush(right1, right2, right3)

    if left_royal_flush or right_royal_flush:
        # If one of the players has a royal flush, then they more than likely cheated
        if left_royal_flush > right_royal_flush:
            return -1
        elif left_royal_flush < right_royal_flush:
            return 1
        else:
            return 0

    if left_3ofa_kind or right_3ofa_kind:
        # if a player pulls a 3 of a kind, and the other cannot match/exceed, a winner is decided
        if left_3ofa_kind > right_3ofa_kind:
            return -1
        elif left_3ofa_kind < right_3ofa_kind:
            return 1
        else:
            return 0

    if left_straight or right_straight:
        # if a player pulls a straight, and the other cannot match/exceed, a winner is decided
        if left_straight > right_straight:
            return -1
        elif left_straight < right_straight:
            return 1
        else:
            return 0

    # if none of the conditions proc, we call a draw
    return 0

# example
result = play_cards()
print(result)
