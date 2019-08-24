# importing required libraries
from selenium import webdriver
import pandas as pd
import time
import csv
import os
from selenium.webdriver.firefox.options import Options

# open firefox browser
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)


def open_browser(url):
    # open required url
    browser.get(url)
    time.sleep(1)


def close_browser():
    browser.close()


url = 'https://www.healthy-india.org/bmi_calculator.php'

file_path = os.path.cwd() + "/auto_test.csv"

with open(file_path, newline='') as test_data_file:
    read_values = list(csv.reader(test_data_file))


def test_runner(input_1, input_2):
    xpath_input_1 = "//input[@id='txtweight']"
    xpath_input_2 = "//input[@id='txtheight']"
    xpath_submit = "//input[@name='submit']"
    xpath_act_result = "//span[contains(text(), 'BMI')]"

    browser.find_element_by_xpath(xpath_input_1).send_keys(input_1)
    browser.find_element_by_xpath(xpath_input_2).send_keys(input_2)
    browser.find_element_by_xpath(xpath_submit).click()
    act_result = browser.find_element_by_xpath(xpath_act_result).text
    return act_result


def get_data_and_test(read_values):
    for i in range(1, len(read_values)):
        input_1 = read_values[i][0]
        for j in range(1, 2):
            input_2 = read_values[j][1]
            output = test_runner(input_1, input_2)
            read_values[i].append(output)
            if read_values[i][2] == read_values[i][3]:
                read_values[i].append("Test passed")
            else:
                read_values[i].append("Test Failed")
    return read_values


def write_to_external_csv(read_values):
    df = pd.DataFrame(read_values)
    df.to_csv('auto_tested.csv', index=False, header=False)


if __name__ == "__main__":
    open_browser(url)
    get_data_and_test(read_values)
    write_to_external_csv(read_values)
    close_browser()
