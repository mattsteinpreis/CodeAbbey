__author__ = 'matt'

from math import sqrt


def new_location(x0, y0, d, move):
    diag = d
    dx = 0.5 * diag
    dy = sqrt(diag*diag - dx*dx)
    moves = {'A': (2*dx, 0.0),
             'B': (dx, dy),
             'C': (-dx, dy),
             'D': (-2*dx, 0.0),
             'E': (-dx, -dy),
             'F': (dx, -dy)}
    movex, movey = moves[move]
    return x0+movex, y0+movey


def calculate_distance(x0, y0, xf, yf):
    dx = abs(xf-x0)
    dy = abs(yf-y0)
    return sqrt(dx*dx + dy*dy)

tile_size = 1.0

n_trips = int(raw_input())

for trip in range(n_trips):
    move_set = raw_input()
    x, y = 0.0, 0.0
    for move_i in move_set:
        x, y = new_location(x, y, tile_size, move_i)
    print round(calculate_distance(0.0, 0.0, x, y), 8),
