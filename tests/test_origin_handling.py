from playwright.sync_api import expect
from pages.origin_handling_page import OriginHandlingPage


def test_origin_handling(page_setup):

    page = page_setup

    origin_handling = OriginHandlingPage(page)

    page.get_by_role("button", name="Origin Handling").click()

    currency = origin_handling.select_currency("INR - Indian Rupee")
    expect(currency).to_have_value("INR - Indian Rupee")
   
    page.screenshot(
        path="screenshots/origin_handling_currency.png",
        full_page=True
       )

    