from selenium import webdriver
driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demo.opencart.com/")

driver.find_element_by_xpath("//div/ul/li/a[@title='My Account']").click()
driver.find_element_by_xpath("//div/ul/li/ul/li/a[@href='https://demo.opencart.com/index.php?route=account/register']").click()
driver.find_element_by_xpath("//div/input[@name='firstname']").send_keys("Nivash")
driver.find_element_by_xpath("//div/input[@name='lastname']").send_keys("J P")
driver.find_element_by_xpath("//div/input[@name='email']").send_keys("jeevprabnivash@gmail.com")
driver.find_element_by_xpath("//div/input[@name='telephone']").send_keys("12345678")
driver.find_element_by_xpath("//div/input[@name='password']").send_keys("1234")
driver.find_element_by_xpath("//div/input[@name='confirm']").send_keys("1234")
driver.find_element_by_xpath("//div/input[@type='checkbox']").click()
driver.find_element_by_xpath("//div/input[@type='submit']").click()
warn_msg=driver.find_element_by_xpath("//div[@class='alert alert-danger alert-dismissible']").text
print(warn_msg)