class TreeNode:
    def __init__(self):
        self.children = []
        self.metadata = []


def next_number(f):
    number = ''
    next_char = f.read(1)
    while next_char and next_char != ' ':
        number += next_char
        next_char = f.read(1)
    return int(number) if len(number) else None


def read_node(f):
    child_count = next_number(f)
    meta_entries = next_number(f)
    current_node = TreeNode()
    for x in range(0, child_count):
        current_node.children.append(read_node(f))
    for x in range(0, meta_entries):
        current_node.metadata.append(next_number(f))
    return current_node


with open('input.txt') as f:
    root = read_node(f)
nodes = [root]
root_sum = 0
while len(nodes):
    node = nodes.pop()
    if len(node.children) == 0:
        root_sum += sum(node.metadata)
    else:
        for meta in node.metadata:
            child_index = meta - 1
            if meta != 0 and child_index < len(node.children):
                nodes.append(node.children[child_index])
print root_sum
