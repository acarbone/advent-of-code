import re

def line_value(line):
    line = line.replace("\n", "")
    digits = re.sub("[^0-9]", "", line)
    if len(digits) == 0:
        return 0

    if len(digits) == 1:
        return int(digits[0] + digits[0])

    return int(digits[0] + digits[-1])

with open('input.txt') as f:
    lines = f.readlines()
    sum = 0

    for line in lines:
      sum += line_value(line)

    print(sum)
