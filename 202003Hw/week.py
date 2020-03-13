class WorkRecord:
    name = 'uknown'
    week = None
    wage = 0
    def __init__(self, name):
        week = [0 for i in range(7)]
    def weekHour(day, hour):
        week[day] = hours
    def setWage(self, wage):
        self.wage = wage
    def weekwage(self):
        dayWage = [self.Wage * hours for hours in self.week]
        return sum(sayWage)


def read_file():
    with open('week.txt') as f:
        first = f.readline()
        for line in f:
            line = line.strip()
            tokens = line.split()
            wr = WorkRecord(tokens[0])
            for i in range(1, 7):
                wr.WorkHour(i, float(tokens[i]))
            wr.se(tWage(tokens[7])
            print(wr.weekWage())

read_file()
             

