import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_saucedemo_total(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    products_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie",
    ]
    for product_id in products_to_add:
        wait.until(EC.element_to_be_clickable((By.ID, product_id))).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    total_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text

    assert "$58.29" in total_text, f"Ожидалась сумма $58.29, получено: {total_text}"
    