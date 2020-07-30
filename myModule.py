def greetings(name):
    print("hello", name)


person1 = {
    "name": 'tauhid',
    "Age": 23,
    "Nationality": "Bangladesh"
}
class car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def print_car(self):
        print(self.brand, self.price)

c1 = car("BMW", 13300)

c1.print_car()