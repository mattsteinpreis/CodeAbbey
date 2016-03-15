__author__ = 'matt'

# input
width, height, str_len = [int(j) for j in raw_input().split()]
#width, height, str_len = [9, 3, 4]
n_steps = 100

print 0,
print 0,

x = 0
y = 0

dx = 1
dy = 1
for i in range(n_steps):
    if x + str_len == width:
        dx = -1
    if x == 0:
        dx = 1
    if y == 0:
        dy = 1
    if y == height-1:
        dy = -1
    x = x + dx
    y = y + dy
    print x, y,