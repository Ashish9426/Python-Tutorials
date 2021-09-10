from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <h1>This is a header1</h1>
            <div id="day1">30</div>
            <div id="day2">40</div>
            <div id="day4">37</div>
            <div id="day3">35</div>
        </body>
    </html>
"""


def function1():
    # instantiate BS and parse the html
    soup = BeautifulSoup(html, "html.parser")

    # find a tag named h1 and get the contents within it
    h1 = soup.find('h1')

    # print(h1)
    print(f"contents within h1 = {h1.text}")


# function1()


def function2():
    # instantiate BS and parse the html
    soup = BeautifulSoup(html, "html.parser")

    # find all occurances of div
    divs = soup.find_all('div')

    for div in divs:
        print(f"temperature = {div.text}")


# function2()


def function3():
    # instantiate BS and parse the html
    soup = BeautifulSoup(html, "html.parser")

    # find div with id = day3
    div = soup.find('div', {"id": "day3"})

    print(f"temperature = {div.text}")


function3()
