from selenium.webdriver.common.by import By


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    # Actions
    def get_page_title(self):
        return self.driver.find_element(*self.PAGE_TITLE).text

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
