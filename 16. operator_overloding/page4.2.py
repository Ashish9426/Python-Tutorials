def divide(n1, n2):
    division = n1 / n2
    print(f"division = {division}")


def add(n1, n2):
    addition = n1 + n2
    print(f"addition = {addition}")


def read_file():
    file = open("text.txt", "r")
    data = file.read()
    print(f"data = {data}")
    file.close()


# try block
try:
    divide(10, 0)

# handles the exception raised in divide function
# specific except block
except ZeroDivisionError:
    print("zero division exception raised")

# handles all other exceptions
# generic except block
except:
    print("generic exception raised")


try:
    read_file()

# handles the exception raised in read_file function
# specific except block
except FileNotFoundError:
    print("file not found exception raised")

# handles all other exceptions
# generic except block
except:
    print("generic exception raised")
