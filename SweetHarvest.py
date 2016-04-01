"""
This code provides the answer for CodeAbbey Problem #60 : "Sweet Harvest"

The problem is to find the best route across a line of 'isles', where each isle offers you
a specific number of 'candies', and each step must jump 1 or 2 isles.

Python 2.7
"""


def candy_count(lc, d, i=0, s=0):
    # memoized dynamic path function

    if i in d:
        return d[i]
    if i > (len(lc) - 3):
        d[i] = lc[i]
        return d[i]
    val1 = candy_count(lc, d, i+2, s)
    val2 = candy_count(lc, d, i+3, s) if i < len(lc) - 3 else 0
    best = max(val1, val2)
    s += best + lc[i]
    d[i] = s
    return s


def test():
    isles = [int(i) for i in '9 7 12 7 16 3 7 17 14 13 4 6 11 6 3 3 5 4 11 3 15 12 14 2 15 19 11 12'.split()]
    my_dict = {}
    result = candy_count(isles, my_dict)
    print result


def code_abbey():
    n_cases = int(raw_input())
    for i in range(n_cases):
        isles = [int(i) for i in raw_input().split()]
        my_dict = {}
        result = candy_count(isles, my_dict)
        print result,

if __name__ == "__main__":
    test()

