from playwright.sync_api import expect
from pages.origin_cartage_page import OriginCartagePage



def test_origin_cartage(page_setup):

    page = page_setup

    origin_cartage = OriginCartagePage(page)

    currency = origin_cartage.select_currency("INR - Indian Rupee")
    expect(currency).to_have_value("INR - Indian Rupee")

    page.screenshot(
        path="screenshots/origin_cartage_currency.png",
        full_page=True
    )

    density = origin_cartage.enter_density(167)
    expect(density).to_have_value("167")

    page.screenshot(
        path="screenshots/origin_cartage_density.png",
        full_page=True
    )

    departure_terminal = origin_cartage.enter_departure_terminal("T1")
    expect(departure_terminal).to_have_value("T1")

    page.screenshot(
        path="screenshots/origin_cartage_Terminal.png",
        full_page=True
        )

    start_date = origin_cartage.enter_start_date("2026-09-05")
    expect(start_date).to_have_value("2026-09-05")

    page.screenshot(
        path="screenshots/origin_cartage_start_date.png",
        full_page=True
        )

    end_date = origin_cartage.enter_end_date("2026-09-06")
    expect(end_date).to_have_value("2026-09-06")
    
    page.screenshot(
        path="screenshots/origin_cartage_End_date.png",
        full_page=True
        )

    page.mouse.wheel(0, 500)

    fuel_surcharge = origin_cartage.enter_fuel_surcharge("10")
    expect(fuel_surcharge).to_have_value("10")
    
    page.screenshot(
        path="screenshots/origin_cartage_Fuel_surcharge.png",
        full_page=True
        )

    notification = origin_cartage.enter_notification("5")
    expect(notification).to_have_value("5")
        
    page.screenshot(
        path="screenshots/origin_cartage_notification.png",
        full_page=True
        )

    page.get_by_role("button", name="Next - Variable Fees →").click()

    page.screenshot(
            path="screenshots/origin_cartage_Variable.png",
            full_page=True
        )

    city = origin_cartage.select_city("chennai")
    expect(city).to_have_value("chennai")
    
    page.screenshot(
            path="screenshots/origin_cartage_city.png",
            full_page=True
        )

    from_postcode = origin_cartage.select_from_postcode("600002")
    expect(from_postcode).to_have_value("600002")
        
    page.screenshot(
              path="screenshots/origin_cartage_from_postcode.png",
              full_page=True
        )
    
    to_postcode = origin_cartage.select_to_postcode("600005")
    expect(to_postcode).to_have_value("600005")
            
    page.screenshot(
            path="screenshots/origin_cartage_to_postcode.png",
            full_page=True
            )

    toll_fee = origin_cartage.enter_toll_fee("100")
    expect(toll_fee).to_have_value("100")
            
    page.screenshot(
            path="screenshots/origin_cartage_toll_fee.png",
            full_page=True
            )

    unit = origin_cartage.select_unit("per shipment")
    expect(unit).to_have_value("shipment")
    
    page.screenshot(
            path="screenshots/origin_cartage_unit.png",
            full_page=True
        )

    booking_deadline = origin_cartage.enter_booking_deadline("09:00")
    expect(booking_deadline).to_have_value("09:00")
        
    page.screenshot(
            path="screenshots/origin_cartage_booking_deadline.png",
            full_page=True
            )
    timeline = origin_cartage.enter_timeline(5)
    expect(timeline).to_have_value("5")
    
    page.screenshot(
            path="screenshots/origin_cartage_Timeline.png",
            full_page=True
        )

    flat_rate = origin_cartage.select_flat_rate()
    expect(flat_rate).to_have_attribute("aria-pressed", "true")
    
    page.screenshot(
                path="screenshots/origin_cartage_types.png",
                full_page=True
            )

    page.mouse.wheel(0, 500)

    base_rate = origin_cartage.enter_base_rate("50")
    expect(base_rate).to_have_value("50")

    minimum_rate = origin_cartage.enter_minimum_rate("40")
    expect(minimum_rate).to_have_value("40")

    rate_per_kg = origin_cartage.enter_rate_per_kg("5")
    expect(rate_per_kg).to_have_value("5")

    page.screenshot(
                path="screenshots/origin_cartage_flat_rate.png",
                full_page=True
                )

    charge_type = origin_cartage.select_charge_type("Chargeable")
    expect(charge_type).to_have_value("Chargeable")
        
    page.screenshot(
                path="screenshots/origin_cartage_charge_type.png",
                full_page=True
            )

    page.get_by_role("button", name="Review & Submit →").click()

    page.screenshot(
                path="screenshots/origin_cartage_review_submit.png",
                full_page=True
                )

    page.mouse.wheel(0, -500)
    page.wait_for_timeout(2000)
    page.mouse.wheel(0, 1000)


    document_name = origin_cartage.enter_document_name("Raju")
    expect(document_name).to_have_value("Raju")
            
    page.screenshot(
                    path="screenshots/origin_cartage_Document_Name.png",
                    full_page=True
                )
    
    page.locator('input[type="file"]').set_input_files(
    "C:\\Users\\NISSI266\\Downloads\\pindrop_ble_sync_report_20260731_125152.pdf"
)
    
    page.screenshot(
                path="screenshots/origin_cartage_Upload.png",
                full_page=True
                )

    page.get_by_role("button", name="Add document").click()

    page.wait_for_timeout(2000)

    page.get_by_role("button", name="Submit Rank").click()

    page.screenshot(
    path="screenshots/origin_cartage_submit.png",
    full_page=True
    )                

    page.get_by_role("button", name="Confirm Submit").click()

    page.wait_for_timeout(2000)

    page.screenshot(
    path="screenshots/origin_cartage_Final_submit.png",
    full_page=True
    )

 