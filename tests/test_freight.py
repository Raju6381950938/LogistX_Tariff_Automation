import random
import re

import pytest

from playwright.sync_api import expect

from pages.freight_page import FreightPage

from test_data.freight_data import (
    get_currency,
    get_density,
    get_terminal,
    get_unpacking,
    get_arrival,
    get_start_date,
    get_end_date,
    get_terminal_fee,
    get_UOM,
    get_basis,
    get_terminal_minimum,
    get_fee,
    get_rate,
    get_base_rate,
    get_minimum,
    get_condition,
    get_weight,
    get_per_kg,
    get_fuel_surcharge,
    get_notification,
    get_carrier,
    get_transit_days,
)
 

@pytest.mark.order(3)
def test_freight(page_setup):

    page = page_setup

    freight = FreightPage(page)

    page.get_by_role("button", name="Freight").click()

    currency_value = get_currency()
    currency = freight.select_currency(currency_value)
    expect(currency).to_have_value(currency_value)

    page.screenshot(
        path="screenshots/freight_currency.png",
        full_page=True
    )

    density_value = random.randint(50,100)
    density = freight.enter_density(density_value)
    expect(density).to_have_value(str(density_value))

    terminal_value = get_terminal()
    terminal = freight.enter_terminal(terminal_value)
    expect(terminal).to_have_value(str(terminal_value))

    page.screenshot(
        path="screenshots/terminl.png",
        full_page=True
    )

    unpacking_value = get_unpacking()
    unpacking = freight.select_unpacking(unpacking_value)
    expect(unpacking).to_have_value(unpacking_value)

    arrival_value = get_arrival()
    arrival = freight.enter_arrival(arrival_value)
    expect(arrival).to_have_value(str(arrival_value))
    
    page.screenshot(
            path="screenshots/arrival.png",
            full_page=True
        )

    page.mouse.wheel(0, 500)

    start_date_value = get_start_date()
    
    start_date = freight.enter_start_date(start_date_value)
    
    expect(start_date).to_have_value(start_date_value)
    
    page.screenshot(
                path="screenshots/freight_start_date.png",
                full_page=True
                 )
    
    end_date_value = get_end_date()
        
    end_date = freight.enter_end_date(end_date_value)
        
    expect(end_date).to_have_value(end_date_value)

    page.mouse.wheel(0, 500)

    page.locator("#step1NextBtn").click()

    page.mouse.wheel(0, -500)

    terminal_fee_value = get_terminal_fee()
    terminal_fee = freight.enter_terminal_fee(terminal_fee_value)
    expect(terminal_fee).to_have_value(str(terminal_fee_value))

    freight.select_terminal_fee_uom_and_basis(get_UOM(), get_basis())

    terminal_minimum_value = get_terminal_minimum()
    terminal_minimum = freight.enter_terminal_minimum(terminal_minimum_value)
    expect(terminal_minimum).to_have_value(str(terminal_minimum_value))
    
    freight.select_terminal_minimum_uom_and_basis(get_UOM(), get_basis())

    for i in range(3):
        page.locator("button[class='add-btn origin-additional-fee-btn']").click()
    
    for i in range(2):
        page.locator("button[aria-label='Remove additional fee 1']").click()


    fee_value = get_fee()
    fee = freight.enter_fee(fee_value)
    expect(fee).to_have_value(fee_value)
    
    rate_value = get_rate()
    rate = freight.enter_rate(rate_value)
    expect(rate).to_have_value(str(rate_value))
    
    freight.select_fee_uom_and_basis(get_UOM(), get_basis())

    page.mouse.wheel(0, 500)
    
    page.get_by_role("button", name="Next - Variable Fees").click()

    for i in range(5):
        page.get_by_role("button", name="+ Add New Breakpoint").click()

    for i in range(5):
        page.locator("button[aria-label='Remove BP 2']").click()

    base_rate_value = get_base_rate()
    base_rate = freight.enter_base_rate(base_rate_value)
    expect(base_rate).to_have_value(str(base_rate_value))

    minimum_rate_value = get_minimum()
    minimum_rate = freight.enter_minimum_rate(minimum_rate_value)
    expect(minimum_rate).to_have_value(str(minimum_rate_value))

    condition_value = get_condition()
    condition = freight.select_condition(condition_value)
    expect(condition.locator("option:checked")).to_have_text(condition_value)

    weight_value = get_weight()       
    weight = freight.enter_weight(weight_value)        
    expect(weight).to_have_value(str(weight_value))

    per_kg_value = get_per_kg()    
    per_kg = freight.enter_per_kg(per_kg_value)      
    expect(per_kg).to_have_value(str(per_kg_value))

    charge_type = freight.select_charge_type("Chargeable")
    expect(charge_type).to_have_value("Chargeable")

    page.mouse.wheel(0, 300)

    fuel_surcharge_value = get_fuel_surcharge()
    fuel_surcharge = freight.enter_fuel_surcharge(fuel_surcharge_value)
    expect(fuel_surcharge).to_have_value(str(fuel_surcharge_value))
    
    freight.select_fuel_surcharge_uom_and_basis(get_UOM(), get_basis())

    notification_value = get_notification()
    notification = freight.enter_notification(notification_value)
    expect(notification).to_have_value(str(notification_value))

    page.mouse.wheel(0, 500)
    
    carrier_value = get_carrier()
    carrier = freight.select_carrier(carrier_value)
    expect(carrier).to_have_value(carrier_value)

    transit_days_value = get_transit_days()
    transit_days = freight.enter_transit_days(transit_days_value)
    expect(transit_days).to_have_value(str(transit_days_value))

    page.mouse.wheel(0, 300)
    
    page.get_by_role("button", name="Review & Submit →").click()

    page.mouse.wheel(0, -300)

    












    







    
