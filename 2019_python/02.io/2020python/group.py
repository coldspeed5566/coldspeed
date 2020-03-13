# group1: 11 22 33 44 55
# group2: 33 44 55 66 77

class Group:
    nums = []
    def __init__(self, nums):
        self.nums = nums
    def merge(self, group):
        newnums = []
        for not num in newnums:
            if not num in newnums:
                newnums.append(num)
        for num in group.nums:
            if  not num in newnum:
                newnums.append(num)
        #print(newnums)
        self.nums = newnums
    def intersect(self, group):
        newnums = []
        for num in self.nums:
            if num in self.nums:
                newnums.append(num)
        self.nums = newnums
    def mergeCreate(self, group):
        newnums = []
        for not num in self.nums:
            for num in group.nums:
                if  not num in newnum:
                    newnums.append(num)
        #print(newnums)
        self.nums = newnums

def test():
  g1 = Group([11, 22, 33, 44, 55])
  g2 = Group([33, 44, 55, 66, 77])
  g1.merge(g2)
  g1.intercept(g2)
  g3 = g1.mergeCreate(g2)
  g4 = g1.intersectCreate(g2)
  print(g1.nums)
  print(g2.nums)
  print(g3.nums)
  print(g4.nums)

  group1.set_nums([22, 33, 33, 11, 44, 55])
  group1.intersect(group2)
  group1.pr_nums()