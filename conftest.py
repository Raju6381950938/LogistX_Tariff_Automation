import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page_setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000
        )

        page = browser.new_page()

        page.goto(
            "https://dev.tariff.logistx.us/195586042318260187944884050901207115",
            wait_until="domcontentloaded"
        )

        yield page

        page.wait_for_timeout(5000)
        browser.close()



