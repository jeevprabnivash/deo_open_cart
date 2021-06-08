import random
import string
from selenium import webdriver

driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://demo.opencart.com/")


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

email1=random_char(7)+"@gmail.com"
print(email1)
driver.find_element_by_xpath("//div/ul/li/a[@title='My Account']").click()
driver.find_element_by_xpath("//div/ul/li/ul/li/a[@href='https://demo.opencart.com/index.php?route=account/register']").click()
driver.find_element_by_xpath("//div/input[@name='firstname']").send_keys("Nivash")
driver.find_element_by_xpath("//div/input[@name='lastname']").send_keys("J P")
driver.find_element_by_xpath("//div/input[@name='email']").send_keys(email1)
driver.find_element_by_xpath("//div/input[@name='telephone']").send_keys("12345678")
driver.find_element_by_xpath("//div/input[@name='password']").send_keys("1234")
driver.find_element_by_xpath("//div/input[@name='confirm']").send_keys("1234")
driver.find_element_by_xpath("//div/input[@type='checkbox']").click()
driver.find_element_by_xpath("//div/input[@type='submit']").click()
success1=driver.find_element_by_xpath("//div[@id='content']/h1").text
print(success1)
# alert1=driver.find_element_by_xpath("//div/p[1]]").text
# print(alert1)





# print (random_char(7)+"@gmail.com")
