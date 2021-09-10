class Car:
    """
    Car class having members
    - model, company, price
    - print_info, is_affordable
    """
    def __init__(self):
        self.model = ''
        self.company = ''
        self.price = 0

    def __init__(self, model, company, price):
        self.model = model
        self.company = company
        self.price = price

    # facilitator / utility
    def print_info(self):
        print(f"model: {self.model}")
        print(f"company: {self.company}")
        print(f"price: {self.price}")

    # facilitator / utility
    def is_affordable(self):
        if self.price > 10:
            print(f"{self.model} is affordable")
        else:
            print(f"{self.model} is not affordable")

# creation
car1 = Car()

# initialization
car1.model = 'i20'
car1.company = 'hyundai'
car1.price = 7.5

# consume
car1.print_info()
car1.is_affordable()

# Error : TypeError: __init__() missing 3 required positional arguments: 'model', 'company', and 'price'