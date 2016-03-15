__author__ = 'matt'


def dice_counts(dice):
    counts = [0]*6
    for die in dice:
        counts[die-1] += 1
    return counts


def hand_rank(dice):
    s = sorted(dice)
    if s == range(1, 6):
        return "small-straight"
    if s == range(2, 7):
        return "big-straight"
    counts = sorted(dice_counts(dice), reverse=True)
    if counts[0] == 5:
        return "yacht"
    if counts[0] == 4:
        return "four"
    if counts[0] == 3:
        if counts[1] == 2:
            return "full-house"
        return "three"
    if counts[0] == 2:
        if counts[1] == 2:
            return "two-pairs"
        return "pair"
    return "none"


n_hands = int(raw_input())
for hand in range(n_hands):
    hand_dice = [int(j) for j in raw_input().split()]
    print hand_rank(hand_dice),