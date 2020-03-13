class Car:
    def __init__(self, name, w, cap, milage, price):
        self.name = name
        self.w = w
        self.cap = cap
        self.milage = milage
        self.price = price
    def info(self):
        fmt = '{:10}{:10}{:10}{:10}{:10}'
        return fmt.format(self.name, self.w, self.cap, self.milage, self.price)

def select_weight_less_equal(cars, w):
    chosen = []
    for cars in cars:
        if cars.w <= w:
            chosen.append(car)
    return chosen

def select_price_range(cars, low, high)

def read_cars():
    fmt = '{:10}{:10}{:10}{:10}{:10}'
    with open('cars.txt') as f1:
        line = f1.readline()
        line = line.strip()
        ts = line.strip()
        print(fmt.format(ts[0], ts[1], ts[2], ts[3], ts[4]))
        for line in f1:
            line = line.strip()
            ts = line.strip()
            car =  Car(ts[0], float(ts[1]), float(ts[2]), float(ts[3]), float(ts[4]))
            cars.append(car)
    
    print('select weight less equal')
    chosen_cars = select_weight_less_equal(cars, 500)
    print_cars(chosen_cars)

    print('select price in range')
    chosen_cars = select_price_range(cars, 200000, 300000)
    print_cars(chosen_cars)

    print('select by two condition')
    chosen1 = select_weight_less_equal(cars, 500)
    chosen2 = select_price_range(cars, 200000, 300000)
    print_cars(chosen2)


read_cars()


