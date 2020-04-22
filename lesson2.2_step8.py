from selenium import webdriver
import time
import os

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/file_input.html')
	for inp in browser.find_elements_by_css_selector(".form-group input"):
		inp.send_keys("data")
	#inputFirstName = browser.find_element_by_name('firstname').send_keys('Ihor')
	#inputLastName = browser.find_element_by_name('lastname').send_keys('Zubenko')
	#inputEmail = browser.find_element_by_name('email').send_keys('izubenkotest@gmail.com')
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'zubenkocv.txt')
	uploadButton = browser.find_element_by_css_selector('input[type="file"]')
	uploadButton.send_keys(file_path)
	submitButton = browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
	time.sleep(5)
	browser.quit()



'''
import os
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.txt')

if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        pass

inputs = ['Aleksey', 'Bychutkin', 'test@gmail.com', file_path]

for element, value in zip(browser.find_elements_by_tag_name('input'), inputs):
    element.send_keys(value)

browser.find_element_by_css_selector('button.btn').click()
'''