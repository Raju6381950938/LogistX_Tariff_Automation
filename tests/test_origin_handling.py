import random

from playwright.sync_api import expect
from pages.origin_handling_page import OriginHandlingPage
from test_data.origin_handling_data import (
    get_currency,
    get_end_date,
    get_start_date,
    get_terminal,
)


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

    terminal_value = get_terminal()

    terminal = origin_handling.enter_terminal(terminal_value)

    expect(terminal).to_have_value(str(terminal_value))


    page.screenshot(
            path="screenshots/origin_handling_terminal.png",
            full_page=True
         )

    start_date_value = get_start_date()

    start_date = origin_handling.enter_start_date(start_date_value)

    expect(start_date).to_have_value(start_date_value)

    page.screenshot(
            path="screenshots/origin_handling_start_date.png",
            full_page=True
             )

    end_date_value = get_end_date()
    
    end_date = origin_handling.enter_end_date(end_date_value)
    
    expect(end_date).to_have_value(end_date_value)
    
    page.screenshot(
            path="screenshots/origin_handling_end_date.png",
            full_page=True
                 )

    page.mouse.wheel(0, 500)

    page.get_by_role("button", name="Next - Fixed Fees →").click()

   