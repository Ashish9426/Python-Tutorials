class Car:
    def __init__(self, model, company, price):
        self.__model = model
        self.__company = company
        self.__price = price

    def print_info(self):
        print(f"model = {self.__model}")
        print(f"company = {self.__company}")
        print(f"price = {self.__price}")


if __name__ == '__main__':
    car = Car('i20', 'hyundai', 7.5)
    car.print_info()
