from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print(driver.current_url)
print(driver.title)
