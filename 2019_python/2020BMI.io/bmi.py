def computerBMI(h,w):
    h = h/100
    return w / (h ** 2)

def getMEMO(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi < 22.9:
        return 'normal'
    elif bmi < 30:
    
    elif bmi


def table():
    with open('bmi.txt') as f:
        first = f.readline()
        hs = first.split()
        fmt = '{:10}{:10}{:10}{:10}{:10}{:10}'
        print(fmt.format(hs[0], hs[1], hs[2], hs[3], 'BMI', 'MEMO'))
        print('-' * 60)
        for line in f:
            tsk = line.strip().split()
            name, gender, h, w = tsk[0], tsk[1], float(tsk[2]), float(tsk[3])
            bmi = round(computerBMI(h, w))
            memo = getMEMO(bmi)
            print(fmt.format(name, gender, h, w,))
            #print(type(name), type(gender), type(h), type(w))

table()