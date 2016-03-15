__author__ = 'matt'


def calc_time(x, y, n):
    return n/(1./x + 1./y)

def round_to_multiple(number, mark):
    return int(number + number % mark)

#n_lines = int(raw_input())

for line in range(n_lines):
#    x, y, n = [int(j) for j in raw_input().split()]
    x, y, n = [3, 5, 4]
    exact = calc_time(x, y, n)
    n_full_pages = int(exact/x) + int(exact/y)

    while n_full_pages < n:
        rem_x = exact % x
        rem_y = exact % y
        if rem_x == 0:
            closest = y
        elif rem_y == 0:
            closest = x
        else:
            closest = x if rem_x < rem_y else y
        exact = round_to_multiple(exact, closest)

    print exact,