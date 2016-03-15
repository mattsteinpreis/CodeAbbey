__author__ = 'matt'

n_guesses = int(raw_input())

n_digits = 4

still_ok = [str(i).zfill(n_digits) for i in range(0, int(10**n_digits))]


def similar_numbers(s1, s2):
    l1 = [ch for ch in s1]
    l2 = [ch for ch in s2]
    return sum([ii == jj for ii, jj in zip(l1, l2)])


def remove_numbers(guess, n_same, numbers):
    return [number for number in numbers if similar_numbers(guess, number) == n_same]


for i in range(n_guesses):
    current_guess, n_right = raw_input().split()
    n_right = int(n_right)
    still_ok = remove_numbers(current_guess, n_right, still_ok)

if len(still_ok) > 1:
    print "Not enough guesses",
else:
    print still_ok[0]