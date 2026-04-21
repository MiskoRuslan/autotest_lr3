from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    URL_FRAGMENT = "/web/index.php/dashboard/index"

    HEADER_TITLE  = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")
    USER_DROPDOWN = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    LOGOUT_ITEM   = (By.XPATH, "//a[normalize-space()='Logout']")
    NAV_ITEM      = (By.CSS_SELECTOR, ".oxd-nav-item")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 15)

    def is_loaded(self):
        return self.URL_FRAGMENT in self.driver.current_url

    def get_page_title(self):
        el = self.wait.until(EC.visibility_of_element_located(self.HEADER_TITLE))
        return el.text.strip()

    def logout(self):
        self.driver.find_element(*self.USER_DROPDOWN).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_ITEM)).click()
