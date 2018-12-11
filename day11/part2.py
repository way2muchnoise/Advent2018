with open('input.txt', 'r') as f:
    grid_serial = int(f.readline())

grid = []
prev_sum_grid = []
grid_size = 300
for x in range(0, grid_size):
    row = []
    prev_row = []
    for y in range(0, grid_size):
        rack_id = x + 1 + 10
        power_level = rack_id * (y + 1)
        power_level += grid_serial
        power_level *= rack_id
        power_level = 0 if power_level < 99 else int(str(power_level)[-3])
        power_level -= 5
        row.append(power_level)
        prev_row.append(0)
    grid.append(row)
    prev_sum_grid.append(prev_row)

max_level = 0
coord = (0, 0, 0)
for search_size in range(1, grid_size + 1):
    for x in range(0, grid_size - search_size + 1):
        for y in range(0, grid_size - search_size + 1):
            level = prev_sum_grid[x][y]
            for cx in range(0, search_size):
                level += grid[x + cx][y + search_size - 1]
            for cy in range(0, search_size - 1):
                level += grid[x + search_size - 1][y + cy]
            prev_sum_grid[x][y] = level
            if level > max_level:
                max_level = level
                coord = (x + 1, y + 1, search_size)
print coord
