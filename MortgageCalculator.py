__author__ = 'matt'

# get input
loan, rate, months = [int(j) for j in raw_input().split()]

factor = 1 + rate / 100. / 12.

factor_sum = 0
for i in range(months):
    factor_sum += factor**i

payment = int((loan*factor**months)/factor_sum + 0.5)
print payment