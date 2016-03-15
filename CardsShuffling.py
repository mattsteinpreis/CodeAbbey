__author__ = 'matt'

def int_to_card(i):
    suits = ['C', 'D', 'H', 'S']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suit = suits[i/13]
    rank = ranks[i % 13]
    return suit+rank

rands = [int(j) for j in raw_input().split()]
deck = range(52)

for i in range(52):
    swap = rands[i] % 52
    deck[i], deck[swap] = deck[swap], deck[i]

for i in deck:
    print int_to_card(i),
