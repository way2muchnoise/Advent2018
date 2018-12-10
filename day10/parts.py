import re
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

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

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
plotted = plt.scatter(*zip(*stars))

ax_time_100 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_time_1 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_time_100 = Slider(ax_time_100, 'Time 100', 0, 200, valinit=1, valfmt='%0.0f')
slider_time_1 = Slider(ax_time_1, 'Time 1', 0, 100, valinit=1, valfmt='%0.0f')


def update(val):
    moved_stars = []
    t = round(slider_time_100.val) * 100 + round(slider_time_1.val)
    for x in range(0, len(stars)):
        star = stars[x]
        velocity = velocities[x]
        moved_stars.append((star[0] + velocity[0] * t, star[1] + velocity[1] * t))
    plotted.set_offsets(moved_stars)
    fig.canvas.draw_idle()


slider_time_100.on_changed(update)
slider_time_1.on_changed(update)

plt.show()
# Some manual work needed in the matplotlib window
