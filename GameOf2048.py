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

    def rotate(self, d):
        s = self.to_string()
        if d == 'L':
            t = s[3::-1]+s[7:3:-1]+s[11:7:-1]+s[15:11:-1]
        self.fill(t)

    def move(self, d):
        self.rotate(d)
        #self.condense()
        self.rotate(self.move_inv[d])


def test():
    start = '2222424422244442'
    b = Board()
    b.fill(start)
    b.show()
    b1 = b.to_string()
    b.move('L')
    b2 = b.to_string()


def CodeAbbey():
    pass


if __name__ == '__main__':
    test()