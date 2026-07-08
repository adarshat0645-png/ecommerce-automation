from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


class TestCart:

    def test_add_product_to_cart(self, driver):
        """Verify product can be added to cart"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(driver)
        products_page.add_backpack_to_cart()
        assert products_page.get_cart_count() == "1", \
            "Cart badge count is incorrect"

        products_page.go_to_cart()
        cart_page = CartPage(driver)
        assert cart_page.get_cart_item_count() == 1, \
            "Product not found in cart"
