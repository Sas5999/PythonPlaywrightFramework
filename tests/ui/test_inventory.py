import re
from playwright.sync_api import Page,expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest
import allure


@pytest.fixture
def inventory_page(page:Page):
    page.goto("https://www.saucedemo.com/")
    login_page = LoginPage(page)
    login_page.login_user("standard_user","secret_sauce")
    return InventoryPage(page)


@allure.title("Heading check")
def test_heading(inventory_page):
    heading = inventory_page.heading()
    assert(heading == "Swag Labs" )


@allure.title("Inventory list ")
def test_inventory_list(inventory_page):
    expect(inventory_page.inventoryList).to_be_visible()


@allure.title("Add to cart ")
def test_add_to_cart(inventory_page):
    inventory_page.addtocart()
    expect(inventory_page.cartbadge).to_have_text("1")

@allure.title("Remove from cart")
def test_remove_from_cart(inventory_page):
    inventory_page.addtocart()
    inventory_page.remove()
    expect(inventory_page.cartbadge).not_to_be_visible



@allure.title("Check footer")
def test_footer(inventory_page):
    inventory_page.footer.scroll_into_view_if_needed()
    expect(inventory_page.footer).to_be_visible














