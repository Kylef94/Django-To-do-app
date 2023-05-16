from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def tearDown(self) -> None:
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        
        #john hears about a great new to do app and decides to check it out
        self.browser.get('http://localhost:8000')

        #he notices the page title and header mention to do lists

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)
        

        #he is invited to enter a to-do right away
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #he enters a task into the text box
        inputbox.send_keys('Buy peacock feathers')
        
        #he hits enter adn the page updates, now lsiting his todo as an item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        
        #the input box for new items is still there, he enters another to do
        self.fail("Finish the test!")
        
        #the page refreshes, both items are in the list now

        #he wonders if these todos will be remembered, he notices he has a unique url
        #and some text explaining this

        #he visits that url, the todos are still there

        #he is now satisfied

if __name__ == "__main__":
    unittest.main()