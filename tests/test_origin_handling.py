import random

import pytest
from playwright.sync_api import expect
from pages.origin_handling_page import OriginHandlingPage
from test_data.origin_handling_data import (
    get_currency,
    get_end_date,
    get_fee_name,
    get_basis,
    get_CISS_Fee,
    get_CMR_Fee,
    get_start_date,
    get_terminal,
    get_Export_Licence_Fee,
    get_FOB_Tax,
    get_Origin_Carrier_Fee,
    get_Origin_Customs,
    get_fixed_rate_unit,
    get_rate,
    get_UOM,
)

@pytest.mark.order(2)
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

    page.get_by_role("button", name="Next - Fixed Fees").click()

    Export_Documents_value = random.randint(50,100)

    Export_Documents= origin_handling.enter_Export_Documents(Export_Documents_value)

    expect(Export_Documents).to_have_value(str(Export_Documents_value))

    page.screenshot(
        path="screenshots/origin_handling_density.png",
        full_page=True
    )

    uom = get_UOM()
    basis = get_basis()

    origin_handling.select_uom_and_basis(uom, basis)

    origin_customs_value = get_Origin_Customs()
    origin_customs = origin_handling.enter_Origin_Customs(origin_customs_value)
    expect(origin_customs).to_have_value(str(origin_customs_value))
    origin_handling.select_Origin_Customs_uom_and_basis(get_UOM(), get_basis())

    cmr_fee_value = get_CMR_Fee()
    cmr_fee = origin_handling.enter_CMR_Fee(cmr_fee_value)
    expect(cmr_fee).to_have_value(str(cmr_fee_value))
    origin_handling.select_CMR_Fee_uom_and_basis(get_UOM(), get_basis())

    export_licence_fee_value = get_Export_Licence_Fee()
    export_licence_fee = origin_handling.enter_Export_Licence_Fee(export_licence_fee_value)
    expect(export_licence_fee).to_have_value(str(export_licence_fee_value))
    origin_handling.select_Export_Licence_Fee_uom_and_basis(get_UOM(), get_basis())

    ciss_fee_value = get_CISS_Fee()
    ciss_fee = origin_handling.enter_CISS_Fee(ciss_fee_value)
    expect(ciss_fee).to_have_value(str(ciss_fee_value))
    origin_handling.select_CISS_Fee_uom_and_basis(get_UOM(), get_basis())

    origin_carrier_fee_value = get_Origin_Carrier_Fee()
    origin_carrier_fee = origin_handling.enter_Origin_Carrier_Fee(origin_carrier_fee_value)
    expect(origin_carrier_fee).to_have_value(str(origin_carrier_fee_value))
    origin_handling.select_Origin_Carrier_Fee_uom_and_basis(get_UOM(), get_basis())

    fob_tax_value = get_FOB_Tax()
    fob_tax = origin_handling.enter_FOB_Tax(fob_tax_value)
    expect(fob_tax).to_have_value(str(fob_tax_value))
    origin_handling.select_FOB_Tax_uom_and_basis(get_UOM(), get_basis())


    page.get_by_role("button", name="Add New Fee").click()

    fee_name_value = get_fee_name()
    fee_name = origin_handling.enter_fee_name(fee_name_value)
    expect(fee_name).to_have_value(fee_name_value)

    rate_value = get_rate()
    rate = origin_handling.enter_rate(rate_value)
    expect(rate).to_have_value(str(rate_value))

    origin_handling.select_fee_uom_and_basis(get_UOM(), get_basis())

    page.screenshot(
            path="screenshots/origin_handling_fixed_fees.png",
            full_page=True
        )

    page.mouse.wheel(0, 500)

    page.get_by_role("button", name="Next - Variable Fees").click()

    page.locator("#rf-fixed").click()

    fixed_rate_unit_value = get_fixed_rate_unit()
    fixed_rate_value = get_rate()
    fixed_rate_unit, fixed_rate = origin_handling.select_fixed_rate_unit(
        fixed_rate_unit_value,
        fixed_rate_value,
    )

    expect(fixed_rate_unit).to_have_value(fixed_rate_unit_value)

    expected_fixed_rate = (
        f"{fixed_rate_value:.2f}"
        if fixed_rate_unit_value in {"VAN", "TRUCK"}
        else str(fixed_rate_value)
    )
    expect(fixed_rate).to_have_value(expected_fixed_rate)

    page.mouse.wheel(0, -500)

    page.locator("div.progress-node", has_text="4").click()

    
    document_name = origin_handling.enter_document_name("vijay")
    expect(document_name).to_have_value("vijay")
            
    page.screenshot(
    path="screenshots/origin_handling_Document_Name.png",
    full_page=True
    )
    
    page.locator('input[type="file"]').set_input_files(
    "C:\\Users\\NISSI266\\Downloads\\pindrop_ble_sync_report_20260731_125152.pdf"
)
    
    page.screenshot(
    path="screenshots/origin_handling_Upload.png",
    full_page=True
    )

    page.get_by_role("button", name="Add document").click()

    page.wait_for_timeout(2000)
    page.mouse.wheel(0, 500)

    page.get_by_role("button", name="Submit Rank").click()

    page.screenshot(
    path="screenshots/origin_handling_submit.png",
    full_page=True
    )

    page.get_by_role("button", name="Confirm Submit").click()

    page.wait_for_timeout(2000)

    page.screenshot(
    path="screenshots/origin_handling_Final_submit.png",
    full_page=True
    )
    






    
