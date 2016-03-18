__author__ = 'matt'

class Life(object):
    def __init__(self, nx = 100, ny = 100):
        self.grid = {}
        self.nx = nx
        self.ny = ny
        self.organisms = []

    def _print(self):
        if self.grid == {}:
            print "No grid input."
            return
        for i in range(self.ny):
            row = ''
            for j in range(self.nx):
                row = row + self.grid[(i, j)]
            print row

    def summary(self):
        self._print()
        print "Organisms at:", self.organisms
        print "Number of organisms:", len(self.organisms)

    def input_row(self, ny, row_str):
        for i, ch in enumerate(row_str):
            self.grid[(ny, i)] = ch
            if ch == 'X':
                self.organisms.append((ny, i))


### testing
test_grid = ['-----',
             '-----',
             '-XXX-',
             '-----',
             '-----']

l = Life(5, 5)
l._print()
for i_row in range(len(test_grid)):
    l.input_row(i_row, test_grid[i])
l._print()
l.summary()