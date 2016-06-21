import string
import requests

# requests doesn't work on site; must provide list explicitly
word_list = [a.decode()
             for a in requests.get('https://gist.githubusercontent.com/' +
                                   'deekayen/4148741/raw/01c6252ccc5b5fb307' +
                                   'c1bb899c95989a8a284616/' +
                                '1-1000.txt').content.splitlines()]


def rotn_decode_letter(l, n):
    base = string.ascii_uppercase
    cipher = base[n:] + base[:n]
    i = cipher.find(l)
    return base[i]


def rotn_decode(p, n):
    dec = [rotn_decode_letter(ch, n) if ch != ' ' else ' ' for ch in p]
    return ''.join(dec)


def score(phrase, wl):
    s = set(wl)
    sc = 0
    for word in phrase.split():
        #print(word.lower(), word.lower() in s)
        if word.lower() in s:
            sc += 1
    return sc


def determine_shift(l, wl):
    best_score = -1
    best_i = 0
    for i in range(1, 26):
        dec = rotn_decode(l, i)
        sc = score(dec, wl)
        #print(dec, sc)
        if sc > best_score:
            best_score = sc
            best_i = i
    return best_i


def crack(l, wl):
    shift = determine_shift(l, wl)
    shifted = rotn_decode(l, shift)
    return shifted, shift


def test():
    a = 'XIP DBSFT PG ESFBNT'
    cracked, shift = crack(a, word_list)
    print(cracked.split()[:3], shift)
    a = 'VJQWIJ KV OCMGU VJKPIU XGTA SWGGT'
    cracked, shift = crack(a, word_list)
    print(cracked.split()[:3], shift)


def main():
    n = int(input())
    lines = []
    for i in range(n):
        lines.append(input())
    for line in lines:
        cracked, shift = crack(line, word_list)
        print(' '.join(cracked.split()[:3]), shift)


if __name__ == '__main__':
    #print(word_list)
    main()