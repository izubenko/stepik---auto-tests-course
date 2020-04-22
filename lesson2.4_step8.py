from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/explicit_wait2.html')
	WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
	button = browser.find_element(By.ID, 'book').click()
	x = int(browser.find_element(By.ID, 'input_value').text)
	answer = browser.find_element_by_id('answer').send_keys(str(math.log(abs(12*math.sin(x)))))
	submit = browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
	time.sleep(3)
	browser.quit()