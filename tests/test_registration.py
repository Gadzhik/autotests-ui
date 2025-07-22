from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_field = chromium_page.locator('//div//input[@id=":r0:"]')
    email_field.fill('user.name@gmail.com')

    username_field = chromium_page.locator('//div//input[@id=":r1:"]')
    username_field.fill('username')

    password_field = chromium_page.locator('//input[@id=":r2:"]')
    password_field.fill('password')

    register_button = chromium_page.get_by_test_id('registration-page-registration-button')
    register_button.click()

    dashboard_message = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_message).to_be_visible()
    expect(dashboard_message).to_have_text('Dashboard')

    chromium_page.wait_for_timeout(3000)
