from playwright.sync_api import Page

class InventoryPage:
    def __init__(self , page:Page):
        self.page = page
        self.heading = page.get_by_text("Swag Labs")
        self.inventoryList = page.locator(".inventory_list")
        self.addtocart = page.locator("#add-to-cart-sauce-labs-fleece-jacket") # remove value should also be checked
        self.remove = page.get_by_text("Remove")
        self.cartbadge = page.locator(".shopping_cart_badge")
        self.filter = page.locator("#product_sort_container") #values should be convered in tests 
        self.footer = page.locator("#footer_copy")

    def add_to_cart(self):
            self.addtocart.click()

    def remove_from_cart(self):
            self.remove.click()


