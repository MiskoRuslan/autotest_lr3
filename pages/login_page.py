# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    # Локатори
    USERNAME_INPUT   = (By.NAME, "username")
    PASSWORD_INPUT   = (By.NAME, "password")
    SUBMIT_BUTTON    = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE    = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    FORGOT_LINK      = (By.CSS_SELECTOR, ".orangehrm-login-forgot p")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)
        return self

    def enter_username(self, username):
        field = self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
        field.clear()
        field.send_keys(username)
        return self

    def enter_password(self, password):
        field = self.driver.find_element(*self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)
        return self

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        return self

    def login(self, username, password):
        return self.enter_username(username).enter_password(password).click_submit()

    def get_error_message(self):
        el = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return el.text.strip()

    def click_forgot_password(self):
        self.driver.find_element(*self.FORGOT_LINK).click()
        return self
