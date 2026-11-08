from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")

    assert len(links) == 9, f"Ожидалось 9 ссылок, найдено {len(links)}"

    for link in links:
        assert link.is_displayed(), f"Ссылка '{link.text}' не отображается"

    assert "1" in links[0].text, f"Текст первой ссылки: '{links[0].text}'"

    driver.quit()