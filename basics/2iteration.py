# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("https://www.w3schools.com/java/")
# print(driver.title)

# search = driver.find_element(By.CSS_SELECTOR, "#tnb-google-search-input")
# search.send_keys("HTML")
# search.send_keys(Keys.RETURN)

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div.w3-panel.w3-info.intro"))
#     )
#     examples = element.find_elements(By.CLASS_NAME, "w3-row-padding")
#     for example in examples:
#         header = example.find_element(By.CLASS_NAME, "w3-third")
#         print(header.text)

# finally:    
#     driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/default.asp")

# Wait for the page to load
time.sleep(3)

# Find the main content section
main_content = driver.find_element(By.CLASS_NAME, "w3-main")

# Find all the links within the main content section
links = main_content.find_elements(By.TAG_NAME, "a")

# Iterate through the links and print their text
for link in links:
    print(link.text)

driver.quit()
