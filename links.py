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
        self.driver = driver
        global wait
        wait = WebDriverWait(driver, 300)
        global link_heading
        #link_heading = "July11Test"
#        link_heading = "Suggest Ideas"
        link_heading = "Documentation"
        global link_url
        #link_url = "https://www.google.com"
        link_url = "wordpress.org/extend/ideas"
        global description
        description = "Desc SampleJuly11Test"
        # global assertEqual
        global categories
        categories = "Blogroll"
        
        

class MainPage(BasePage):

    def test_click_links(self):
        driver = self.driver
        links = wait.until(EC.visibility_of_element_located((By.ID, 'menu-links')))
        actions = ActionChains(driver)
        actions.move_to_element(links)
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'All Links'))).click()
        #driver.find_element_by_link_text('All Links').click()

    def test_table_headings(self):
        driver = self.driver

        links_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.wp-list-table.widefat.fixed.bookmarks')))       
        actions = ActionChains(driver)
        actions.move_to_element(links_table)
        actions.perform()
        table_heading = links_table.find_element_by_tag_name('thead')
        table_heading_row = table_heading.find_element_by_tag_name('tr')
        table_heading_row_values = table_heading_row.find_elements_by_tag_name('th')
        print(table_heading_row_values[0].text)
        print(table_heading_row_values[1].text)
        print(table_heading_row_values[2].text)
        print(table_heading_row_values[3].text)
        print(table_heading_row_values[4].text)
        print(table_heading_row_values[5].text)
        print(table_heading_row_values[6].text)
        assert table_heading_row_values[0].text == "Select All"
        assert table_heading_row_values[1].text == "Name"
        assert table_heading_row_values[2].text == "URL"
        assert table_heading_row_values[3].text == "Categories"
        assert table_heading_row_values[4].text == "Relationship"
        assert table_heading_row_values[5].text == "Visible"
        assert table_heading_row_values[6].text == "Rating"
     #   '''
      #  assertEqual(table_heading_row_values[0].text, "Select All", msg="Select All incorrect")
       # print(table_heading_row_values[0].text)
        #assertEqual(table_heading_row_values[1].text, "Name", msg="Name incorrect")
        #assertEqual(table_heading_row_values[2].text, "URL", msg="URL incorrect")
#        assertEqual(table_heading_row_values[3].text, "Categories", msg="Categories incorrect")
 #       assertEqual(table_heading_row_values[4].text, "Relationship", msg="Relationship incorrect")
  #      assertEqual(table_heading_row_values[5].text, "Visible", msg="Visible incorrect")
   #     assertEqual(table_heading_row_values[6].text, "Rating", msg="Rating incorrect")
    #'''
    def test_table_row_values(self):
        print(1)
        driver = self.driver
        links_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.wp-list-table.widefat.fixed.bookmarks')))
        actions = ActionChains(driver)
        actions.move_to_element(links_table)
        actions.perform()
        table_body = links_table.find_element_by_tag_name('tbody')
        table_body_rows = table_body.find_elements_by_tag_name('tr')
        for row_values in table_body_rows:
        #for row_values in table_body_rows[:]:
            table_body_row_th_values = row_values.find_elements_by_tag_name('th')
            for row_th_value in table_body_row_th_values:
                print(row_th_value.text)
            #print(row_values.find_element_by_tag_name('th').text)
            table_body_row_td_values = row_values.find_elements_by_tag_name('td')
            #for row_td_value in table_body_row_td_values[:]:
            for row_td_value in table_body_row_td_values:
                print(row_td_value.text)

    def test_create_link(self):
        driver = self.driver
        add_new_link = driver.find_element_by_link_text('Add New')
        actions = AcionChains(driver)
        actions.move_to_element(add_new_link)
        actions.perform()
        add_new_link.click()
        link_title = wait.until(EC.visibility_of_element_located((By.ID, 'link_name')))
        link_title.send_keys(link_heading)
        link_address = wait.until(EC.visibility_of_element_located((By.ID, 'link_url')))
        link_address.send_keys(link_url)
        link_info = wait.until(EC.visibility_of_element_located((By.ID, 'link_description')))
        link_info.send_keys(description)
        link_category = wait.until(EC.visibility_of_element_located((By.ID, 'in-link-category-2')))
        link_category.click()
        driver.find_element_by_id('publish').click()

    def test_verify_link_created(self):
        driver = self.driver
        links = wait.until(EC.visibility_of_element_located((By.ID, 'menu-links')))
        actions = ActionChains(driver)
        actions.move_to_element(links)
        actions.perform()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'All Links'))).click()
        links_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.wp-list-table.widefat.fixed.bookmarks')))
        actions = ActionChains(driver)
        actions.move_to_element(links_table)
        actions.perform()
        table_body = links_table.find_element_by_tag_name('tbody')
        table_body_rows = table_body.find_elements_by_tag_name('tr')
        for row_values in table_body_rows:
            ##make th list 
            title = driver.find_elements_by_tag_name('td')
           # title = driver.find_element_by_tag_name('th')
            title_text = title[0].text           
            print(title_text)
            print(link_heading)
            assert title_text == link_heading
            if True:
                print(title_text)
                table_body_row_td_values = row_values.find_elements_by_tag_name('td')
                for row_td_value in table_body_row_td_values:
                    print(row_td_value.text)
            if False:
                print()
    #def test_edit_link(self):

    #def test_delete_link(self):

    def test_click_url(self):
        driver = self.driver
        links_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.wp-list-table.widefat.fixed.bookmarks')))
        actions = ActionChains(driver)
        actions.move_to_element(links_table)
        actions.perform()
        table_body = links_table.find_element_by_tag_name('tbody')
        table_body_rows = table_body.find_elements_by_tag_name('tr')
        for row_values in table_body_rows:
            title = driver.find_elements_by_tag_name('td')
            title_text = title[0].text           

            assert title_text == link_heading
            if True:
                url = title[1].text
                assert url == link_url
                if True:
                    driver.find_element.by_link_text(url).click()

    def test_click_category(self):
        driver = self.driver
        links_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.wp-list-table.widefat.fixed.bookmarks')))
        actions = ActionChains(driver)
        actions.move_to_element(links_table)
        actions.perform()
        table_body = links_table.find_element_by_tag_name('tbody')
        table_body_rows = table_body.find_elements_by_tag_name('tr')
        for row_values in table_body_rows:
            title = driver.find_elements_by_tag_name('td')
            title_text = title[0].text           

            assert title_text == link_heading
            if True:
                category = title[2].text
                assert category == categories
                if True:
                    driver.find_element_by_link_text(category).click()

                    
        


                            
                
                
        
        
                
        
        


                
                
            
        
        
        
        
        
        
        
        
