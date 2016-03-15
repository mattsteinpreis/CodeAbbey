__author__ = 'matt'

MAX = 3000000


def generate_primes(up_to):
    numbers = range(3, up_to, 2)
    not_primes = set()
    for n in numbers:
        if n*n > up_to:
            break
        if n in not_primes:
            continue
        current = n*n
        while(current < up_to):
            not_primes.add(current)
            current += 2*n
    allnumbers = set(numbers)
    primes = allnumbers.difference(not_primes)
    return sorted([2]+list(primes))

n_cases = int(raw_input())
desired_indices = [int(j) for j in raw_input().split()]

my_primes = generate_primes(MAX)
#desired_indices = [7,1,199999, 4]
for ind in desired_indices:
    print my_primes[ind-1],