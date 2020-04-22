from selenium import webdriver
from math import log, sin
import time
from selenium.webdriver.support.ui import Select


try:
	browser = webdriver.Chrome()

	browser.get('http://suninjuly.github.io/selects1.html')
	x = browser.find_element_by_id('num1').text
	y = browser.find_element_by_id('num2').text
	num1 = int(x)
	num2 = int(y)
	sum_el = str(num1 + num2)
	print(sum_el)
	select = Select(browser.find_element_by_id('dropdown'))
	select.select_by_visible_text(sum_el)
	button1 = browser.find_element_by_class_name('btn-default').click()
	
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
