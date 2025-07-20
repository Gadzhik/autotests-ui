from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    email_field = page.locator('//input[@id=":r0:"]')
    email_field.focus()
    page.keyboard.type('user.name@gmail.com')

    username_field = page.locator('//input[@id=":r1:"]')
    username_field.focus()
    page.keyboard.type('user.name@gmail.com')

    password_field = page.locator('//input[@id=":r2:"]')
    password_field.focus()
    page.keyboard.type('password')

    expect(registration_button).to_be_enabled()

    page.wait_for_timeout(3000)