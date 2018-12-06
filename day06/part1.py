from Queue import Queue
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

matrix = []
for x in range(min_x, max_x + 1):
    new = []
    for y in range(min_y, max_y + 1):
        new.append(None)
    matrix.append(new)

edges = Queue()
for coord in coords:
    matrix[coord[0] - min_x][coord[1] - min_y] = (coords_to_plot_index[coord], 0)
    edges.put(coord)


def try_put_in_matrix(x, y, i, d):
    global matrix
    global edges
    current = matrix[x - min_x][y - min_y]
    if not current or current[1] > d:
        matrix[x - min_x][y - min_y] = (i, d)
        edges.put((x, y))
    elif current and current[1] == d and not current[0] == i:
        matrix[x - min_x][y - min_y] = (None, d)


while not edges.empty():
    (x, y) = edges.get()
    (ni, nd) = matrix[x - min_x][y - min_y]
    if ni is None:
        continue
    if x - 1 >= min_x:
        try_put_in_matrix(x - 1, y, ni, nd + 1)
    if x + 1 <= max_x:
        try_put_in_matrix(x + 1, y, ni, nd + 1)
    if y - 1 >= min_y:
        try_put_in_matrix(x, y - 1, ni, nd + 1)
    if y + 1 <= max_x:
        try_put_in_matrix(x, y + 1, ni, nd + 1)

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
