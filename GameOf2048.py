__author__ = 'matt'

"""
Code for CodeAbbey #91: Game of 2048

The problem gives a board set-up and a list of moves,
and asks for the number of each 2, 4, etc.

TO-DO:
- format so multiple digits look better
- map directional inputs to letters

BUGS:

"""
import string

class Board(object):
    def __init__(self):
        self.tiles = []
        self.move_inv = {'R':'R', 'L':'L', 'U':'D', 'D':'U'}

    def fill(self, l):
        m = []
        for i in range(4):
            m.extend([ch for ch in l[i*4:((i+1)*4)]])
        self.tiles = m

    def show(self):
        for i in range(4):
            print ' '.join(self.tiles[i*4:((i+1)*4)])
        print

    def rotate(self, d):
        s = self.tiles
        if d == 'L':
            t = s[3::-1]+s[7:3:-1]+s[11:7:-1]+s[15:11:-1]
        elif d == 'U':
            t = s[12::-4] + s[13::-4] + s[14::-4] + s[15::-4]
        elif d == 'D':
            t = s[3::4] + s[2::4] + s[1::4] + s[::4]
        else:
            t = s
        self.tiles = t

    def move(self, d):
        self.rotate(d)
        self.condense()
        self.rotate(self.move_inv[d])

    def condense(self):
        # everything goes to the right
        nt = []
        for i in range(4):
            row_i = self.tiles[i*4:((i+1)*4)]
            # move all dashes to the left
            row_i, n_num = shift_dashes(row_i)
            marker = 3
            while marker > (4 - n_num):
                a, b = row_i[marker-1], row_i[marker]
                if a == b:
                    row_i[marker] = str(int(a) + int(b))
                    row_i[marker - 1] = '-'
                    row_i, n_num = shift_dashes(row_i)
                marker -= 1
            nt.extend(row_i)
            print nt
        self.tiles = nt


def shift_dashes(r):
    d = [ri for ri in r if ri == '-']
    nd = [ri for ri in r if ri != '-']
    return d + nd, len(nd)


def interactive():
    start = '2422442242422222'
    b = Board()
    b.fill(start)
    b.show()
    while True:
        m = raw_input()
        if m == 'q':
            return
        b.move(m.upper())
        b.show()

def test():
    start = '2422442242422222'
    b = Board()
    b.fill(start)
    b.show()
    b.move('U')
    b.show()
    b.move('L')
    b.show()
    b.move('D')
    b.show()
    b.move('R')
    b.show()
    return None


def CodeAbbey():
    pass


if __name__ == '__main__':
    test()