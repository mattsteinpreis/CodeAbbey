__author__ = 'matt'

import math


def mean(x):
    return sum(x) / float(len(x))

def sd(x):
    mn = mean(x)
    errs = [abs(xi-mn) for xi in x]
    sqerrs = [i*i for i in errs]
    return math.sqrt(mean(sqerrs))

n_stocks = int(raw_input())

for i in range(n_stocks):
    line = raw_input().split()

    line = 'BLEP 43 44 43 43 45 45 47 48 46 46 44 42 43 42'.split()
    stock = line[0]
    shares = [int(j) for j in line[1:]]
    stdev = sd(shares)
    mn = mean(shares)
    profit = mn*0.01
    print stdev, profit
    if stdev > profit*4:
        print stock,