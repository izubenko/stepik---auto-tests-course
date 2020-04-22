from selenium import webdriver
import time
import math

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/execute_script.html')
	x = browser.find_element_by_id("input_value").text
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	y = calc(x)
	input = browser.find_element_by_id('answer').send_keys(y)
	checkboxRobot = browser.find_element_by_id('robotCheckbox').click()
	radiobuttonRobot = browser.find_element_by_id('robotsRule')
	browser.execute_script("return arguments[0].scrollIntoView(true);", radiobuttonRobot)
	radiobuttonRobot.click()
	button = browser.find_element_by_class_name('btn-primary').click()


finally:
	time.sleep(5)
	browser.quit()
