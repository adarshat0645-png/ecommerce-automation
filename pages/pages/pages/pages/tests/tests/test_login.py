from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestLogin:

    def test_valid_login(self, driver):
        """Verify successful login with valid credentials"""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        products_page = ProductsPage(driver)
        assert products_page.get_page_title() == "Products", \
            "Login failed - Products page not displayed"

    def test_invalid_login(self, driver):
        """Verify error message with invalid credentials"""
        login_page = LoginPage(driver)
        login_page.login("invalid_user", "wrong_password")

        error = login_page.get_error_message()
        assert "do not match" in error, \
            "Expected error message not displayed"

    def test_locked_out_user(self, driver):
        """Verify locked-out user cannot log in"""
        login_page = LoginPage(driver)
        login_page.login("locked_out_user", "secret_sauce")

        error = login_page.get_error_message()
        assert "locked out" in error, \
            "Locked out message not displayed"
