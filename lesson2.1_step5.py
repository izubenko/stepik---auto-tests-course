from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    def calc(x):
    	return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    inpu1 = browser.find_element_by_class_name('form-control')
    inpu1.send_keys(y)
    checkbox1 = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    radiobutton1 = browser.find_element_by_css_selector("[value='robots']").click()
    button1 = browser.find_element_by_class_name('btn-default').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

'''
from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

x = browser.find_element_by_css_selector('[id = "input_value"]').text
browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))

for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
    browser.find_element_by_css_selector(selector).click()
'''