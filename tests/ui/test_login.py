import re
from playwright.sync_api import Page,expect
from pages.login_page import LoginPage
import pytest
import allure

# @pytest.mark.parametrize(
#         "username,password" ,
#         [
#             ("standard_user","secret_sauce"),
#             ("standard_user","secret_sahuce")
#         ]
# )

@pytest.fixture
def login_page(page:Page):
    page.goto("https://www.saucedemo.com/")
    return LoginPage(page)

@allure.title("Creds validation")
def test_credsfield_validations(login_page) -> None:
    # page.goto("https://www.saucedemo.com/")
    # login_page =LoginPage(page)
    login_page.click_login()
    expect(login_page.no_creds_error).to_be_visible()

@allure.title("Pass check")
def test_passwordfield_validation(login_page) -> None:
    # page.goto("https://www.saucedemo.com/")
    # login_page = LoginPage(page)
    login_page.enter_username("standard_user")
    login_page.click_login()
    expect(login_page.no_pass_error).to_be_visible()

@allure.title("Invalid login")
def test_invalidLogin(login_page) -> None:
    # page.goto("https://www.saucedemo.com/")
    # login_page = LoginPage(page)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sahuce")
    login_page.click_login()
    
    expect(login_page.wrong_creds_error).to_be_visible()

@allure.title("Valid login")
def test_validLogin(login_page) -> None:
    # page.goto("https://www.saucedemo.com/")
    # login_page = LoginPage(page)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")













