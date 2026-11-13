from playwright.sync_api import Page, expect
import pytest

pytestmark = pytest.mark.smoke

def test_ecommerce_homepage(app_page: Page):
    expect(app_page).to_have_url("https://www.saucedemo.com/")


def test_login_fields_visibile(app_page: Page):
    expect(app_page.get_by_placeholder("Username")).to_be_visible()
    expect(app_page.get_by_placeholder("Password")).to_be_visible()