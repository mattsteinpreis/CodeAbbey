__author__ = 'matt'


def side_length(xa, ya, xb, yb):
    return ((xa-xb)**2 + (ya-yb)**2)**0.5


def calculate_triangle_area_sides(la, lb, lc):
    s = (la+lb+lc)/2.
    return (s*(s-la)*(s-lb)*(s-lc))**0.5


def calculate_triangle_area_points(xa, ya, xb, yb, xc, yc):
    l_ab = side_length(xa, ya, xb, yb)
    l_ac = side_length(xa, ya, xc, yc)
    l_bc = side_length(xb, yb, xc, yc)
    return calculate_triangle_area_sides(l_ab, l_ac, l_bc)


def calculate_polygon_area(coordinates):
    # assumes points in CW or CCW order
    n_points = len(coordinates)
    x0, y0 = coordinates[0]
    total_area = 0
    for i in xrange(1, n_points-1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i+1]
        total_area += calculate_triangle_area_points(x0, y0, x1, y1, x2, y2)
    return total_area


n_sides = int(raw_input())
xy_list = []
for i in xrange(n_sides):
    xy_list.append([int(j) for j in raw_input().split()])
polyarea = calculate_polygon_area(xy_list)
print polyarea