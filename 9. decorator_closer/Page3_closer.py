# closure
def outer(num):
    print("inside outer")

    def inner():
        print("insider inner")
        print(f"num = {num}, type = {type(num)}")

    return inner


# # function alias
#result = outer(10)
#print(f"result = {result}, type = {type(result)}")
#result()


# closure
def create_tag(tag):

    def inner(data):
        print(f"<{tag}>{data}</{tag}>")

    return inner


# h1 = create_tag('h1')
# h2 = create_tag('h2')
# h3 = create_tag('h3')
# div = create_tag('div')
# p = create_tag('p')
#
# h1('header line 1')
# h1('header line 2')
# h1('header line 3')
#
# h2('header line 1')
# h2('header line 2')
# h2('header line 3')
#
# h3('header line 1')
# h3('header line 2')
# h3('header line 3')
#
# div('division 1')
# div('division 2')
# div('division 3')
#
# p('paragraph 1')
# p('paragraph 2')
# p('paragraph 3')


# closure
def create_table(number):

    def inner(count=10):
        # table = [number * index for index in range(1, count + 1)]
        # print(table)

        for index in range(1, count + 1):
            print(f"{number} x {index} = {number * index}")

    return inner

# number_2 = create_table(2)
# number_2()

number_5 = create_table(5)
number_5(20)
