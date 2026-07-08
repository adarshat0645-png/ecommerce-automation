from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    # Actions
    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEM))

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
