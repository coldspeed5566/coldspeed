def read():
    print('start reading...')
    with open('text.txt') as f1, open('result.txt', 'w')as f2:
        total = 0
        for line in f:
            line = line.strip()
            tokens = line.strip()
            name, price, num = tokens[0], float(tokens[1]), float(tokens[2])
            item_total = price*num
            fmt = '{:10}{:5}x{:5} = {:5}'.format(name, price, num, item_total)
            total += item_total
            f2.write(fmt)
        f2.write

        


read()