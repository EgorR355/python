from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

AVATAR_BUTTON_SELECTOR = "button.navbar-main__user-dropdown-toggle"
PROFILE_LINK_SELECTOR = ".dropdown-item[href^='/user/']"


def open_profile(driver):
    avatar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, AVATAR_BUTTON_SELECTOR))
    )
    avatar.click()

    profile_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, PROFILE_LINK_SELECTOR))
    )
    profile_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains("/user/"))
    return driver.current_url


def test_session_storage_auth():
    driver = webdriver.Chrome()

    cookie_user1 = {
        "name": "SESSION",
        "value": "Yzk2MTBkMTktNjAwYS00NTUyLWExYzctMWEwMTY4NmNjNGRj",
        "domain": ".gitflic.ru"
    }
    cookie_user2 = {
        "name": "SESSION",
        "value": "NjgyNmEzNjYtOTlkYy00NzkwLTkwMmItYzRlZjhkMjA0Y2Mw",
        "domain": ".gitflic.ru"
    }

    try:
        driver.get("https://gitflic.ru/")
        driver.add_cookie(cookie_user1)
        driver.refresh()
        url_user1 = open_profile(driver)

        driver.delete_all_cookies()

        driver.get("https://gitflic.ru/")
        driver.add_cookie(cookie_user2)
        driver.refresh()
        url_user2 = open_profile(driver)

        assert url_user1 != url_user2, f"URL пользователей совпадают: {url_user1}"

    finally:
        driver.quit()
        