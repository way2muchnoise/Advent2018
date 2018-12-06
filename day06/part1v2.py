import operator
from collections import Counter

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
        new.append(min(map(lambda coord: (coords_to_plot_index[coord], man_dist(x, y, coord[0], coord[1])), coords), key=operator.itemgetter(1)))
    matrix.append(new)

to_remove = set()
to_remove.add(None)
for x in range(min_x, max_x + 1):
    to_remove.add(matrix[x - min_x][min_y - min_y][0])
    to_remove.add(matrix[x - min_x][max_y - min_y][0])
for y in range(min_y, max_y + 1):
    to_remove.add(matrix[min_x - min_x][y - min_y][0])
    to_remove.add(matrix[max_x - min_x][y - min_y][0])

occurrence = []
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        if matrix[x - min_x][y - min_y]:
            occurrence.append(matrix[x - min_x][y - min_y][0])

counted = Counter(occurrence)
for remove in to_remove:
    del counted[remove]

print counted.most_common(1)[0]
