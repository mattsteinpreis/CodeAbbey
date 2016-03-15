__author__ = 'matt'


def get_next(x, a = 445, c=700001, m=2097152):
    return (a*x+c) % m


def get_letter(number, vowel = False):
    consonants = 'bcdfghjklmnprstvwxz'
    vowels = 'aeiou'
    if vowel:
        return vowels[number % 5]
    return consonants[number % 19]


seed = int(raw_input())
n_words = 900000

max_count = 0
max_word = ''
word_counts = {}
for i in range(n_words):
    word = ''
    for j in range(6):
        seed = get_next(seed)
        isVowel = j % 2 != 0
        word = word + get_letter(seed, isVowel)
    if word_counts.has_key(word):
        word_counts[word] += 1
    else:
        word_counts[word] = 1
    this_count = word_counts[word]
    if this_count > max_count:
        max_count = this_count
        max_word = word

print max_word