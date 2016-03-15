__author__ = 'matt'

import math


def parse_time(time):
    minute = int(time[-2:])
    hour = int(time[:(len(time)-3)]) % 12
    return hour, minute


def get_angles(hour, minute):
    angle_minute = minute/60. * 2 * math.pi
    angle_hour = (hour+ minute/60.)/12. * 2 * math.pi
    return angle_hour, angle_minute


def get_coordinates(angle, r, x0, y0):
    x = r * math.sin(angle)
    y = r * math.cos(angle)
    return round(x0+x, 8), round(y0+y, 8)


length_minute = 9
length_hour = 6

n_clocks = int(raw_input())
times = [parse_time(t) for t in raw_input().split()]

for h, m in times:
    ang_h, ang_m = get_angles(h, m)
    xh, yh = get_coordinates(ang_h, length_hour, 10, 10)
    xm, ym = get_coordinates(ang_m, length_minute, 10, 10)
    print xh, yh, xm, ym,