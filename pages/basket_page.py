from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
           "Basket items is presented, but should not be"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), \
            "Empty basket text is not presented"
        empty_basket_text = self.browser.find_element(
            *BasketPageLocators.BASKET_EMPTY_TEXT
        ).text
        assert empty_basket_text == "Your basket is empty. Continue shopping", \
            "Basket text is different than expected"
