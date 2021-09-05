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
    def __init__(self, model, company, price):
        self.__model = model
        self.__company = company
        self.__price = price

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

i10 = Car('i10', 'hyundai', 5.5)
print(i10.__dict__)
i10.price = 50.5
i10.model = 'Invalid Model'
i10.company = 'Invalid Company'

# not working
# i10.price = 6.5

# not working
# i10.__price = 6.5

# not recommended
# i10._Car__price = 6.5

# i10.__model = 'invalid data'
# i10.__company = 'invalid company'
# i10._Car__model = 'invalid data'
# i10._Car__company = 'invalid company'





i10.print_info()
i10.is_affordable()