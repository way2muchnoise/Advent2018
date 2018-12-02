with open('input.txt', 'r') as f:
    lines = f.readlines()

for x in range(0, len(lines) - 1):
    line_x = lines[x]
    for y in range(x + 1, len(lines)):
        line_y = lines[y]
        diffs = 0
        for c in range(0, len(line_x)):
            if line_x[c] is not line_y[c]:
                diffs += 1
                if diffs > 1:
                    break
        if diffs == 1:
            common = ''
            for c in range(0, len(line_x)):
                if line_x[c] is line_y[c]:
                    common += line_x[c]
            print common
            exit(0)
