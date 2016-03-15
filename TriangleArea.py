__author__ = 'matt'


n = int(raw_input())

def side_length(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def calculate_area(l1, l2, l3):
    s = (l1+l2+l3)/2.
    return (s*(s-l1)*(s-l2)*(s-l3))**0.5

for i in range(n):
    x1, y1, x2, y2, x3, y3 = [int(j) for j in raw_input().split()]
    l1 = side_length(x1,y1,x2,y2)
    l2 = side_length(x1,y1,x3,y3)
    l3 = side_length(x2,y2,x3,y3)
    print calculate_area(l1,l2,l3),