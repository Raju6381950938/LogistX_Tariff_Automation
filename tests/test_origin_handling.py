import random

from playwright.sync_api import expect
from pages.origin_handling_page import OriginHandlingPage
from test_data.origin_handling_data import get_currency


def test_origin_handling(page_setup):

    page = page_setup

    origin_handling = OriginHandlingPage(page)

    page.get_by_role("button", name="Origin Handling").click()

    currency_value = get_currency()

    currency = origin_handling.select_currency(currency_value)

    expect(currency).to_have_value(currency_value)
   
    page.screenshot(
        path="screenshots/origin_handling_currency.png",
        full_page=True
       )
    
    density_value = random.randint(50,100)

    density = origin_handling.enter_density(density_value)

    expect(density).to_have_value(str(density_value))

    page.screenshot(
        path="screenshots/origin_handling_density.png",
        full_page=True
    )


     
