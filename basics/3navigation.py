from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver=webdriver.Chrome()

driver.get("https://www.w3schools.com/java/")
print(driver.title)


link=driver.find_element(by=By.CSS_SELECTOR,value="#subtopnav > a.ga-nav.subtopnav_firstitem")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div:nth-child(3) > a.w3-right.w3-btn"))
    )
    element.click()


    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div:nth-child(3) > a.w3-right.w3-btn"))    
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div:nth-child(3) > a.w3-right.w3-btn"))    
    )
    element.click()

    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()
    driver.forward()
finally:   
    driver.quit()


