__author__ = 'matt'

import itertools

def get_dictionary(filepath):
    f = open(filepath, "rb")
    words = f.read().split()
    d = {word: 1 for word in words}
    return d

def number_of_anagrams(word, dic):
    good = 0
    anagrams = [''.join(item) for item in itertools.permutations(word)]
    found = {}
    for anagram in anagrams:
        if anagram == word:
            continue
        if found.has_key(anagram):
            continue
        if dic.has_key(anagram):
            good += 1
            found[anagram] = 1
    return good

my_dict = get_dictionary("Dictionary.txt")

input_words = ['terrains', 'headers', 'tersest', 'angriest',
               'lameness', 'integral', 'staking', 'deposit']
#input_words = ['bat','coal','lots']

for w in input_words:
    print number_of_anagrams(w, my_dict),