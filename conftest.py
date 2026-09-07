import pytest
from playwright.sync_api import Page


@pytest.fixture
def page_setup(page: Page):
    page.goto(
        "https://dev.tariff.logistx.us/489010921037307298672556035815421025",
        wait_until="domcontentloaded"
    )

    page.wait_for_timeout(5000)

    yield page

    page.wait_for_timeout(5000)


