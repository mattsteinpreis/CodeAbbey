__author__ = 'matt'

from math import pi, tan

def calculate_height(d,b):
    a = (b - 90)/360.*2*pi
    return d * tan(a)

def nearest_int(n):
    if n > 0:
        return int(n+0.5)
    return int(n-0.5)

n_trees = int(raw_input())

for i in range(n_trees):
    distance, angle = [float(j) for j in raw_input().split()]
    height = calculate_height(distance, angle)
    print nearest_int(height),