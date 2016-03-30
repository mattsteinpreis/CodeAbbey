__author__ = 'matt'

"""
Code for CodeAbbey #91: Game of 2048

The problem gives a board set-up and a list of moves,
and asks for the number of each 2, 4, etc.
"""


class Board(object):
    def __init__(self):
        self.tiles = None
        self.move_inv = {'R':'R', 'L':'L', 'U':'D', 'D':'U'}

    def to_string(self):
        return ''.join([ch for row in self.tiles for ch in row])

    def fill(self, s):
        m = []
        for i in range(4):
            m.append([ch for ch in s[i*4:((i+1)*4)]])
        self.tiles = m

    def show(self):
        for row in self.tiles:
            print ' '.join(row)
        print

    def rotate(self, d):
        s = self.to_string()
        if d == 'L':
            t = s[3::-1]+s[7:3:-1]+s[11:7:-1]+s[15:11:-1]
        elif d == 'U':
            t = s[12::-4] + s[13::-4] + s[14::-4] + s[15::-4]
        elif d == 'D':
            t = s[3::4] + s[2::4] + s[1::4] + s[::4]
        else:
            t = s
        self.fill(t)

    def move(self, d):
        self.rotate(d)
        self.condense()
        self.rotate(self.move_inv[d])

    def condense(self):
        # everything goes to the right
        nt = []
        for row in self.tiles:
            row_i = row
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
            nt.append(row_i)
        self.tiles = nt


def shift_dashes(r):
    d = [ri for ri in r if ri == '-']
    nd = [ri for ri in r if ri != '-']
    return d + nd, len(nd)


def test():
    start = '------------2222'
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