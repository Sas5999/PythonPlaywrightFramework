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

@allure.testcase("Creds validation")
def test_credsfield_validations(page:Page) -> None:
    page.goto("https://www.saucedemo.com/")
    login_page =LoginPage(page)
    login_page.click_login()
    expect(login_page.no_creds_error).to_be_visible()

@allure.testcase("Pass check")
def test_passwordfield_validation(page:Page) -> None:
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.enter_username("standard_user")
    login_page.click_login()
    expect(login_page.no_pass_error).to_be_visible()

@allure.testcase("Invalid login")
def test_invalidLogin(page:Page) -> None:
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sahuce")
    login_page.click_login()
    
    expect(login_page.wrong_creds_error).to_be_visible()

@allure.testcase("Valid login")
def test_validLogin(page:Page) -> None:
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")













