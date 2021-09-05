def divide(n1, n2):
    division = n1 / n2
    print(f"division = {division}")

def read_file():
    file = open("text.txt", "r")
    data = file.read()
    print(f"data = {data}")
    file.close()

try:
    divide(10, 2)
    divide(10, 0)
    read_file()

except ZeroDivisionError:
    print("zero division exception raised")

except FileNotFoundError:
    print("file not found exception raised")

except:
    print("generic exception raised")