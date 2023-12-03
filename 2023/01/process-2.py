import re

def line_value(line):
    print(line.replace("\n", ""))
    line = line.replace("\n", "")

    #.replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9')

    left_index = 0
    right_index = 0
    mo = re.search(r'\d+', line)
    if mo:
        left_index = mo.start()

    mo = re.match('.+([0-9])[^0-9]*$', line)
    if mo:
        right_index = mo.start(1)

    indexes = {}
    for i in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
        found = line.find(i)
        if found > -1:
            indexes[i] = found
    #print(indexes)

    if len(indexes) > 0:
        min_char_position = min(indexes.values())
        res_min = [key for key in indexes if indexes[key] == min_char_position]

        max_char_position = max(indexes.values())
        res_max = [key for key in indexes if indexes[key] == max_char_position]
        print(, indexes[res_max[0]])
        if indexes[res_min[0]] < left_index:
            line = line.replace(res_min[0], )
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
      value = line_value(line)
      print(value)
      sum += value

    print(sum)
