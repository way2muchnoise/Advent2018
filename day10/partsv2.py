import re

star_pattern = re.compile(r'position=<(.*)> velocity=<(.*)>')

stars = []
velocities = []
with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        star, velocity = star_pattern.match(line).group(1, 2)
        star = star.replace(' ', '').split(',')
        velocity = velocity.replace(' ', '').split(',')
        stars.append((int(star[0]), int(star[1])))
        velocities.append((int(velocity[0]), int(velocity[1])))
        line = f.readline()


def get_area(stars):
    x, y = zip(*stars)
    x_size = max(x) - min(x)
    y_size = max(y) - min(y)
    return x_size * y_size


min_area = get_area(stars)
t = 0
is_smaller = True
while is_smaller:
    is_smaller = False
    t += 1
    moved_stars = []
    for x in range(0, len(stars)):
        star = stars[x]
        velocity = velocities[x]
        moved_stars.append((star[0] + velocity[0] * t, star[1] + velocity[1] * t))
    area = get_area(moved_stars)
    if area <= min_area:
        min_area = area
        is_smaller = True

t -= 1
for x in range(0, len(stars)):
    star = stars[x]
    velocity = velocities[x]
    stars[x] = (star[0] + velocity[0] * t, star[1] + velocity[1] * t)

x, y = zip(*stars)
min_x = min(x)
max_x = max(x)
min_y = min(y)
max_y = max(y)

print_array = []
for y in range(min_y, max_y + 1):
    to_add = []
    for x in range(min_x, max_x + 1):
        to_add.append(' ')
    print_array.append(to_add)

for star in stars:
    print_array[star[1] - min_y][star[0] - min_x] = '#'

for row in print_array:
    print ''.join(row)

print t
