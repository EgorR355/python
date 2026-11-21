from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        delay_input = self.wait.until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, label):
        locator = (By.XPATH, f"//span[text()='{label}']")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_screen_text(self):
        return self.driver.find_element(*self.SCREEN).text

    def wait_for_result(self, expected_text):
        return self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_text)
        )
    