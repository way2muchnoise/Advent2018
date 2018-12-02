from collections import Counter

two = 0
three = 0
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        counts = Counter(line)
        if 2 in counts.values():
            two += 1
        if 3 in counts.values():
            three += 1
        line = f.readline()
checksum = two * three
print checksum
