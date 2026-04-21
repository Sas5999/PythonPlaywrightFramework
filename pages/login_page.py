from playwright.sync_api import Page
class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_cta = page.locator("#login-button")
        self.wrong_creds_error = page.get_by_text("Epic sadface: Username and password do not match any user in this service")
        self.no_creds_error = page.get_by_text("Epic sadface: Username is required")
        self.no_pass_error = page.get_by_text("Epic sadface: Password is required")
        
    def enter_username(self,username:str):
        self.username_input.fill(username)

    def enter_password(self,password:str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_cta.click()       

    def login_user(self,username:str ,password:str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_cta.click()
        self.page.wait_for_url("**/inventory.html")






