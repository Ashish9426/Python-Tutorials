class Car:
    pass

def print_info(car):
    print(f"model = {car.model}")
    print(f"company = {car.company}")

c1 = Car()

# adding attributes
c1.model = 'i20'
c1.company = 'hyundai'
c1.print_info = print_info

c1.print_info(c1)
print_info(20)

