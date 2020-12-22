from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    PRODUCT_NAME = (
        By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1'
    )
    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color'
    )
    BASKET_PRODUCT_NAME = (
        By.XPATH, '//*[@id="messages"]/div[1]/div/strong'
    )
    BASKET_PRODUCT_PRICE = (
        By.CSS_SELECTOR, '#messages > .alert-info > div > p > strong'
    )
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR, '#messages > div:nth-child(1) > div.alertinner'
    )
