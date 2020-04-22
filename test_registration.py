import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_page(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
        first_name.send_keys("Irving")

        last_name = browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
        last_name.send_keys("Shaw")

        email = browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
        email.send_keys("1@1.1")

        button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        button.click()

        time.sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, "h1")
        assert welcome_text.text == "Congratulations! You have successfully registered!", "registration result is different!"

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    test_form_page("http://suninjuly.github.io/registration1.html")
    test_form_page("http://suninjuly.github.io/registration2.html")
