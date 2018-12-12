state_changes = {}
with open('input.txt', 'r') as f:
    initial_state = f.readline().replace('\n', '').split(' ')[-1]
    f.readline()
    line = f.readline()
    while line:
        k, v = line.replace('\n', '').split(' => ')
        state_changes[k] = v
        line = f.readline()

current_state = initial_state[:]
start_index = 0
gen = 0
fifty_billion = 50000000000
while gen < fifty_billion:
    if current_state[0:4] != '....':
        current_state = '....' + current_state
        start_index -= 4
    if current_state[-4:] != '....':
        current_state += '....'
    new_state = list(current_state)
    for char in range(2, len(current_state) - 3):
        new_state[char] = state_changes[current_state[char - 2:char + 3]]
    new_state = ''.join(new_state)
    if new_state.strip('.') in current_state:
        start_index += fifty_billion - gen - 1
        gen = fifty_billion
    current_state = new_state
    gen += 1

plant_sum = 0
for char_index in range(0, len(current_state)):
    if current_state[char_index] == '#':
        plant_sum += start_index + char_index
print plant_sum
