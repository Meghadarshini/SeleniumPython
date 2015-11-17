import unittest
from element import BasePageElement
import init
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 
#from selenium.common.exceptions.WebdriverException import AssertionException

class BasePage(object):

	 #@classmethod
#        def setUpClass(cls):
 #               cls.driver = webdriver.Firefox()
#               global driver = cls.driver
                #driver = webdriver.Firefox()
  #              cls.driver.maximize_window()


	def __init__(self, driver):
		self.driver = driver

#class HowleyLogin(unittest.TestCase):
class HowleyLogin(BasePage):
	
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox()
#		global driver = cls.driver
		#driver = webdriver.Firefox()
		cls.driver.maximize_window()

#		cls.driver.maximize_window()
	

#	def setUp(self):
#		global driver
		#driver = self.driver


	#def setUp(self):
#		self.driver = webdriver.Firefox()
#		self.driver.maximize_window()
#		driver = self.driver

#		wait = WebDriverWait(self.driver, 10)
		
	#	usernameInput = "mm"
	#	passwordInput = "s1rp4syMPJM9"

	def test_login(self):
#		driver = init.get_or_create_webdriver()
		#global driver = self.driver
		wait = WebDriverWait(driver, 100)

		driver.get("http://howley.in/")
		driver.find_element_by_link_text('Login').click()
	        username_input = "mm"
                password_input = "s1rp4syMPJM9"
#		username = driver.find_element_by_id('user_login')
		username = wait.until(EC.visibility_of_element_located((By.ID,'user_login')))
		actions = ActionChains(driver)
		actions.move_to_element(username)
		actions.perform()
		username.send_keys(username_input)
		password = driver.find_element_by_id('user_pass')
		password.send_keys(password_input)
		remember_me = driver.find_element_by_id('rememberme')
		if(remember_me.is_selected()):
			remember_me.click()
		driver.find_element_by_name('user-submit').click()
		

#		display = driver.find_element_by_id('wp-admin-bar-my-account')
 #               name_display = display.text
  #              print(name_display)
#                assert name_display == "Howdy, "+username_input
#               except AssertionError: "not same"
#                actions = ActionChains(driver)
#                actions.move_to_element(display)
#                actions.perform()
#                driver.find_element_by_link_text(username_input).click()

#return driver

	def test_goto_profile(self):
#		driver = test_login()
#		wait = WebDriverWait(driver, 1000)

#		display = wait.until(EC.visibility_of_element_located(By.ID,'wp-admin-bar-my-account'))
#		display = wait.until(EC.visibility_of_element_located((By.ID,"wp-admin-bar-my-account")))

		display = driver.find_element_by_id('wp-admin-bar-my-account')
		name_display = display.text
		print(name_display)
		assert name_display == "Howdy, "+username_input
#		except AssertionError: "not same"
		actions = ActionChains(driver)
		actions.move_to_element(display)
		actions.perform()
		driver.find_element_by_link_text(username_input).click()


	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
#	def tearDown(self):
#		self.driver.close()

if __name__ == "__main__":
	unittest.main()


