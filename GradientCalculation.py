__author__ = 'matt'

import math


def formula(x, y, a, b, c):
    t1 = (x-a)**2
    t2 = (y-b)**2
    expo = (x+a)**2 + (y-b)**2
    t3 = c*math.exp(-expo)
    return t1 + t2 + t3


def gradient(x, y, fun, *args):
    dt = 1e-9
    t0 = fun(x, y, *args)
    tx = fun(x + dt, y, *args)
    ty = fun(x, y + dt, *args)
    gx = (tx - t0) / dt
    gy = (ty - t0) / dt
    return gx, gy


def angle(x, y):
    rad = math.atan2(y, x)
    deg = rad/(2*math.pi)*360
    return int(deg+0.5)

n, aa, bb, cc = [float(i) for i in raw_input().split()]
for j in range(int(n)):
    xi, yi = [float(i) for i in raw_input().split()]
    gxi, gyi = gradient(xi, yi, formula, aa, bb, cc)
    ang = angle(gxi, gyi)
    print ang,

