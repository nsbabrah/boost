#Author: Navjot Singh Babrah
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
username = "navbabrah"
password = "babrah123"
target='navjotbabrah'
time.sleep(3)
getdriver = ("https://www.instagram.com/accounts/login/")

driver = webdriver.Chrome()
driver.get(getdriver)

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
time.sleep(3)

r=driver.find_element_by_xpath("//input[@class='_9x5sw']").click()
driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(target)
wait = WebDriverWait(driver, 20)
#////////////////////////////////////////////
# driver.find_element_by_xpath("//a[@class='_k2vj6 _xk9bu']").click()
time.sleep(4)
age = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._o1o4h")))
age.click()
time.sleep(4)
age1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._ovg3g")))
age1.click()

age1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._tk4ba")))
age1.click()
