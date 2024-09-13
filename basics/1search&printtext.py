from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver=webdriver.Chrome()

driver.get("https://www.w3schools.com/java/")
print(driver.title)

search=driver.find_element(by=By.CSS_SELECTOR,value="#tnb-google-search-input")
search.send_keys("HTML")
search.send_keys(Keys.RETURN)
# print(driver.page_source)

#elements.clear()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div.w3-panel.w3-info.intro"))
    )
    print(element.text)
    
except:    
    driver.quit()

driver.quit()