import re

class Locations:
    def __init__(self, lines):
        self.lines = lines
        self.left = []
        self.right = []

        for line in self.lines:
            points = re.split("   ", line)
            self.left.append(int(points[0]))
            self.right.append(int(points[1]))

    def similarity(self):
        sum = 0
        for item in self.left:
            sum += item * self.right.count(item)

        return sum


with open('input.txt') as f:
    lines = f.readlines()

    locations = Locations(lines)
    print(locations.similarity())
