import unittest



        def setUpClass(cls):
		self.driver = webdriver.Firefox()
                self.driver.maximize_window()
                driver = self.driver



        def setUp(self):
                self.driver = webdriver.Firefox()
                self.driver.maximize_window()
                driver = self.driver
def suite():
	suite = unittest.TestSuite()
	suite.addTest(HowleyLogin('test_login'))
	suite.addTest(HowleyLogin('test_goto_profile'))
	return suite 
