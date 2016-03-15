__author__ = 'matt'

def calculate_hand(hand):
    ranks = {str(i):i for i in range(2,10)}
    ranks.update({'T':10, 'J':10, 'Q':10, 'K':10, 'A':11})
    score = 0
    n_aces = 0
    for card in hand:
        if card == 'A':
            n_aces += 1
        score += ranks[card]
    for i in range(n_aces):
        if score > 21:
            score -= 10
    return score


n_hands = int(raw_input())

for i in range(n_hands):
    hand = raw_input().split()
    score = calculate_hand(hand)
    if score > 21:
        score = 'Bust'
    print score,