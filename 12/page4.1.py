class Car:
    """
    Car class having members
    - model, company, price
    - print_info, is_affordable
    - access specifier
      - public members
        - member having name without any under score (_)
        - can be accessed outside of the class
        - e.g. self.model, self.company, self.price
      - private or protected members
        - member having name with double underscores (__)
        - can be accessed only within the same class
        - can not be accessed outside of the class
        - e.g. self.__model, self.__company, self.__price
    """
    def __init__(self, model, company, price=0):
        self.__model = model
        self.__company = company
        self.__price = price

    # getters or inspectors
    def get_price(self):
        return self.__price

    def get_model(self):
        return self.__model

    def get_company(self):
        return self.__company

    # setters or mutators
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("invalid price")

    def set_company(self, company):
        self.__company = company

    def set_model(self, model):
        self.__model = model

    # facilitator / utility
    def print_info(self):
        print(f"model: {self.__model}")
        print(f"company: {self.__company}")
        print(f"price: INR {self.__price} L")

    # facilitator / utility
    def is_affordable(self):
        if self.__price > 10:
            print(f"{self.__model} is not affordable")
        else:
            print(f"{self.__model} is affordable")

x5 = Car('X5', 'BMW')
x5.print_info()
x5.set_price(39.5)
# x5.print_info()
print(f"price = {x5.get_price()}")
print(f"model = {x5.get_model()}")
print(f"company = {x5.get_company()}")
