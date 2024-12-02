import re

class Levels:
    def __init__(self, levels):
        self.levels = levels

    def areIncreasing(self):
        return all(self.levels[i] < self.levels[i+1] for i in range(len(self.levels)-1))

    def areDecreasing(self):
        return all(self.levels[i] > self.levels[i+1] for i in range(len(self.levels)-1))

    def areStepsClose(self):
        if self.areIncreasing():
            for i in range(1, len(self.levels)):
                diff = self.levels[i] - self.levels[i-1]
                if diff < 1 or diff > 3:
                    return False
        else:
            for i in range(1, len(self.levels)):
                diff = self.levels[i-1] - self.levels[i]
                if diff < 1 or diff > 3:
                    return False

        return True

class Report:
    def __init__(self, report):
        self.report = report

    def safe(self):
      items = list(map(int, re.split(" ", self.report)))
      levels = Levels(items)
      return (levels.areIncreasing() or levels.areDecreasing()) and levels.areStepsClose()

class Reports:
    def __init__(self, reports):
        self.reports = reports

    def safe(self):
        sum = 0
        for item in self.reports:
            report = Report(item)

            if report.safe():
              sum += 1

        return sum


with open('input.txt') as f:
    lines = f.readlines()

    reports = Reports(lines)
    print(reports.safe())
