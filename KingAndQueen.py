__author__ = 'matt'

def queen_can_reach(sqK, sqQ):
    kfile = ord(sqK[0])
    qfile = ord(sqQ[0])
    krank = int(sqK[1])
    qrank = int(sqQ[1])

    filediff = abs(kfile - qfile)
    rankdiff = abs(krank - qrank)

    if filediff == 0 or rankdiff == 0 or rankdiff == filediff:
        return 'Y'
    return 'N'

n_moves = int(raw_input())

for i in range(n_moves):
    k, q = raw_input().split()
    print queen_can_reach(k, q),
