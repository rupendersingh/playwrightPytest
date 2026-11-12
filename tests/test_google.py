import re
from playwright.sync_api import expect

def test_google_title(page):
    page.goto("https://www.google.com/")
    try:
        page.get_by_role("button",name="Accept all").click(timeout=1000)
    except:
        print("No pop up to accept")
    page.get_by_role("combobox",name="Search").fill("Playwright with python")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Playwright"))