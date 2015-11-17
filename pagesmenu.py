from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        global wait
        wait = WebDriverWait(driver, 300)
        global page_input
        page_input = "page1"

class MainPage(BasePage):
        def test_allpages_link(self):
            driver = self.driver
            pages = wait.until(EC.visibility_of_element_located((By.ID, 'menu-pages')))
            actions = ActionChains(driver)
            actions.move_to_element(pages)
            actions.perform()
            allpages = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'All Pages')))
            allpages.click()

        def test_pagetable_heading(self):
            driver = self.driver
            page_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.wp-list-table.widefat.fixed.pages')))
            actions = ActionChains(driver)
            actions.move_to_element(page_table)
            actions.perform()
            heading = page_table.find_element_by_tag_name('thead')
            row = heading.find_element_by_tag_name('tr')
            th = []
            th = row.find_elements_by_tag_name('th')
   #         print(th.text)
    #        td = []
     #       td = row.find_elements_by_tag_name('td')
            assert th[0].text == "Select All"
            if True:
                print("At th[0] text is"+ th[0].text)
            assert th[1].text == "Title"
            assert th[2].text == "Author"
            assert th[3].text == ""
            assert th[4].text == "Date"
            assert th[5].text == "Views"
            assert th[6].text == "SEO"
            assert th[7].text == "SEO Title"
            assert th[8].text == "Meta Desc."
            assert th[9].text == "Focus KW"
            for th_value in th:
                print(th_value.text)

        def test_create_page(self):
            driver = self.driver
            add_new = driver.find_element_by_link_text('Add New')
            actions = ActionChains(driver)
            actions.move_to_element(add_new)
            actions.perform()
            add_new.click()
            title = wait.until(EC.visibility_of_element_located((By.ID, 'title-prompt-text')))
            title.send_keys("paa")
            text_button = wait.until(EC.visibility_of_element_located((By.ID, 'content-html')))
            text_button.click()
            content = wait.until(EC.visibility_of_element_located((By.ID, 'content')))
            content.send_keys("paa content ")
            driver.find_element_by_id('save-post').click()                                 
            
            
	def test_page_added(self):
		driver = self.driver
		page_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.wp-list-table.widefat.fixed.pages')))
		actions = ActionChains(driver)
		actions.move_to_element(page_table)
		actions.perform()
		#page_table = driver.find_element_by_class_name('wp-list-table.widefat.fixed.pages')
            	page_body = page_table.find_element_by_tag_name('tbody')
            	body_row = []
		body_row = page_body.find_elements_by_tag_name('tr')
		for row in body_row:
                    th = row.find_element_by_tag_name('th')
                    td = []
                    td = row.find_elements_by_tag_name('td')
                    if td[0].text == page_input+" - Draft":
                        for td_value in td: 
                            print(td_value.text)
                    elif td[0].text == "paa":
                        for td_value in td:
                                 print(td_value.text)
            
        
    
