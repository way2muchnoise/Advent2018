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


def get_patches(x, y, width, height):
    current_patches = []
    for w in range(0, width):
        for h in range(0, height):
            current_patches.append(patches[get_patch_name(x + w, y + h)])
    return current_patches


with open('input.txt', 'r') as f:
    line = f.readline()
    while line:
        m = patch_pattern.match(line)
        claim_patch(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
        line = f.readline()
    f.seek(0)
    line = f.readline()
    while line:
        m = patch_pattern.match(line)
        line_patches = get_patches(int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
        good = True
        for line_patch in line_patches:
            good &= len(line_patch) is 1
        if good:
            print m.group(1)
            break
        line = f.readline()
