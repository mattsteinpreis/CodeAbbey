__author__ = 'matt'


def duel_outcome(pa, pb, n):
    alans_wins = 0
    bobs_wins = 0
    total_prob = 0
    for i in range(n):
        alans_turn = (1-total_prob)*pa
        alans_wins += alans_turn
        total_prob += alans_turn
        bobs_turn = (1-total_prob)*pb
        total_prob += bobs_turn
        bobs_wins += bobs_turn
    return alans_wins, bobs_wins

duel_outcome(.3,.5, 1000)

# input
n_duels = int(raw_input())
for i in range(n_duels):
    p_a, p_b = [int(j)/100. for j in raw_input().split()]
    print int(duel_outcome(p_a, p_b, 1000)[0]),