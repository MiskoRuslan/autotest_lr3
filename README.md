# OrangeHRM Selenium Tests

Автоматизовані тести для https://opensource-demo.orangehrmlive.com/

## Структура проекту

```
OrangeHRM_Tests/
├── pages/
│   ├── __init__.py
│   ├── login_page.py       # Page Object для сторінки логіну
│   └── dashboard_page.py   # Page Object для Dashboard
├── tests/
│   ├── __init__.py
│   └── test_login.py       # 7 тест-кейсів
├── conftest.py             # Fixtures (driver, logged_in_driver)
├── requirements.txt
└── README.md
```

## Встановлення

```bash
pip install -r requirements.txt
```

## Запуск тестів

```bash
# Всі тести
pytest tests/ -v

# З HTML-звітом
pytest tests/ -v --html=report.html --self-contained-html

# Один тест
pytest tests/test_login.py::TestLogin::test_successful_login -v
```

## Тести

| ID | Назва | Очікуваний результат |
|----|-------|----------------------|
| test_successful_login | Успішний вхід | URL містить /dashboard/index |
| test_invalid_password | Невірний пароль | Повідомлення 'Invalid credentials' |
| test_empty_credentials | Порожні поля | Повідомлення 'Required' під полями |
| test_dashboard_title_after_login | Заголовок Dashboard | h6 містить 'Dashboard' |
| test_forgot_password_page | Forgot Password | URL містить /requestPasswordResetCode |
| test_invalid_username | Невірний логін | Повідомлення 'Invalid credentials' |
| test_logout_after_login | Logout | URL містить /auth/login |