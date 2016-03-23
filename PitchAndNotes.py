__author__ = 'matt'

"""
Calculating the standard frequency for a given note+octave.
e.g. A4 = 440 Hz, C4 = 261.63 Hz

"""

def within(test,  val, d):
    return abs(test - val) < d


def find_octave(f):
    b=41.203445
    o = 0
    o_base = b
    while f < o_base:
        o += 1
        o_base *= 2
        if o > 20:
            return "Octave error: {}".format(f)
    return o


def find_pitch(f, on):
    b=41.203445
    step = 2.**(1./12.)
    pn = 0
    pf = b*(2.**on)
    while not within(f, pf, pf/100.):
        pf *= step
        pn += 1
        if pn > 13:
            return "Pitch Error: {}".format(f)
    return pf


def frequency(name):
    # assumes only single-digit octaves
    octave = int(name[-1])
    pitch = name[:-1]
    base = 440./(2**(3+9./12))
    pitch_names = ['C', 'C#', 'D', 'D#', 'E', 'F',
                   'F#', 'G', 'G#', 'A', 'A#', 'B']
    pitch_indices = { b:a for a, b in zip(range(12), pitch_names)}
    freq = base*2**(pitch_indices[pitch]/12. + (octave-1))
    return int(round(freq))


def RunCodeAbbey():
    n_cases = int(raw_input())
    notes = raw_input().split()
    for note in notes:
        print frequency(note),


if __name__ == "__main__":
    print frequency('A4')
