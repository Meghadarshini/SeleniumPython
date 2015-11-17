from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        global wait
        wait = WebDriverWait(driver, 300)
        global current_window

class MainPage(BasePage):
    def test_hover_seo(self): 
        driver = self.driver
        seo = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'SEO')))
        actions = ActionChains(driver)
        actions.move_to_element(seo)
        actions.perform()
 #       keyword_research = wait.until(EC.visibility_of_element_located((By.ID, 'wp-admin-bar-wpseo-kwresearch')))
#        if(keyword_research.text == 'Keyword Research'):
        #keyword_research = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Keyword Research')))
 #           actions = ActionChains(driver)
  #          actions.move_to_element(keyword_research)
   #         actions.perform()
    #        adwords_external = wait.until(EC.visibility_of_element_located((By.ID, 'wp-admin-bar-wpseo-adwordsexternal')))
         #   google_insights = wait.until(EC.visibility_of_element_located((By.ID, 'wp-admin-bar-wpseo-googleinsights')))
         #   seo_book = wait.until(EC.visibility_of_element_located((By.ID, 'wp-admin-bar-wpseo-wordtracker')))
         #   keyword_list = ['AdWords External', 'Google Insights', 'SEO Book']
        #for i in range(0, len(keyword_research)):
          #  if(adwords_external.text == keyword_list[0]):
           #     print(adwords_external.text)
         #   if(google_insights.text == keyword_list[1]):
          #      print(google_insights.text)
         #   if(seo_book.text == keyword_list[2]):
          #      print(seo_book.text)
     #   current_window = driver.current_window_handle    
      #  actions = ActionChains(driver)
       # actions.move_to_element(keyword_research)
#        print("moved")
 #       actions.click(adwords_external)
  #      actions.click()
         #   driver.find_element_by_id('wp-admin-bar-wpseo-adwordsexternal').click()
          #  print("clicked")
   #     actions.perform()
         #   print("performed")

            
            
            
        
    def test_adwords_page(self):
        driver = self.driver
        seo = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'SEO')))
        actions = ActionChains(driver)
        actions.move_to_element(seo)
        actions.perform()
        keyword_research = wait.until(EC.visibility_of_element_located((By.ID, 'wp-admin-bar-wpseo-kwresearch')))
      #  if(keyword_research.text == 'Keyword Research'):
        #keyword_research = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Keyword Research')))
       #     actions = ActionChains(driver)
        #    actions.move_to_element(keyword_research)
         #   actions.perform()
          #  adwords_external = wait.until(EC.visibility_of_element_located((By.ID, 'wp-admin-bar-wpseo-adwordsexternal')))

        current_window = driver.current_window_handle    
        actions = ActionChains(driver)
        actions.move_to_element(keyword_research)
        print("moved")
       # actions.click(adwords_external)
       # actions.click()
        actions.perform()
        #adwords_external = wait.until(EC.visibility_of_element_located((By.ID, 'wp-admin-bar-wpseo-adwordsexternal')))
        adwords_external = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'AdWords External')))
        current_window = driver.current_window_handle                                       
        actions = ActionChains(driver)
       # actions.move_to_element(adwords_external)
       # actions.move_to_element(adwords_external)
        actions.move_to_element(keyword_research)
        #actions.click()
        actions.click(adwords_external)
        actions.perform()          

       # wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ads')))
        assert "Google Ads" in driver.title       
        for handle in driver.window_handles:
            if(current_window != handle):
                driver.switch_to_window(handle)
        assert "Google Ads" in driver.title
        driver.switch_to_window(current_window)

    def test_google_insights(self):
        driver = self.driver
        seo = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'SEO')))
        actions = ActionChains(driver)
        actions.move_to_element(seo)
        actions.perform()
        keyword_research = wait.until(EC.visibility_of_element_located((By.ID , 'wp-admin-bar-wpseo-kwresearch')))
        actions = ActionChains(driver)
        actions.move_to_element(keyword_research)
        actions.perform()
        current_window = driver.current_window_handle
        google_insights = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Google Insights')))
        actions = ActionChains(driver)
        actions.move_to_element(keyword_research)
        actions.click(google_insights)
        actions.perform()
        for handle in driver.window_handles:
            if(handle != current_window):
               driver.switch_to_window(handle)
               assert "Boundries + Google" in driver.title
        driver.switch_to_window(current_window)               

                                          
    def test_google_page_speed(self):
        driver = self.driver
        seo = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'SEO')))
        actions = ActionChains(driver)
        actions.move_to_element(seo)
        actions.perform()                                      
        analyze_this_page = wait.until(EC.visibility_of_element_located((By.ID, 'wp-admin-bar-wpseo-analysis')))
        actions = ActionChains(driver)
        actions.move_to_element(analyze_this_page)
        actions.perform()
        google_page_speed_test= wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Google Page Speed Test')))
        current_window = driver.current_window_handle                                       
        actions = ActionChains(driver)
        actions.move_to_element(google_page_speed_test)
        actions.click()
        actions.perform()
        for handle in driver.window_handles:
            if(handle != current_window):
                driver.switch_to_window(handle)
        assert "PageSpeed Insights" in driver.title
        driver.switch_to_window(current_window)
        
    def test_check_rich_snippets(self):
        driver = self.driver
        seo = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'SEO')))
        actions = ActionChains(driver)
        actions.move_to_element(seo)
        actions.perform()
        analyze_this_page = wait.until(EC.visibility_of_element_located((By.ID, 'wp-admin-bar-wpseo-analysis')))
        actions = ActionChains(driver)
        actions.move_to_element(analyze_the_page)
        actions.perform()
        current_window = driver.current_window_handle
        check_rich_snippets = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Check Rich Snippets')))
        actions = ActionChains(driver)
        #actions.move_to_element(check_rich_snippets)
        actions.move_to_element(analyze_the_page)
        actions.click(check_rich_snippets)
        actions.perform()
        for handle in driver.window_handles:
            if(handle != current_window):
                driver.switch_to_window(handle)
                assert "Structured Data Testing Tool    |   Google Developers" in driver.title
        driver.switch_to_window(current_window)
        
            
