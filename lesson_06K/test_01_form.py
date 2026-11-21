import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color


@pytest.fixture
def driver():
    browser = webdriver.Edge()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_form_validation_colors(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = wait.until(EC.visibility_of_element_located((By.NAME, "first-name")))
    first_name.send_keys("Иван")

    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")


    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    zip_code_field = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

    def get_bg_rgba(element):
        color_value = element.value_of_css_property("background-color")
        return Color.from_string(color_value).rgba

    zip_color = get_bg_rgba(zip_code_field)
    assert zip_color == "rgba(248, 215, 218, 1)", (
        f"Zip code должен быть красным, но получен {zip_color}"
    )

    green_fields_ids = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company",
    ]

    for field_id in green_fields_ids:
        element = driver.find_element(By.ID, field_id)
        field_color = get_bg_rgba(element)
        assert field_color == "rgba(209, 231, 221, 1)", (
            f"Поле {field_id} должно быть зелёным, но получен {field_color}"
        )
