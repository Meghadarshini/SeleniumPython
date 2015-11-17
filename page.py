#from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from element import BasePageElement

class BasePage(object):

	def __init__(self, driver):
		#global driver
        	self.driver = driver
		global username_input
		username_input = "mm"
                global password_input
		password_input = "s1rp4syMPJM9"
		global wait
		wait = WebDriverWait(driver, 300)
		


class MainPage(BasePage):

        def test_login(self):

                driver = self.driver
#                wait = WebDriverWait(driver, 100)

                driver.get("http://howley.in/")
                driver.find_element_by_link_text('Login').click()
#                username_input = "mm"
 #               password_input = "s1rp4syMPJM9"
                #username = driver.find_element_by_id('user_login')
		
                username = wait.until(EC.visibility_of_element_located((By.ID, 'user_login')))
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

        def test_goto_profile(self):
		driver = self.driver

#                wait = WebDriverWait(driver, 1000)

                display = wait.until(EC.visibility_of_element_located((By.ID, 'wp-admin-bar-my-account')))
#               display = wait.until(EC.visibility_of_element_located((By.ID,"wp-admin-bar-my-account")))
#		driver = self.driver
 #               display = driver.find_element_by_id('wp-admin-bar-my-account')
                name_display = display.text
                print(name_display)
                assert name_display == "Howdy, "+username_input
#               except AssertionError: "not same"
                actions = ActionChains(driver)
                actions.move_to_element(display)
                actions.perform()
                driver.find_element_by_link_text(username_input).click()
	
	
        def test_allpages_link(self):
            driver = self.driver
            pages = wait.until(EC.visibility_of_element_located((By.ID, 'menu-pages')))
            actions = ActionChains(driver)
            actions.move_to_element(pages)
            actions.perform()
            allpages = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'All Pages')))
            allpages.click()	




	def test_page_added(self):
		driver = self.driver
		page_table = driver.find_element_by_class_name('wp-list-table.widefat.fixed.pages')
		page_body = page_table.find_element_by_tag_name('tbody')
		body_row = page_body.find_element_by_tag_name('tr')
		for row in body_row:
                    th = row.find_element_by_tag_name('th')
                    td = row.find_element_by_tag_name('td')
                    if td[0].text == "page1 - Draft":
                        print(td.text)   
