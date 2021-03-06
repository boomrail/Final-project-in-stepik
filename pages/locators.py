from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    WELCOME_TEXT = (
        By.CSS_SELECTOR,
        "#promotions > section:nth-child(1) > div > h2"
    )


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    PASSWORD_REPEAT_FIELD = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')


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


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '#basket_formset > div')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
