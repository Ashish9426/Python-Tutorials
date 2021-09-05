class Vehicle:
    def __init__(self, model, company, price):
        self._model = model
        self._price = price
        self._company = company

    def print_info(self):
        print(f"model: {self._model}")
        print(f"company: {self._company}")
        print(f"price: {self._price}")


class Bike(Vehicle):
    def __init__(self, model, company, price):
        Vehicle.__init__(self, model, company, price)

    # overriding the print_info method
    def print_info(self):
        print(f"-- bike information --")
        Vehicle.print_info(self)


class Car(Vehicle):
    def __init__(self, model, company, price, fuel_type):
        Vehicle.__init__(self, model, company, price)
        self._fuel_type = fuel_type

    # overriding the print_info method
    def print_info(self):
        print(f"-- car information --")
        Vehicle.print_info(self)
        print(f"fuel: {self._fuel_type}")


b1 = Bike('activa', 'honda', 75000)
b1.print_info()

c1 = Car('i20', 'hyundai', 750000, 'petrol')
c1.print_info()
