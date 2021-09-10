class Car:
    """
    Car class having members
    - model, company, price
    - print_info, is_affordable
    """
    def __init__(self, model, company, price=0):
        self.model = model
        self.company = company
        self.price = price

    # facilitator / utility
    def print_info(self):
        print(f"model: {self.model}")
        print(f"company: {self.company}")
        print(f"price: {self.price}L")

    # facilitator / utility
    def is_affordable(self):
        if self.price > 10:
            print(f"{self.model} is not affordable")
        else:
            print(f"{self.model} is affordable")

#i20 = Car() -> # Error: TypeError: __init__() missing 3 required positional arguments: 'model', 'company', and 'price'

#i20 = Car('i20', 'hyundai', 7.5)
#i20.print_info()
#i20.is_affordable()

x5 = Car('X5', 'BMW')
x5.print_info()

print("enter model: ")
model = input()

print("enter company: ")
company = input()

print("enter price: ")
price = float(input())

car = Car(model, company, price)
car.print_info()
car.is_affordable()


