from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_action(self):
        self.should_be_add_to_basket_button()
        self.add_product_to_basket()

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_to_basket_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"

    def should_be_match_product_and_basket_parameters(self):
        self.should_be_match_name_of_product_and_name_in_basket()
        self.should_be_match_price_of_product_and_price_in_basket()

    def should_be_match_name_of_product_and_name_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Product name is not present"
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text
        basket_product_name = self.browser.find_element(
            *ProductPageLocators.BASKET_PRODUCT_NAME
        ).text
        assert product_name == basket_product_name, \
            "Product name and product name in basket didn`t match"
        print(f"Product with name {product_name} was added to basket")

    def should_be_match_price_of_product_and_price_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "Product price is not present"
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        basket_product_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRODUCT_PRICE
        ).text
        print(f"Product price is {product_price}, price in basket is {basket_product_price}")
        assert product_price == basket_product_price, \
            "Product price and product price in basket didn`t match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_be_disappeare_element(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
