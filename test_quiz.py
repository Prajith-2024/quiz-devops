from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_quiz():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("http://localhost:5000")

    driver.find_element(By.XPATH, "//input[@value='4']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    assert "Score: 1" in driver.page_source

    driver.quit()