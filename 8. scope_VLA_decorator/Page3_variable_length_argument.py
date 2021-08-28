def add1(p1, p2):
    addition = p1 + p2
    print(f"addition = {addition}")

# add1(20,30)
# add1(p1=10, p2=20)

def add2(p1, p2, p3):
    addition = p1 + p2 + p3
    print(f"addition = {addition}")


# add2(10, 20, 30)

# variable length argument function
def add(*args, **kwargs):
    print("inside function add")
    print(f"args = {args}, type = {type(args)}")
    print(f"kwargs = {kwargs}, type = {type(kwargs)}")
    addition = 0
    for value in args:
        addition += value

    print(f"addition = {addition}")


# add(40, 50, 60, p1=10, p2=20, p3=30)
# add(10)
# add(10, 20)
# add(10, 20, 30)
# add(10, 20, 30, 40)
# add(10, 20, 30, 40, 50)


def draw_circle(*args, **kwargs):
    radius, color, border_width = 10, "red", 10

    print(f"radius = {kwargs.get('radius')}")
    print(f"color = {kwargs.get('color')}")
    print(f"border width = {kwargs.get('border_width')}")

    # check if key radius exists
    if kwargs.get('radius'):
        radius = kwargs.get('radius')

    # check if key color exists
    if kwargs.get('color'):
        color = kwargs.get('color')

    # check if key border_width exists
    if kwargs.get('border_width'):
        border_width = kwargs.get('border_width')

    print(f"radius = {radius}")
    print(f"color = {color}")
    print(f"border_width = {border_width}")


draw_circle()
# draw_circle(color="green")
# draw_circle(radius=50, color="blue", border_width=5)





