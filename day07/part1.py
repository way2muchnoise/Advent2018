nodes = {}
letters = set()
with open('input.txt') as f:
    line = f.readline()
    while line:
        splitted = line.split(" ")
        letter_before = splitted[1]
        letter_after = splitted[7]
        if letter_before not in nodes:
            nodes[letter_before] = []
            letters.add(letter_before)
        if letter_after not in nodes:
            nodes[letter_after] = []
            letters.add(letter_after)
        nodes[letter_after].append(letter_before)
        line = f.readline()

order = []
while len(letters):
    next_free = sorted(filter(lambda letter: len(nodes[letter]) == 0, letters))[0]
    order.append(next_free)
    for node in nodes.values():
        if next_free in node:
            node.remove(next_free)
    letters.remove(next_free)
print ''.join(order)
