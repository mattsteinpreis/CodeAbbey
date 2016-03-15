__author__ = 'matt'


def encode_message(message, encoding):
    codes = [encoding[ch] for ch in message]
    code_string = ''.join(codes)
    code_string += '0'*(8 - len(code_string) % 8)
    pointer = 0
    encoded = []
    for i in range(len(code_string) / 8):
        byte = code_string[pointer:(pointer+8)]
        dec_byte = int(byte, 2)
        pretty_hex = "{0:0{1}x}".format(dec_byte, 2)
        encoded.append(pretty_hex.upper())
        pointer += 8
    return encoded

my_encoding = { ' ': '11',       'e': '101',
                't': '1001',     'o': '10001',
                'n': '10000',    'a': '011',
                's': '0101',     'i': '01001',
                'r': '01000',    'h': '0011',
                'd': '00101',    'l': '001001',
                '!': '001000',   'u': '00011',
                'c': '000101',   'f': '000100',
                'm': '000011',   'p': '0000101',
                'g': '0000100',  'w': '0000011',
                'b': '0000010',  'y': '0000001',
                'v': '00000001', 'j': '000000001',
                'k': '0000000001',   'x': '00000000001',
                'q': '000000000001', 'z': '000000000000'}

string_to_encode = raw_input()
#string_to_encode = "entertaining interpreter"
encoded_message = encode_message(string_to_encode, my_encoding)
for word in encoded_message:
    print word,