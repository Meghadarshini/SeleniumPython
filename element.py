from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):

	def __set__(self, obj, value):
		driver = obj.driver

	def __get__(self, obj, owner):
		driver = obj.driver
