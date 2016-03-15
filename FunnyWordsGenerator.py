__author__ = 'matt'

def get_next(x, a = 445, c=700001, m=2097152):
    return (a*x+c) % m

def get_letter(number, vowel = False):
    consonants = 'bcdfghjklmnprstvwxz'
    vowels = 'aeiou'
    if vowel:
        return vowels[number % 5]
    return consonants[number % 19]

n_words, x0 = [int(j) for j in raw_input().split()]
#n_words, x0 = 3, 0

n_letters = [int(j) for j in raw_input().split()]
#n_letters = [4,5,6]

for i in range(n_words):
    word = ''
    for j in range(n_letters[i]):
        x0 = get_next(x0)
        letter = get_letter(x0, j % 2 != 0)
        word = word + letter
    print word,




