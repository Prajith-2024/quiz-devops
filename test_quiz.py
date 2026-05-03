from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_quiz():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("http://127.0.0.1:5000")

    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@value='4']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    time.sleep(2)

    assert "Score: 1" in driver.page_source

    driver.quit()