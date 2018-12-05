import string
import StringIO


def is_opposite(a, b):
    return a == b.swapcase() and b == a.swapcase()


def react(f):
    chars = f.read(1)
    next_char = f.read(1)
    while next_char:
        if len(chars) > 0 and is_opposite(chars[-1], next_char):
            chars = chars[:-1]
        else:
            chars += next_char
        next_char = f.read(1)
    return chars


with open('input.txt', 'r') as f:
    chars = react(f)

reductions = []
for letter in string.ascii_lowercase:
    reduction = chars.replace(letter, '').replace(letter.upper(), '')
    f = StringIO.StringIO(reduction)
    reduction = react(f)
    reductions.append(len(reduction))
    f.close()
    print letter, len(reduction)
print "minimum", min(reductions)
