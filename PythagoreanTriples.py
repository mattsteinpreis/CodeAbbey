__author__ = 'matt'

from math import sqrt


def find_pythagorean_triple(abc_sum):
    abc_sq = abc_sum*abc_sum
    for a in xrange(1, abc_sum/3):
        print a
        a_sq = a*a
        for b in xrange(a+1, abc_sum/2):
            if a + b + b + 1 > abc_sum:
                break
            b_sq = b*b
            c = sqrt(a_sq + b_sq)
            #print a, b, c
            if a + b + c == abc_sum:
                return a, b, int(c)
    return None


n_cases = int(raw_input())

for i in range(n_cases):
    s = float(raw_input())
    triple = find_pythagorean_triple(s)