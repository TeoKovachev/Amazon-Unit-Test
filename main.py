import unittest
from selenium import webdriver

# A file containing the local path to the driver
import chromeDriverPath
PATH = chromeDriverPath.PATH

# File containing all automation
import search as search

# A class that contains all the automation methods from the search file
class TheTest(object):
    def automated_part(self):
        numTests = 0 # Number of automation methods called and completed
        numItems = 1 # Order list of Amazon product search result list

        # Find search bar, insert item name, press enter to search
        if search.SearchBar.input(self): numTests+=1

        # Find first item in the search result, click it
        self.driver.implicitly_wait(1)
        if search.Items.select_item(self,numItems):
            numTests+=1
            numItems+=1

        # Method not used due to Amazon's antibot security. It closes the driver
        # Add item to wishlist
        #self.driver.implicitly_wait(1)
        #if search.Items.add_wishlist(self): numTests+=1

        # Go to cart and check if empty
        self.driver.implicitly_wait(1)
        if search.Items.check_cart_empty(self): numTests+=1

        # Making sure all methods return True, makeshift assertment
        return numTests==3

# The main unit test
class AmazonWebTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.amazon.com/")

    # Testing the class above
    def test_whole(self):
        assert TheTest.automated_part(self)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
