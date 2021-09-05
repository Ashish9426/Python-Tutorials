class Engine:
    def __init__(self, name):
        self.__name = name

    def print_info(self):
        print(f"-- engine info --")
        print(f"engine name = {self.__name}")


class Car:
    def __init__(self, model, engine_name):
        self.__model = model
        self.__engine = Engine(engine_name)

    def print_info(self):
        print("-- car info --")
        print(f"model = {self.__model}")
        self.__engine.print_info()


car = Car('i20', 'V6 Turbo')
car.print_info()
