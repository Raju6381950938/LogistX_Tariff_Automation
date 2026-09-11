import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page_setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=500,
            args=["--disable-gpu"]
        )

        page = browser.new_page()

        page.goto(
            "https://dev.tariff.logistx.us/123614366232414564921753344888600973",
            wait_until="domcontentloaded"
        )

        yield page

        page.wait_for_timeout(1000)
        browser.close()


