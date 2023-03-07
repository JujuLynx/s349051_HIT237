class Food():
    def __init__(self, desc, price):
        self.description = desc
        try:
            price = float(price)
        except:
            self.cost = 0.0
        else:
            self.cost = price
    def get_details(self):
        return str('The %s will cost %.2f.' % (self.description, self.cost))

class Pizza(Food):
    def __init__(self, desc, price, toppings):
        super().__init__(desc, price)
        self.toppings = toppings
    def get_details(self):
        return str('This %s pizza has the following toppings: %s' % (self.description, self.toppings))

myPizza = Pizza("Hawaiian", 4.95, "Ham, Pineapple")
print(myPizza.get_details())