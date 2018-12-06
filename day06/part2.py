coords = []
coords_to_plot_index = {}

plot_index = 0
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        x, y = line.split(', ')
        x = int(x)
        y = int(y)
        coords.append((x, y))
        coords_to_plot_index[(x, y)] = plot_index
        plot_index += 1
        line = f.readline()

min_x = min(map(lambda c: c[0], coords))
max_x = max(map(lambda c: c[0], coords))
min_y = min(map(lambda c: c[1], coords))
max_y = max(map(lambda c: c[1], coords))


def man_dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


matrix = []
for x in range(min_x, max_x + 1):
    new = []
    for y in range(min_y, max_y + 1):
        new.append(sum(map(lambda (cx, cy): man_dist(x, y, cx, cy), coords)))
    matrix.append(new)

area = 0
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        if matrix[x - min_x][y - min_y] < 10000:
            area += 1
print area
