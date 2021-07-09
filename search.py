from selenium.webdriver.common.keys import Keys
class Search(object):
    def __init__(self, driver):
        self.driver = driver

class SearchBar(Search):
    def input(self):
        search_bar = self.driver.find_element_by_id("twotabsearchtextbox")
        search_bar.clear()
        search_bar.send_keys("panda")
        search_bar.send_keys(Keys.ENTER)
        return True

class Items(Search):

    def select_item(self, search_result):
        result = self.driver.find_element_by_xpath('//div[@data-cel-widget="search_result_{0:d}"]'.format(search_result))
        result.find_element_by_class_name('a-link-normal').click()
        return True

    # This method isnt used due to Amazon's antibot security. It instantly closes the driver
    def add_wishlist(self):
        list = self.driver.find_element_by_id('wishListMainButton')
        list.click()
        return True

    def check_cart_empty(self):
        cart = self.driver.find_element_by_id('nav-cart-count-container')
        cart.click()
        self.driver.implicitly_wait(1)
        empty = self.driver.find_element_by_class_name('sc-your-amazon-cart-is-empty')
        return True

