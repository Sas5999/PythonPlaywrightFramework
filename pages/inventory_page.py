from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.locator(".app_logo")
        self.inventoryList = page.locator(".inventory_list")
        self.cartbadge = page.locator('[data-test="shopping-cart-badge"]')
        self.cartIcon = page.get_by_test_id("shopping-cart-link")
        self.filter = page.locator("#product_sort_container")
        self.footer = page.locator(".footer_copy")

    def add_to_cart_button(self, product_slug: str):
        return self.page.locator(f"[data-test='add-to-cart-{product_slug}']")

    def remove_button(self, product_slug: str):
        return self.page.locator(f"[data-test='remove-{product_slug}']")

    def add_to_cart(self, product_slug: str = "sauce-labs-backpack"):
        self.add_to_cart_button(product_slug).click()

    def remove_from_cart(self, product_slug: str = "sauce-labs-backpack"):
        self.remove_button(product_slug).click()

    def go_to_cart(self):
        self.cartIcon.click()

    def sort_by(self, value: str):
        self.filter.select_option(value)