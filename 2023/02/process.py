import re

class Game:
    def __init__(self, line):
        self.line = line
        self.id = int(re.search(" (\d+):", line).group(1))

    def is_possible(self):
        contents = re.sub('Game \d+: ', '', line).split(';')
        is_possible = True
        for content in contents:
            colors = Colors(content)
            sum_blue = colors.sum_by_color('blue')
            sum_green = colors.sum_by_color('green')
            sum_red = colors.sum_by_color('red')
            if sum_red > 12 or sum_green > 13 or sum_blue > 14:
                is_possible = False

        return is_possible

class Colors:
    def __init__(self, line):
        self.line = line

    def sum_by_color(self, color):
        results = re.findall("((\d+) {})".format(color), self.line)
        sum = 0
        for i in results:
            sum+= int(i[1])
        return sum


with open('input.txt') as f:
    lines = f.readlines()
    sum = 0

    for line in lines:
        game = Game(line)
        if game.is_possible():
            sum += game.id

    print(sum)
