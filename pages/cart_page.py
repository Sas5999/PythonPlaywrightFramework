from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_quantity = page.locator('[data-test="item-quantity"]')
        self.title = page.locator('[data-test="title"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.inventory_price = page.locator('[data-test="inventory-item-price"]')

    def get_page_url(self):
        return self.page.url

    def remove_button(self, product_slug: str):
        return self.page.locator(f"[data-test='remove-{product_slug}']")


    def get_all_quantities(self):
        return self.cart_quantity.all_text_contents()
    

    def is_loaded(self):
        self.title.is_visible()

    def remove_product(self,product_slug: str):
         self.remove_button(product_slug).click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def checkout(self):
        self.checkout_button.click()



        




    



    




    
    


    

    

