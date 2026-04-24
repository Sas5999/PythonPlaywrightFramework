from playwright.sync_api import Page
from pages.checkout_page_two import CheckoutPageTwo

class CheckoutPageOne:
    def __init__(self, page:Page):
        self.page = page
        self.cancel_checkout_CTA = page.locator("#cancel")
        self.first_name_field = page.locator('[data-test="firstName"]')
        self.last_name_field = page.locator('data-test="lastName"')
        self.zipcode_field = page.locator('data-test="postalCode"')
        self.continue_checkout = page.locator('data-test="continue"')
        


    
    def checkout_title(self) -> str:
        return self.page.title()
    
    def enter_checkout_details(self , firstname:str, lastname:str , zipcode:str) -> CheckoutPageTwo:
        self.first_name_field.fill(firstname)
        self.last_name_field.fill(lastname)
        self.zipcode_field(zipcode)
        self.continue_checkout.click()
        return CheckoutPageTwo(self.page)


    def checkout_url(self) -> str:
        return self.page.url()