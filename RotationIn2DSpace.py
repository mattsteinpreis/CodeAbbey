__author__ = 'matt'

import math


def radius(x, y):
    return math.sqrt(x**2+y**2)


def rounder(x):
    if x < 0:
        return int(x-0.5)
    return int(x+0.5)


def rotate(x, y, a, ccw=True):
    r = radius(x, y)
    a_o = math.atan2(y, x)
    c = 1 if ccw else -1
    a_rad = a * 2 * math.pi / 360
    a_f = a_o + c * a_rad
    x_f = r * math.cos(a_f)
    y_f = r * math.sin(a_f)
    return rounder(x_f), rounder(y_f)


n_stars, angle = [int(i) for i in raw_input().split()]
stars = []
for j in range(n_stars):
    star, xj, yj = raw_input().split()
    xj, yj = int(xj), int(yj)
    xnew, ynew = rotate(xj, yj, angle, ccw=True)
    stars.append((star, xnew, ynew))

sorted_stars = sorted(stars, key=lambda x: (x[2], x[1]))
for st in sorted_stars:
    print st[0],

### EXAMPLE
#input data:
#4 45
#Deneb -10 10
#Algol 10 10
#Sirius -10 -10
#Mira 10 -10
#answer:
#Sirius Deneb Mira Algol