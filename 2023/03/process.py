import re

class Line:
    def __init__(self, line, index, lines):
        self.line = line
        self.index = index
        self.lines = lines

    def value (self):
        print(line)
        sum = 0
        for match in re.finditer('(\d+)', line, re.S):
            value = Value(lines, index, match.group(1), match.start(), match.end())
            if value.isvalid():
                sum += value.value

        return sum

class Value:
    def __init__(self, lines, lineindex, value, start, end):
        self.lines = lines
        self.lineindex = lineindex
        self.value = int(value)
        self.start = start
        self.end = end

    def checkvalue(self, index, column):
        val = self.lines[index][column]
        if val != '.' and val != '\n' and not val.isdigit():
            print(val, self.value)
            return True

        return False


    def isvalid(self):
        for i in range(-1, 2):
            index = self.lineindex + i
            if index < 0 or index >= len(self.lines):
                continue

            if self.start > 0:
                if self.checkvalue(index, self.start - 1):
                    return True

            for i in range(self.start, self.end):
                if self.checkvalue(index, i):
                    return True

            if self.end < len(self.lines[index]):
                if self.checkvalue(index, self.end):
                    return True

        return False

with open('input.txt') as f:
    lines = f.readlines()
    sum = 0

    for index, line in enumerate(lines):
        pipe = Line(line, index, lines)
        sum += pipe.value()
        print('sum', sum)

    print(sum)
