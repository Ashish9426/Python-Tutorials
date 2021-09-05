# import a module
import page1
import car

print(f"page2 module name: {__name__}")

# create an object of a class defined in page1
person2 = page1.Person('person2', 30)
person2.print_info()

print('-' * 80)

# create an object of a class defined in car
car1 = car.Car('i10', 'hyundai', 5.5)
car1.print_info()
