__author__ = 'matt'


from random import randint
from math import sqrt

def mean(x):
    return sum(x) / float(len(x))


def sd(x):
    mn = mean(x)
    err = [abs(i-mn)**2 for i in x]
    var = sum(err) / float(len(x))
    return sqrt(var)


def median(x):
    s = sorted(x)
    half = len(x) / 2
    if len(x) % 2 == 0:
        m1 = s[half]
        m2 = s[half-1]
        return 0.5 * (m1+m2)
    return s[half]


def get_stats(x):
    s = {}
    s["mean"] = mean(x)
    s["sd"] = sd(x)
    s["max"] = max(x)
    s["min"] = min(x)
    s["median"] = median(x)
    return s


def rand_gen_rolls(n_dice, n_sides, n_rolls):
    x = []
    for i in range(n_rolls):
        total = 0
        for j in range(n_dice):
            total += randint(1, n_sides)
        x.append(total)
    return x


def find_best_stats(true_stats, roll_stats):
    list_of_bests = {}
    for stat_key in roll_stats.keys():
        roll_stat = roll_stats[stat_key]
        stat_best = 999
        dice_best = ''
        for dice_key in true_stats.keys():
            true_stat = true_stats[dice_key][stat_key]
            error = abs(true_stat - roll_stat)
            if error < stat_best:
                stat_best = error
                dice_best = dice_key
        if list_of_bests.has_key(dice_best):
            list_of_bests[dice_best] += 1
        else:
            list_of_bests[dice_best] = 1
    # find dice with most wins
    mostwins = 0
    top = ''
    for key, val in zip(list_of_bests.keys(), list_of_bests.values()):
        if val > mostwins:
            mostwins = val
            top = key
    return top


def find_best_counts(true_counts, test_counts):
    best_score = 999999
    best_dice = ''
    for dice in true_counts.keys():
        true_count_i = true_counts[dice]
        score = 0
        for count in true_count_i.keys():
            true_val = true_count_i[count]
            test_val = test_counts[count]
            score += (true_val - test_val)**2
        score = sqrt(score)
        if score < best_score:
            best_score = score
            best_dice = dice
    return best_dice


def get_roll_count(x, max, normalize = True):
    counts = {}
    for i in range(max):
        counts[i] = 0
    for xi in x:
        counts[xi] += 1
    if normalize:
        for key, val in zip(counts.keys(), counts.values()):
            counts[key] = val / float(len(x))
    return counts


possible_n_dice = [1,2,3,4,5]
possible_n_sides = [2,4,6,8,10,12]
n_random_rolls = 10000

dice_stats = {}
dice_counts = {}
for dice in possible_n_dice:
    for side in possible_n_sides:
        name = "{}d{}".format(dice, side)
        rand_rolls = rand_gen_rolls(dice, side, n_random_rolls)
        dice_stats[name] = get_stats(rand_rolls)
        dice_stats[name]["min"] = dice
        dice_stats[name]["max"] = dice*side
        dice_counts[name] = get_roll_count(rand_rolls, 5*12)


# get stats for all cases
n_cases = 10

for i in range(n_cases):
    rolls = [int(j) for j in raw_input().split() if j != '0']
    case_counts = get_roll_count(rolls, 5*12)
    winner = find_best_counts(dice_counts, case_counts)
    print winner,