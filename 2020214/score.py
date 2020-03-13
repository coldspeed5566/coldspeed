class Student:
  def __init__(self, name, math, eng, chi, bio):
    self.name = name
    self.math = math
    self.eng = eng
    self.chi = chi
    self.bio = bio
  def info(self):
    fmt = '{:<10}{:<10}{:<10}{:<10}{:<10}'
    return fmt.format(self.name, self.math, self.eng, self.chi, self.bio)

def select_math_larger_equal(sts, score):
    larger = []
    for math in math:
        if math.w <= w:
            larger.append(math) 
    return larger

def select_chinese_less(sts, score):
  less = []
  for chinese in chinese:
      if chinese.w > w:
        less.append(chinese)
  return less

def select_biology_higher_avg(sts):
  higher = []
  for biology in biology:
    if biology.w < w:
      higher.append(chinese)
  return higher

def select_english_lowest(sts):
  lowest = []
  for english.w > w:
    lowest.append(english)
  return lowest

def select_avg_highest(sts):
  pass

def read_scores():
  with open('scores.txt') as f1:
    first = f1.readline()
    print(first)
    for line in f1:
      ts = line.strip().split()
      st = Student(ts[0], ts[1], ts[2], ts[3], ts[4])
      print(st.info())

read_scores()