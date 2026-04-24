import pytest
import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def inventory_page(page: Page, base_url):
    print("VALUE:", base_url)

    page.goto(base_url)
    login_page = LoginPage(page)
    login_page.login_user("standard_user", "secret_sauce")

    expect(page).to_have_url(f"{base_url}inventory.html")
    return InventoryPage(page)


@allure.title("Inventory list is visible")
def test_inventory_list(inventory_page):
    expect(inventory_page.inventoryList).to_be_visible()


@allure.title("Add item to cart updates badge count")
def test_add_to_cart(inventory_page):
    inventory_page.add_to_cart()
    expect(inventory_page.cartbadge).to_have_text("1")


@allure.title("Add then remove item hides badge")
def test_add_then_remove_from_cart(inventory_page):
    inventory_page.add_to_cart()
    inventory_page.remove_from_cart()
    expect(inventory_page.cartbadge).not_to_be_visible()

@allure.title("Footer is visible after scroll")
def test_footer(inventory_page):
    inventory_page.footer.scroll_into_view_if_needed()
    expect(inventory_page.footer).to_be_visible()