from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.safari.service import Service
from selenium.webdriver.edge.service import Service
import time


def form_automator(website, webdriver, name, student_number, address, phone_number, internship,semester, program):
    path = '/Users/andreisandor/Documents/driver'
    service = Service(excutable_path=path)

    if(str(webdriver) == "Chrome"):
        driver = webdriver.Chrome(service=service)

    elif (str(webdriver) == "Firefox"):
        driver = webdriver.FireFox(service=service)

    elif (str(webdriver) == "Safari"):
        driver = webdriver.FireFox(service=service)

    elif (str(webdriver) == "Edge"):
        driver = webdriver.FireFox(service=service)

    else:
        return "Wrong browser"

    driver.get(website)

    info = ["Name", "Studend Id", "Address", "Phone Number", "Internship", "Semester", "Program"]
    data = [str(name), str(student_number), str(address), str(phone_number), str(internship), str(semester), str(program)]

    info_form = dict(zip(info,data))

    driver.get(website)

    for info, data in info_form.items():
        input = driver.find_element(by='xpath',
                                     value=f'//div[contains(@data-params, "{info}")]//textarea | '
                                           f'//div[contains(@data-params, "{info}")]//input')
        input.send_keys(data)

    submit_button = driver.find_element(by='xpath', value='//div[@role="button"]//span[text()="Submit"]')
    submit_button.click()

    driver.quit()


