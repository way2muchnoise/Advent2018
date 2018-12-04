import re
from datetime import datetime
from collections import Counter

working_guard = ''
sleep_start = None
minutes = []
guards = {}
actions = {}
line_regex = re.compile(r'\[(.*)\] (.*)')

for x in range(0, 60):
    minutes.append([])

with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        m = line_regex.match(line)
        current_datetime = datetime.strptime(m.group(1), "%Y-%m-%d %H:%M")
        actions[current_datetime] = m.group(2)
        line = f.readline()

for t in sorted(actions.keys()):
    action = actions[t]
    if action.startswith("Guard"):
        working_guard = action.split(" ")[1][1:]
        if working_guard not in guards.keys():
            guards[working_guard] = 0
    elif action.startswith("falls asleep"):
        sleep_start = t
    elif action.startswith("wakes up"):
        for x in range(sleep_start.minute, t.minute):
            minutes[x].append(int(working_guard))
            guards[working_guard] += 1

top_times_asleep = 0
sleepy_guard = -1
minute_asleep = 0
for minute in range(0, 60):
    most_common = Counter(minutes[minute]).most_common(1)
    if len(most_common) > 0:
        (guard_asleep, current_times_asleep) = most_common[0]
        if current_times_asleep > top_times_asleep:
            top_times_asleep = current_times_asleep
            sleepy_guard = guard_asleep
            minute_asleep = minute
mul = int(sleepy_guard) * minute_asleep
print mul
