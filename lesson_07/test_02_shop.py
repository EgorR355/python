import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_saucedemo_checkout_total(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    products = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie",
    ]
    for product in products:
        inventory_page.add_to_cart(product)

    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Иван", "Петров", "123456")

    checkout_page.continue_to_overview()

    total_text = checkout_page.get_total()

    assert "$58.29" in total_text, (
        f"Ожидалась итоговая сумма $58.29, получено: {total_text}"
    )
