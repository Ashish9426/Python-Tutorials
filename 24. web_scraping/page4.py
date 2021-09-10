from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def function1():
    url = "https://www.accuweather.com/en/in/pune/204848/daily-weather-forecast/204848"

    browser = webdriver.Chrome('/Users/amitk/selenium/chromedriver')
    browser.get(url)
    time.sleep(2)

    # find div containing the temp information
    divs = browser.find_elements_by_class_name('daily-wrapper')

    temperatures = []
    for div in divs:
        # date
        h2 = div.find_element_by_class_name('date')
        span_dow = h2.find_element_by_class_name('dow')
        span_sub = h2.find_element_by_class_name('sub')

        # print(f"day = {span_dow.text}")
        # print(f"date = {span_sub.text}")

        # temperature
        div_temp = div.find_element_by_class_name('temp')
        div_high = div_temp.find_element_by_class_name('high')
        div_low = div_temp.find_element_by_class_name('low')

        # print(f"div high = {div_high.text}")
        # print(f"div low = {div_low.text}")

        # percipitation
        div_precip = div.find_element_by_class_name('precip')

        # remove the special character
        temp_high = div_high.text.replace('°', '')

        # remove the special characters
        temp_low = div_low.text.replace('°', '')
        temp_low = temp_low.replace('/', '')

        # remove the special character
        precip = div_precip.text.replace('%', '')

        temperatures.append({
            "day": span_dow.text,
            "date": span_sub.text,
            "high_temp": int(temp_high),
            "low_temp": int(temp_low),
            "precip": int(precip)
        })

    browser.close()

    # print("information")
    # print(temperatures)

    file = open('temperatures.csv', 'w')
    file.write(f"day,date,high temp,low temp,precip\n")
    for dictionary in temperatures:
        file.write(f"{dictionary['day']},{dictionary['date']},{dictionary['high_temp']},{dictionary['low_temp']},{dictionary['precip']}\n")

    file.close()


# function1()


def function2():
    import matplotlib.pyplot as plt
    import pandas as pd

    df = pd.read_csv('./temperatures.csv')
    # print(df.columns)

    days = range(1, len(df['high temp']) + 1)
    plt.plot(days, df['high temp'], color="red", label="High Temperature")
    plt.scatter(days, df['high temp'], color="red")

    plt.plot(days, df['low temp'], color="green", label="Low Temperature")
    plt.scatter(days, df['low temp'], color="green")

    plt.xlabel("Days")
    plt.ylabel("Temperatures")
    plt.title("Temperatures in October")

    plt.legend()

    plt.tight_layout()
    plt.show()


function2()