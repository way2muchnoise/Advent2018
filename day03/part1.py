import re

patches = {}
patch_pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')


def get_patch_name(x, y):
    return repr(x) + "," + repr(y)


def claim_patch(id, x, y, width, height):
    for w in range(0, width):
        for h in range(0, height):
            patch_name = get_patch_name(x + w, y + h)
            if patch_name not in patches:
                patches[patch_name] = [id]
            else:
                patches[patch_name].append(id)


with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        m = patch_pattern.match(line)
        claim_patch(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
        line = f.readline()
overlap_count = 0
for value in patches.values():
    if len(value) > 1:
        overlap_count += 1
print overlap_count
