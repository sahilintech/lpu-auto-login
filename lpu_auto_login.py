from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://internet.lpu.in/24online/webpages/client.jsp")

username = driver.find_element(By.NAME, "username")
username.clear()
username.send_keys("Your username goes here")

passwd = driver.find_element(By.NAME, "password")
passwd.clear()
passwd.send_keys("Your lpu wifi password goes here")

try:
    checkBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "agreepolicy"))
    )
    checkBox.click()

    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "loginbtn"))
    )
    login.click()

finally:
    driver.quit()