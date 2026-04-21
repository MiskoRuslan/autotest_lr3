import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class TestLogin:
    def test_successful_login(self, driver):
        login = LoginPage(driver)
        login.open().login("Admin", "admin123")

        dashboard = DashboardPage(driver)
        assert dashboard.is_loaded(), (
            f"Очікувався редирект на dashboard, але URL: {driver.current_url}"
        )

    def test_invalid_password(self, driver):
        login = LoginPage(driver)
        login.open().login("Admin", "wrong_password_123")

        error = login.get_error_message()
        assert "Invalid credentials" in error, (
            f"Очікувалось 'Invalid credentials', отримано: '{error}'"
        )

    def test_empty_credentials(self, driver):
        login = LoginPage(driver)
        login.open().click_submit()

        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(driver, 10)
        required_messages = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".oxd-input-field-error-message")
            )
        )
        assert len(required_messages) >= 2, (
            f"Очікувалось ≥2 повідомлення 'Required', знайдено: {len(required_messages)}"
        )
        for msg in required_messages:
            assert "Required" in msg.text, f"Очікувалось 'Required', отримано: '{msg.text}'"

    def test_dashboard_title_after_login(self, driver):
        login = LoginPage(driver)
        login.open().login("Admin", "admin123")

        dashboard = DashboardPage(driver)
        title = dashboard.get_page_title()
        assert "Dashboard" in title, (
            f"Очікувався заголовок 'Dashboard', отримано: '{title}'"
        )

    def test_forgot_password_page(self, driver):
        login = LoginPage(driver)
        login.open().click_forgot_password()

        assert "requestPasswordResetCode" in driver.current_url, (
            f"Очікувалась сторінка відновлення паролю, але URL: {driver.current_url}"
        )

    def test_invalid_username(self, driver):
        login = LoginPage(driver)
        login.open().login("nonexistent_user_xyz", "admin123")

        error = login.get_error_message()
        assert "Invalid credentials" in error, (
            f"Очікувалось 'Invalid credentials', отримано: '{error}'"
        )


    def test_logout_after_login(self, driver):
        login = LoginPage(driver)
        login.open().login("Admin", "admin123")

        dashboard = DashboardPage(driver)
        assert dashboard.is_loaded(), "Вхід не виконано"

        dashboard.logout()

        assert "auth/login" in driver.current_url, (
            f"Після logout очікувалась сторінка логіну, але URL: {driver.current_url}"
        )
