import re

setup_pattern = re.compile(r'(\d+) players; last marble is worth (\d+) points')


class Marble:
    def __init__(self, number):
        self.number = number
        self.cw = None
        self.ccw = None

    def get_cw(self, count):
        marble = self
        for c in range(0, count):
            marble = marble.cw
        return marble

    def get_ccw(self, count):
        marble = self
        for c in range(0, count):
            marble = marble.ccw
        return marble


with open('input.txt') as f:
    line = f.readline()
    player_count, last_marble = map(int, setup_pattern.match(line).group(1, 2))

players = []
for x in range(0, player_count):
    players.append(0)

current_marble = Marble(0)
current_marble.cw = current_marble
current_marble.ccw = current_marble

last_marble *= 100

current_player = 0
for marble_number in range(1, last_marble + 1):
    if marble_number % 23 == 0:
        players[current_player] += marble_number
        to_remove = current_marble.get_ccw(7)
        to_remove.cw.ccw = to_remove.ccw
        to_remove.ccw.cw = to_remove.cw
        players[current_player] += to_remove.number
        current_marble = to_remove.cw
    else:
        new_marble = Marble(marble_number)
        current_marble_cw_1 = current_marble.get_cw(1)
        current_marble_cw_2 = current_marble.get_cw(2)
        new_marble.ccw = current_marble_cw_1
        new_marble.cw = current_marble_cw_2
        current_marble_cw_1.cw = new_marble
        current_marble_cw_2.ccw = new_marble
        current_marble = new_marble
    current_player = (current_player + 1) % player_count

print max(players)
