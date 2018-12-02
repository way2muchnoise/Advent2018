frequency = 0
frequencies = set()
with open('input.txt', 'r') as f:
    line = f.readline()
    while frequency not in frequencies:
        frequencies.add(frequency)
        frequency += int(line)
        line = f.readline()
        if not line:
            f.seek(0)
            line = f.readline()
print frequency
