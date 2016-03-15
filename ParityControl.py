def countBits(s):
    return sum([int(i) for i in s])


def getNBitBinary(i, n):
    a = abs(i)
    b = '%0*d' % (n, int(bin(a)[2:]))
    return b


def getDecimal(binstr):
    return int(binstr, 2)


def getAscii(i):
    return chr(i)


def decodeInt(i):
    _bin = getNBitBinary(i, 8)
    nBits = countBits(_bin)
    if nBits % 2 != 0:
        return None
    _bin = '0'+_bin[1:]
    dec = getDecimal(_bin)
    ch = getAscii(dec)
    return ch

# line = [int(j) for j in raw_input().split()]
line = [65, 238, 236, 225, 46]

message = []
for number in line:
    letter = decodeInt(number)
    message.append(letter)
    if letter == '.':
        break

print ''.join([ch for ch in message if ch])
