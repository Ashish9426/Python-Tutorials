def divide(n1, n2):
    division = n1 / n2
    print(f"division = {division}")


def add():
    pass


try:
    divide(10, 0)
except ZeroDivisionError:
    print("n2 is zero")
except:
    print("exception raised")
else:
    print("next line after divide (else block)")
finally:
    # calls irrespective of any exception
    # - called when there is no exception
    # - called when there is an exception
    print("this is a finally block")
