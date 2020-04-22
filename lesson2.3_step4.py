from selenium import webdriver
import time
import math

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/alert_accept.html')
	button1 = browser.find_element_by_css_selector('button[type="submit"]').click()
	confirm = browser.switch_to.alert.accept()
	x = int(browser.find_element_by_id('input_value').text)
	answer = browser.find_element_by_id('answer').send_keys(str(math.log(abs(12*math.sin(x)))))
	submit = browser.find_element_by_css_selector('button[type="submit"]').click()
	alertText = browser.switch_to.alert.text.split(': ')[-1]
	print(alertText)

finally:
	time.sleep(5)
	browser.quit()

'''
# получение ответа и автоматический его ввод на степике
from selenium import webdriver
import os
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

button = browser.find_element_by_class_name('btn-primary').click()
browser.switch_to.alert.accept()

x = browser.find_element_by_id("input_value").text
y = calc(x)

browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_class_name('btn-primary').click()

alert = browser.switch_to.alert
alert_text = alert.text.split()
alert.accept()
answer = alert_text[-1]

browser.get('https://stepik.org/catalog?auth=login&language=ru')
time.sleep(5)

browser.find_element_by_id('id_login_email').send_keys('***')# здесь вводится e-mail
browser.find_element_by_id('id_login_password').send_keys('***')# здесь вводится пароль

browser.find_element_by_class_name('sign-form__btn').click()
time.sleep(3)
browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
time.sleep(3)

answer_input = browser.find_element_by_css_selector('textarea')
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
answer_input.send_keys(answer)

button = browser.find_element_by_class_name('submit-submission')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(1)
button.click()
'''


'''
#c def
import math
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    ans = alert.text.split()[-1]
    print(ans)
    alert.accept()

    return ans


def stepik_auth(remote: webdriver.Remote):
    remote.get(auth_link)
    WebDriverWait(remote, 3).until(lambda x: x.find_element_by_name("login"))
    auth_elems = ("login", "password")

    for auth_elem in auth_elems:
        remote.find_element_by_name(auth_elem).send_keys(os.getenv(auth_elem))
    remote.find_element_by_class_name("sign-form__btn").click()
    WebDriverWait(
        remote,
        3).until(lambda x: x.find_element_by_class_name("navbar__profile-img"))


def stepik_send_answer(remote: webdriver.Remote, answer: str):
    remote.get("https://stepik.org/lesson/184253/step/4?unit=158843")
    WebDriverWait(remote,
                  3).until(lambda x: x.find_element_by_tag_name("textarea"))
    remote.find_element_by_tag_name("textarea").send_keys(answer)
    remote.find_element_by_class_name("submit-submission").click()
    WebDriverWait(remote, 3).until(lambda x: x.find_element_by_id("correct"))


link = "http://suninjuly.github.io/alert_accept.html"
auth_link = "https://stepik.org/catalog?auth=login"
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_css_selector("[type = \"submit\"]").click()
    browser.switch_to.alert.accept()
    WebDriverWait(browser,
                  5).until(lambda x: x.find_element_by_id("input_value"))
    browser.find_element_by_id("answer").send_keys(
        calc(browser.find_element_by_id("input_value").text))
    browser.find_element_by_css_selector("[type = \"submit\"]").click()
    answer = print_answer(browser)
    stepik_auth(browser)
    stepik_send_answer(browser, answer)
finally:
    browser.quit()
'''