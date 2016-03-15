__author__ = 'matt'

my_input = ['00', '0.']


width = 2 # the number of cells on the X axis
height = 2  # the number of cells on the Y axis
rows = {i:[] for i in range(height)}
columns = {i:[] for i in range(width)}
nodes = []
for j in xrange(height):
    line = my_input[j]  # width characters, each either 0 or .
    for i, ch in enumerate(line):
        if ch == '0':
            nodes.append([i, j])
            rows[j].append(j)
            columns[i].append(i)

for node in nodes:
    x1, y1 = node
    to_the_right = [x for x in rows[y1] if x > x1]
    if to_the_right:
        x2 = to_the_right[0]
        y2 = y1
    else:
        x2, y2 = -1, -1
    to_the_bottom = [y for y in columns[x1] if y > y1]
    if to_the_bottom:
        x3 = x1
        y3 = to_the_bottom[0]
    print "{} {} {} {} {} {}".format(x1, y1, x2, y2, x3, y3)