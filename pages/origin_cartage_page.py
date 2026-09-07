from playwright.sync_api import Page


class OriginCartagePage:

    def __init__(self, page: Page):
        self.page = page

    def get_page_title(self):
        return self.page.title()

    def wait_for_page(self):
        self.page.wait_for_timeout(5000)

    def select_currency(self, currency):
        currency_field = self.page.locator("#sel-currency")

        currency_field.click()

        self.page.get_by_text(
            currency,
            exact=True
        ).click()

        return currency_field

    def enter_density(self, density):
        density_field = self.page.get_by_label("Density")

        density_field.fill(str(density))

        return density_field

    def enter_departure_terminal(self, departure_terminal):
        departure_terminal_field = self.page.get_by_label(
            "Departure terminal (OPT)"
        )

        departure_terminal_field.fill(str(departure_terminal))

        return departure_terminal_field

    def enter_start_date(self, start_date):
        start_date_field = self.page.locator("#in-start")
        start_date_field.fill(start_date)

        return start_date_field

    def enter_end_date(self, end_date):
        end_date_field = self.page.locator("#in-end")
        end_date_field.fill(end_date)

        return end_date_field

    def enter_fuel_surcharge(self, fuel_surcharge):
        fuel_surcharge_field = self.page.locator("#in-fuel-surcharge-pct")
        fuel_surcharge_field.fill(str(fuel_surcharge))
    
        return fuel_surcharge_field

    def enter_notification(self, notification):
        notification_field = self.page.locator("#in-fuel-surcharge-notification")
        notification_field.fill(str(notification))

        return notification_field

    def select_city(self, city):
        city_dropdown = self.page.get_by_label("City (OPT)")
        city_dropdown.select_option(city)

        return city_dropdown
    

    def select_from_postcode(self, from_postcode):
        from_postcode_field = self.page.get_by_label(
            "From postcode", exact=True
        )
        from_postcode_field.fill(str(from_postcode))
        self.page.get_by_role(
            "option", name=str(from_postcode), exact=True
        ).click()

        return from_postcode_field

    def select_to_postcode(self, to_postcode):
        to_postcode_field = self.page.get_by_label("To postcode", exact=True)
        to_postcode_field.fill(str(to_postcode))
        self.page.get_by_role(
            "option", name=str(to_postcode), exact=True
        ).click()

        return to_postcode_field

    def enter_toll_fee(self, toll_fee):
        toll_fee_field = self.page.locator("#z1-toll-fee")
        toll_fee_field.fill(str(toll_fee))

        return toll_fee_field

    def select_unit(self, unit):
        unit_field = self.page.locator("#z1-toll-fee-unit")
        unit_field.select_option(label=unit)

        return unit_field

    def enter_booking_deadline(self, booking_deadline):
        booking_deadline_field = self.page.locator("#z1-booking-deadline")
        booking_deadline_field.fill(booking_deadline)

        return booking_deadline_field

    def enter_timeline(self, timeline):
        timeline_field = self.page.locator("#z1-timeline")
        timeline_field.fill(str(timeline))

        return timeline_field

    def select_flat_rate(self):
        flat_rate_button = self.page.locator("#crf-flat")
        flat_rate_button.click()

        return flat_rate_button

    def enter_base_rate(self, base_rate):
        base_rate_field = self.page.locator("#z1-flat-base")
        base_rate_field.fill(str(base_rate))

        return base_rate_field

    def enter_minimum_rate(self, minimum_rate):
        minimum_rate_field = self.page.locator("#z1-flat-min")
        minimum_rate_field.fill(str(minimum_rate))

        return minimum_rate_field

    def enter_rate_per_kg(self, rate_per_kg):
        rate_per_kg_field = self.page.locator("#z1-flat-per-kg")
        rate_per_kg_field.fill(str(rate_per_kg))

        return rate_per_kg_field

    def select_charge_type(self, charge_type):
        charge_type_field = self.page.locator("#z1-flat-per-kg-basis")
        charge_type_field.select_option(value=charge_type)

        return charge_type_field

    def enter_document_name(self, document_name):
        document_name_field = self.page.get_by_placeholder("e.g. Rate sheet")
        document_name_field.fill(document_name)

        return document_name_field
    
    