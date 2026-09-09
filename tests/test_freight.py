import pytest
from playwright.sync_api import expect
from pages.freight_page import freightPage


@pytest.mark.order(3)
def test_freight(page_setup):

    page = page_setup

    freight = freightPage(page)

    page.get_by_role("button", name="freight").click()

    

