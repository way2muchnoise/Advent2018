frequency = 0
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        frequency += int(line)
        line = f.readline()
print frequency
