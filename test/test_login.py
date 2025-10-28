import time

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from playwright.sync_api import expect
from config import Config

def test_invalid_userlogin(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.click_my_account()
    home_page.click_login()

    login_page.set_email(Config.invalid_email)
    login_page.set_password(Config.invalid_password)
    login_page.click_login()

    time.sleep(3)
    expect(login_page.get_login_error()).to_be_visible(timeout=3000)


def test_valid_userlogin(page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.click_my_account()
    home_page.click_login()

    login_page.set_email(Config.email)
    login_page.set_password(Config.password)
    login_page.click_login()

    time.sleep(3)
    my_account = MyAccountPage(page)
    expect(my_account.get_my_account_page_heading()).to_be_visible(timeout=3000)
