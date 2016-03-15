__author__ = 'matt'

from math import sqrt


def solve_quadratic_equation(a, b, c):
    discriminant = (b * b) - (4 * a * c)
    if discriminant < 0:
        complex_a = int(-1 * b / (2 * a))
        complex_b = int(sqrt(-1 * discriminant) / (2 * a))
        root_1 = "{}+{}i".format(complex_a, complex_b)
        root_2 = "{}-{}i".format(complex_a, complex_b)
    else:
        root_1 = int((-1 * b + sqrt(discriminant)) / (2 * a))
        if discriminant > 0:
            root_2 = int((-1 * b - sqrt(discriminant)) / (2 * a))
        else:
            root_2 = root_1
    return [str(root_1), str(root_2)]

n_cases = int(raw_input())


for i in range(n_cases):
    ai, bi, ci = [float(j) for j in raw_input().split()]
    roots = solve_quadratic_equation(ai, bi, ci)
    print "{} {}".format(roots[0], roots[1])
    if i < n_cases-1:
        print ";",