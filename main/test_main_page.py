from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    ''' Тестируем возможность перехода на страницу логина для ананимного юзера'''
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
