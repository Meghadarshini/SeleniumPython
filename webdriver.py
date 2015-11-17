from selenium import webdriver 

driver = None

def get_or_create_webdriver():
	global driver
	driver = webdriver.Firefox()
	return driver



