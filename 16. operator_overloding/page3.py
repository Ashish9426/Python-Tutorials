def divide(n1, n2):
    # try:
        division = n1 / n2
        print(f"division = {division}")
    # except:
    #     print("exception raised in divide function")


def function1():
    # try:
        divide(10, 0)
    # except:
    #     print("exception raised in function1")


try:
    function1()
except:
    print(f"exception raised outside function1 or divide")

# try:
#     divide(10, 0)
# except:
#     print(f"exception raised")
