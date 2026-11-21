import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_slow_calculator(driver):
    page = CalculatorPage(driver)

    page.open()

    page.set_delay(45)

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    page.wait_for_result("15")
    assert page.get_screen_text() == "15", (
        f"Ожидался результат 15, получено: {page.get_screen_text()}"
    )
    