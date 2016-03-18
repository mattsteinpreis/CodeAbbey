__author__ = 'matt'

class Life(object):
    def __init__(self, nx = 100):
        self.grid = {}
        self.nx = nx
        self.ny = 0
        self.organisms = []
        self.organism_count = 0

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

    def input_row(self, row_str):
        for i, ch in enumerate(row_str):
            self.grid[(self.ny, i)] = ch
            if ch == 'X':
                self.organisms.append((self.ny, i))
                self.organism_count += 1
        self.ny += 1

    def num_neighbors(self, i, j):
        nn = 0
        for ii in range(i-1,i+2):
            for jj in range(j-1, j+2):
                if (ii, jj) == (i, j):
                    continue
                if self.grid[(ii, jj)] == 'X':
                    nn += 1
        return nn

    def evolve(self):
        deaths = []
        births = []
        for i in range(1, self.ny-1):
            for j in range(1, self.nx-1):
                cell = self.grid[(i,j)]
                n_neighbors = self.num_neighbors(i, j)
                if cell == 'X' and n_neighbors not in [2, 3]:
                    deaths.append((i, j))
                if cell == '-' and n_neighbors == 3:
                    births.append((i, j))
        for death in deaths:
            self.grid[death] = '-'
        for birth in births:
            self.grid[birth] = 'X'
        self.organism_count -= len(deaths)
        self.organism_count += len(births)

    def step(self, printing = False):
        self.evolve()
        if printing:
            self._print()

    def full_evolve(self, n, show_n_org = True):
        for i in range(n):
            self.step()
            if show_n_org:
                print self.organism_count,


### testing
test_grid = [
'---XX--',
'X-----X',
'--XX-X-',
'XX--XX-',
'XX-XX--',
]

buffer_length = 5
input_row_length = 7
full_row_length = buffer_length*2+input_row_length

life = Life(full_row_length)
life._print()
for i_row in range(buffer_length):
    life.input_row('-'*full_row_length)
for i_row in range(len(test_grid)):
    life.input_row('-'*buffer_length + test_grid[i_row] + '-'*buffer_length)
for i_row in range(buffer_length):
    life.input_row('-'*full_row_length)

n_steps = 5
organism_counts = []

for i in range(n_steps):
    life.step(True)
    organism_counts.append(life.organism_count)
    print organism_counts

for count in organism_counts:
    print count,