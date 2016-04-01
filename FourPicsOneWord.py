import itertools

"""
NOT FINISHED
Need to optimize. Taking too long for some cases...
"""

def get_dictionary(filepath):
    f = open(filepath, "rb")
    words = f.read().split()
    d = {word: 1 for word in words}
    return d


def read_data(filepath):
    f = open(filepath, 'rb')
    raw = f.read().splitlines()
    return raw


def good_words(l, n, d):
    possible = itertools.permutations(l, n)
    good = []
    for item in possible:
        word = ''.join(item)
        if word in d:
            good.append(word)
    return len(good)


def test():
    word_dict = get_dictionary("FourPicsOneWordDictionary.txt")
    letters = [ch for ch in 'heraginmfvttyaac']
    n_letters = 10
    print good_words(letters, n_letters, word_dict)


def code_abbey():
    word_dict = get_dictionary("FourPicsOneWordDictionary.txt")
    data = read_data("FourPicsOneWordTestData.txt")
    n_cases = int(data[0])
    for i in range(n_cases):
        case = data[i+1].split()
        n_letters = int(case[0])
        letters = case[1:]
        n_words = good_words(letters, n_letters, word_dict)
        print n_words,


if __name__ == "__main__":
    test()
