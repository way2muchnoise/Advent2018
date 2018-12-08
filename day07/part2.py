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


class Worker:
    def __init__(self):
        self.remaining = 0
        self.doing = None

    def start_working(self, letter):
        self.remaining = 60 + ord(letter) - ord('A') + 1
        self.doing = letter

    def work(self, timing):
        self.remaining -= timing
        if self.remaining <= 0:
            self.remaining = 0
            return True
        return False


order = []
workers = []
for x in range(0, 5):
    workers.append(Worker())
time = 0


def do_work():
    global time, workers, nodes
    next_ready = min(filter(lambda w: w.doing is not None, workers), key=lambda w: w.remaining)
    timing = next_ready.remaining
    for worker in workers:
        if worker.work(timing):
            for node in nodes.values():
                if worker.doing in node:
                    node.remove(worker.doing)
            worker.doing = None
    time += timing
    return next_ready


while len(letters):
    next_letters = sorted(filter(lambda letter: len(nodes[letter]) == 0, letters))
    if len(next_letters) > 0:
        next_letter = next_letters[0]
        order.append(next_letter)
        letters.remove(next_letter)
        free_workers = filter(lambda w: w.remaining == 0, workers)
        if len(free_workers) == 0:
            free_workers.append(do_work())
        free_worker = free_workers[0]
        free_worker.start_working(next_letter)
    else:
        do_work()
while len(filter(lambda w: w.remaining > 0, workers)):
    do_work()
print ''.join(order)
print time

