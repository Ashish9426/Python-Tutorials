# decorator
def log(function):

    def inner(*args, **kwargs):
        # open log file in append mode
        file = open('page4.log', 'a')

        # write the logs
        file.write("-" * 80)
        file.write("\n")
        file.write(f"inside {function.__name__}")
        file.write("\n")
        file.write(f"arguments => {args}")
        file.write("\n")
        file.write(f"kwargs    => {kwargs}")
        file.write("\n")
        file.write("-" * 80)

        # close the file
        file.close()

        function(*args, **kwargs)

    return inner


@log
def add(p1, p2):
    print(f"addition = {p1 + p2}")



@log
def multiply(p1, p2):
    print(f"multiplication = {p1 + p2}")



add(10, 20)
add(40, 70)
multiply(10, 20)
multiply(40, 70)
