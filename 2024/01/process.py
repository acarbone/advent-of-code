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

    def distance(self):
        self.left.sort()
        self.right.sort()

        sum = 0
        for i in range(len(self.left)):
            sum += abs(self.left[i] - self.right[i])

        return sum


with open('input.txt') as f:
    lines = f.readlines()
    sum = 0

    locations = Locations(lines)
    print(locations.distance())
