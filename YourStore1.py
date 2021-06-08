from selenium import webdriver
driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demo.opencart.com/")
driver.find_element_by_xpath("//div/input").send_keys("Laptop")
driver.find_element_by_xpath("//div/span").click()