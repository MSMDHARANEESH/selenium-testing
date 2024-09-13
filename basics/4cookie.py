from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for the language selector to be clickable
lang_selector = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#langSelect-EN"))
)

# Click on the language selector to switch to English
lang_selector.click()

# Wait for the big cookie and other elements to load
cookie = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "bigCookie"))
)
cookie_count = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "cookies"))
)

# Find items
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]

# Initialize ActionChains
actions = ActionChains(driver)

# Click the cookie repeatedly
for i in range(5000):
    actions.click(cookie).perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
