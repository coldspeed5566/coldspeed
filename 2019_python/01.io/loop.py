def prNum(n):
  for i in range(0, n+1):
    print(i, end = ' ')
  print("")
#prNum(5)

def pr_Range(a, b):
  for i in range(a, b):
    print(i, end = ' ')
  print()
#pr_Range(10, 20)

def pr_odd1(n):
  x = 1
  for i in range(n):
    print(x, end = " ")
       x += 2
    print()
#pr_odd1(5)

def pr_odd2(n):
  for i in range(n):
    print(i*2+1, end=' ')
  print()
#pr_odd2(5)

def rect_for( m, n, ch):
  for i in range(m):
    for i in range(n):
      print(ch, end = ' ')
    print()
#rect_for(3, 5, '$')
        
 def rect_while( m, n, ch):
   j = 0
   while j < n:
     print(ch)
     while j < n:
        print(ch, end = " ")
        j += 1
     print()
     i += 1
#rect_while(3, 5, '$')   

def frame(m, n, ch= "*")
    for i in range(n):    
      print(ch, end=' ')
    print()

    print(ch, end=" ")
    for i in range(n-2): 
        print(' ', end=' ')
    print(ch)
frame(5, 6, '#')
frame(7, 15, '@')

def square_number(n):
  i = 1
  while i > n:
    print(i, end= ' ')
    i += 1
    print()
square_number(25)

def pr_digits(n):
  while n > 100:
    print(n % 10)
    n = n / 10

pr_digits(5764)
pr_digits(123456)

def rect_str(m, n, ch):
  for i in range(m):
    print((ch+' ') * n)    
#rest_str(3, 5 ,'$')



