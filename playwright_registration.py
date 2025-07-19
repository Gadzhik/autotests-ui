from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_field = page.locator('//div//input[@id=":r0:"]')
    email_field.fill('user.name@gmail.com')

    username_field = page.locator('//div//input[@id=":r1:"]')
    username_field.fill('username')

    password_field = page.locator('//input[@id=":r2:"]')
    password_field.fill('password')

    register_button = page.get_by_test_id('registration-page-registration-button')
    register_button.click()

    dashboard_message = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_message).to_be_visible()
    expect(dashboard_message).to_have_text('Dashboard')

    page.wait_for_timeout(3000)


