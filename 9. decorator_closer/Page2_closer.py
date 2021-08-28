# closure

# <h1>header line 1</h1>
# <h1>header line 2</h1>
# <h1>header line 3</h1>

# <div>division 1</div>
# <div>division 2</div>
# <div>division 3</div>

# <p>paragraph 1</p>
# <p>paragraph 2</p>
# <p>paragraph 3</p>


def function1(tag, data):
    print(f"<{tag}>{data}</{tag}>")


# function1("h1", "header line 1")
# function1("h1", "header line 2")
# function1("h1", "header line 3")
#
# function1("div", "division 1")
# function1("div", "division 2")
# function1("div", "division 3")
#
# function1("p", "paragraph 1")
# function1("p", "paragraph 2")
# function1("p", "paragraph 3")



def h1(data):
    print(f"<h1>{data}</h1>")


def div(data):
    print(f"<div>{data}</div>")


def p(data):
    print(f"<p>{data}</p>")


def strong(data):
    print(f"<strong>{data}</strong>")

h1("header 1")
h1("header 2")
h1("header 3")

div("division 1")
div("division 2")
div("division 3")

p("paragraph 1")
p("paragraph 2")
p("paragraph 3")


