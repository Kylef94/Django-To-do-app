from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def tearDown(self) -> None:
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        
        #john hears about a great new to do app and decides to check it out
        browser.get('http://localhost:8000')

        #he notices the page title and header mention to do lists

        self.assertIn('To-do', self.browser.title)
        self.fail("Finish the test!")

        #he is invited to enter a to-do right away

        #he enters a task into the text box

        #he hits enter adn the page updates, now lsiting his todo as an item

        #the input box for new items is still there, he enters another to do

        #the page refreshes, both items are in the list now

        #he wonders if these todos will be remembered, he notices he has a unique url
        #and some text explaining this

        #he visits that url, the todos are still there

        #he is now satisfied

if __name__ == "__main__":
    unittest.main()