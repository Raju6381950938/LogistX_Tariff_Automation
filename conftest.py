import pytest
from playwright.sync_api import Page


@pytest.fixture
def page_setup(page: Page):
    page.goto(
        "https://dev.tariff.logistx.us/104338920338453802483362134034588548",
        wait_until="domcontentloaded"
    )

    page.wait_for_timeout(5000)

    yield page

    page.wait_for_timeout(5000)

    