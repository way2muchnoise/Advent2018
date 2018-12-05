def is_opposite(a, b):
    return a == b.swapcase() and b == a.swapcase()


with open('input.txt', 'r') as f:
    chars = f.read(1)
    next_char = f.read(1)
    while next_char:
        if len(chars) > 0 and is_opposite(chars[-1], next_char):
            chars = chars[:-1]
        else:
            chars += next_char
        next_char = f.read(1)
print len(chars)
