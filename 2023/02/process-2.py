import re

class Game:
    def __init__(self, line):
        self.line = line
        self.id = int(re.search(" (\d+):", line).group(1))

    def power(self):
        colors = Colors(line)
        max_blue = colors.max_by_color('blue')
        max_green = colors.max_by_color('green')
        max_red = colors.max_by_color('red')
        return max_blue * max_green * max_red

class Colors:
    def __init__(self, line):
        self.line = line

    def max_by_color(self, color):
        results = re.findall("((\d+) {})".format(color), self.line)
        results = [int(i[1]) for i in results]
        return max(results)


with open('input.txt') as f:
    lines = f.readlines()
    sum = 0

    for line in lines:
        game = Game(line)
        sum += game.power()

    print(sum)
