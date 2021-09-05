def divide(n1, n2):
    # try block
    try:

        # exception can be raised
        division = n1 / n2
        print(f"division = {division}")

    # except block
    except:
        print(f"except has raised")


# divide(10, 0)


def read_file():
    try:
        file = open("mYtext.txt", "r")
        data = file.read()
        print(f"data = {data}")
        file.close()
    except:
        print("the file does not exist")


read_file()
