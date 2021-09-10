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
        print(f"price: INR {self.price} L")

    # facilitator / utility
    def is_affordable(self):
        if self.price > 10:
            print(f"{self.model} is not affordable")
        else:
            print(f"{self.model} is affordable")

i10 = Car('i10', 'hyundai', 5.5)
print(i10.__dict__)
i10.price = 50.5
i10.model = 'Invalid Model'
i10.company = 'Invalid Company'
i10.print_info()
i10.is_affordable()