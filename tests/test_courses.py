from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_field = page.get_by_test_id('registration-form-email-input').locator('input')
        email_field.fill('tmpuser0@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('tmpuser1')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser_state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser_state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_header).to_be_visible()
        expect(courses_header).to_have_text('Courses')

        icon_check = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_check).to_be_visible()

        results_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(results_text).to_be_visible()
        expect(results_text).to_have_text('There is no results')

        result_pipelene_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(result_pipelene_text).to_be_visible()
        expect(result_pipelene_text).to_have_text('Results from the load test pipeline will be displayed here')

        page.wait_for_timeout(3000)