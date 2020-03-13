def ticket(age):
  if age<15:
    print("CHILDREN")
  elif age<64:
    print("SENIOR")
  else:
    print("ADULT")
  
  
def test():
  ticket(10)
  ticket(15)
  ticket(20)
  ticket(65)
  ticket(80)
  
test()