print('guess number')

import random
def guess():
    num = 0
    x = random.randint(0, 100)
    print('you have 5 chance to guess the number')
    #print('answer:'x)
    while 1 > 0:
        while num < 5:
            try:
                a = int(input())
                if a > x:
                    print('too large, guess something smaller')
                elif a < x:
                    print('too small, guess something bigger')
                elif a == x:
                    print('comgragulation, you are right')
                    break
                num += 1
            except:
                print('wrong input, please try again')
        print('you loose')
    print('Do you want to try again?(yes)')
    b = input()
    if b = yes:
        print()
    else:
        break

guess()