from playwright.sync_api import Page

def test_valid_otp(page:Page):
    page.goto("https://qaplayground.dev/apps/verify-account/")
    otp = "999999"
    otp_inputs = page.locator(".code-container .code")
    success_state = page.get_by_text("Success")
    for i in range(len(otp)):
        otp_inputs.nth(i).type(otp[i])

    assert success_state.is_visible()
