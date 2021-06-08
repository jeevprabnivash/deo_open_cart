from selenium import webdriver
driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demo.opencart.com/")
driver.find_element_by_xpath("//div/a/img[@title='MacBook']").click()
driver.find_element_by_xpath("//div/button[@id='button-cart']").click()
success=driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
print(success)
