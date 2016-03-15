__author__ = 'matt'


def possible_breasts_per_pig(bTotal):
    return range(6, bTotal+1, 2)


def possible_pig_stats(b, l):
    possible_n = possible_breasts_per_pig(b)
    stats = []
    for n in possible_n:
        p = (b-l) / float(n - 4)
        if p % 1 == 0 and p * 4 <= l and p*n != b:
            stats.append((p, n))
    return stats


n_cases = int(raw_input())

for i in range(n_cases):
    legs, breasts = [int(j) for j in raw_input().split()]
    possible_solutions = possible_pig_stats(breasts, legs)
    print sum(solutions),