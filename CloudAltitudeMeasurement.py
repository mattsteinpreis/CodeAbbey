__author__ = 'matt'

"""
Solves Code Abbey problem #172: Cloud Altitude Measurement
http://www.codeabbey.com/index/task_view/cloud-altitude-measurement

"""

import math


def deg_to_rad(a):
    return a * math.pi / 180


def calculate_height(d, a, b, to_radian=False):
    if to_radian:
        a = deg_to_rad(a)
        b = deg_to_rad(b)
    tan_a = math.tan(a)
    tan_b = math.tan(b)
    num = d * tan_a
    den = 1 - (tan_a / tan_b)
    return num / den


n_cases = int(raw_input())
for case in range(n_cases):
    inp = raw_input().split()
    d1 = int(inp[0])
    angle1 = float(inp[1])
    angle2 = float(inp[2])
    h = calculate_height(d1, angle1, angle2, to_radian=True)
    print int(round(h)),
    