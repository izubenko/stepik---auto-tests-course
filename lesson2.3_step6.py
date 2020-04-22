from selenium import webdriver
import time
import math

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/redirect_accept.html')
	buttonTroll = browser.find_element_by_class_name('btn-primary').click()
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	x = int(browser.find_element_by_id('input_value').text)
	answer = browser.find_element_by_id('answer').send_keys(str(math.log(abs(12*math.sin(x)))))
	submit = browser.find_element_by_css_selector('button[type="submit"]').click()

	
finally:
	time.sleep(5)
	browser.quit()