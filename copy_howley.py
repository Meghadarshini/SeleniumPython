import unittest
#from element import BasePageElement
#import init
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
import page
import links
import seo
import pagesmenu
#import pdb

#class Settings:
#	driver = webdriver.Firefox()

class Howley(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
                cls.driver = webdriver.Firefox()
	
#		cls.driver = Settings.driver
#               global driver = cls.driver
                #driver = webdriver.Firefox()
                cls.driver.maximize_window()
		global alert
#		global assertEqual
#	def setUp(self):
#		self.driver = Settings.driver

	def test_methods(self):
		main_page = page.MainPage(self.driver)
		#pdb.set_trace()
		main_page.test_login()
		main_page.test_goto_profile()
		pagesmenu_page = pagesmenu.MainPage(self.driver)
		
		pagesmenu_page.test_allpages_link()
		pagesmenu_page.test_pagetable_heading()
		pagesmenu_page.test_create_page()
		Alert(driver).accept()
#		alert = Alert(driver)
#		alert.accept()
		pagesmenu_page.test_allpages_link()
		pagesmenu_page.test_page_added()
#		main_page.test_goto_profile()
#		assertEqual(A, A, msg="crct")
#		assertEqual(A, B, msg="incrct")

#		links_page = links.MainPage(self.driver)
#		links_page.test_click_links()
#		links_page.test_table_headings()
#		links_page.test_table_row_values()
#		links_page.test_create_link()
#		links_page.test_click_links()
#		links_page.test_verify_link_created()
#		links_page.test_click_links()
#		links_page.test_click_url()
#		links_page.test_click_links()
#		links_page.test_click_category()
#		seo_page = seo.MainPage(self.driver)
#		seo_page.test_hover_seo()
#		seo_page.test_adwords_page()
#		seo_page.test_google_insights()
#		seo_page.test_google_page_speed()
#		seo_page.test_check_rich_snippets()

        @classmethod
        def tearDownClass(cls):
                cls.driver.close()
#       def tearDown(self):
#               self.driver.close()

if __name__ == "__main__":
        unittest.main()

	



