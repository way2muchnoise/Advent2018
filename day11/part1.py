with open('input.txt', 'r') as f:
    grid_serial = int(f.readline())

grid = []
grid_size = 300
for x in range(0, grid_size):
    row = []
    for y in range(0, grid_size):
        rack_id = x + 1 + 10
        power_level = rack_id * (y + 1)
        power_level += grid_serial
        power_level *= rack_id
        power_level = 0 if power_level < 99 else int(str(power_level)[-3])
        power_level -= 5
        row.append(power_level)
    grid.append(row)

max_level = 0
coord = (0, 0)
for x in range(0, grid_size - 2):
    for y in range(0, grid_size - 2):
        level = grid[x + 0][y] + grid[x + 0][y + 1] + grid[x + 0][y + 2] + \
                grid[x + 1][y] + grid[x + 1][y + 1] + grid[x + 1][y + 2] + \
                grid[x + 2][y] + grid[x + 2][y + 1] + grid[x + 2][y + 2]
        if level > max_level:
            max_level = level
            coord = (x + 1, y + 1)
print coord
