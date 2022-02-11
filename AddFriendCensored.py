from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()


#Okay I guess you gotta log in because of Headless Chrome
driver.get("https://spacehey.com/login") #navigate to home

#WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.email,'body')))
emailInput = "XXX" #ENTER EMAIL ADDRESS
passInput = "XXX" #ENTER PASSWORD

email = driver.find_element_by_id('email')
email.send_keys(emailInput)

password = driver.find_element_by_id('password')
password.send_keys(passInput)

submittest = driver.find_element_by_class_name('login_btn.standalone')
submittest.submit()


#turned into loop
#better as try instead of if

while True:
	try:
		driver.get("https://spacehey.com/requests")
		count = driver.find_element_by_class_name('count')
		if count != 0:
			acceptAll = driver.find_element_by_xpath("/html/body/div/main/div/div/div[2]/form/button") #this is the XPath
			acceptAll.click()
			driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')
	except NoSuchElementException:
        	driver.refresh
        	time.sleep(5)

else:
		driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')
		time.sleep(5)
			
driver.quit()

#Order
#Go to SpaceHey homepage
#Check that you are logged in
#Go to requests page
#Check that friend requests are available 
#if driver.find_elements_by_css_selector('button.inner'):
#    print "Button exists"
#Find add friend button
#Use submit instead of click for Add All Friends button
#Refresh page
#Loop