from playwright.sync_api import Page


class FreightPage:

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

    def enter_terminal(self, terminal):
            terminal_field = self.page.locator("#departure_terminal")
            terminal_field.fill(str(terminal))
            return terminal_field

    def select_unpacking(self, unpacking):
        unpacking_field = self.page.locator("#unpacking_portcode")
        unpacking_field.select_option(value=unpacking)

        return unpacking_field

    def enter_arrival(self, arrival):
                arrival_field = self.page.locator("#arrival_terminal")
                arrival_field.fill(str(arrival))
                return arrival_field
    
    def enter_start_date(self, start_date):
            start_date_field = self.page.get_by_label("Start Date")
    
            start_date_field.fill(str(start_date))
    
            return start_date_field
    
    
    def enter_end_date(self, end_date):
            end_date_field = self.page.get_by_label("End Date")
    
            end_date_field.fill(str(end_date))
    
            return end_date_field

    def enter_terminal_fee(self, terminal_fee):
        terminal_fee_field = self.page.locator("#fr-terminal-fee-kg")
        terminal_fee_field.scroll_into_view_if_needed()
        terminal_fee_field.fill(str(terminal_fee))
        return terminal_fee_field
    
    def select_terminal_fee_uom_and_basis(self, uom, basis):
        terminal_fee_uom_dropdown = self.page.locator("#fr-terminal-fee-kg-unit")
        terminal_fee_uom_dropdown.scroll_into_view_if_needed()
        terminal_fee_uom_dropdown.select_option(label=uom)

        if uom == "kilogram":
            terminal_fee_basis_dropdown = self.page.locator("#fr-terminal-fee-kg-basis")
            terminal_fee_basis_dropdown.scroll_into_view_if_needed()
            terminal_fee_basis_dropdown.select_option(label=basis)

                
    def enter_terminal_minimum(self, terminal_minimum):
            terminal_minimum_field = self.page.locator("#fr-terminal-transfer-min")
            terminal_minimum_field.scroll_into_view_if_needed()
            terminal_minimum_field.fill(str(terminal_minimum))
            return terminal_minimum_field
        
    def select_terminal_minimum_uom_and_basis(self, uom, basis):
            terminal_minimum_uom_dropdown = self.page.locator("#fr-terminal-transfer-min-unit")
            terminal_minimum_uom_dropdown.scroll_into_view_if_needed()
            terminal_minimum_uom_dropdown.select_option(label=uom)
    
            if uom == "kilogram":
                terminal_minimum_basis_dropdown = self.page.locator("#fr-terminal-transfer-min-basis")
                terminal_minimum_basis_dropdown.scroll_into_view_if_needed()
                terminal_minimum_basis_dropdown.select_option(label=basis)

    def enter_fee(self, fee):
            fee_field = self.page.locator("#ff-additional-fee-name-1")
            fee_field.scroll_into_view_if_needed()
            fee_field.fill(str(fee))
    
            return fee_field
    
    def enter_rate(self, rate):
            rate_field = self.page.locator("#ff-additional-fee-amount-1")
            rate_field.scroll_into_view_if_needed()
            rate_field.fill(str(rate))
    
            return rate_field
    
    def select_fee_uom_and_basis(self, uom, basis):
            fee_uom_dropdown = self.page.locator("#ff-additional-fee-unit-1")
            fee_uom_dropdown.scroll_into_view_if_needed()
            fee_uom_dropdown.select_option(label=uom)
    
            if uom == "kilogram":
                fee_basis_dropdown = self.page.locator("#ff-additional-fee-basis-1")
                fee_basis_dropdown.scroll_into_view_if_needed()
                fee_basis_dropdown.select_option(label=basis)


    def enter_base_rate(self, base_rate):
               base_rate_field = self.page.locator("#fr-bp-base")
               base_rate_field.fill(str(base_rate))
               return base_rate_field

    def enter_minimum_rate(self, minimum_rate):
                   minimum_rate_field = self.page.locator("#fr-bp-min")
                   minimum_rate_field.fill(str(minimum_rate))
                   return minimum_rate_field
    
    def select_condition(self, condition):
        condition_field = self.page.locator("#fbp-condition-1")
        condition_field.scroll_into_view_if_needed()
        condition_field.select_option(label=condition)
        return condition_field


    def enter_weight(self, weight):
        weight_field = self.page.locator("#fbp-weight-1")
        weight_field.fill(str(weight))
        return weight_field

    def enter_per_kg(self, per_kg):
        per_kg_field = self.page.locator("#fbp-rate-1")
        per_kg_field.fill(str(per_kg))
        return per_kg_field

    def select_charge_type(self, charge_type):
            charge_type_field = self.page.locator("#fbp-rate-1-type")
            charge_type_field.select_option(value=charge_type)
            return charge_type_field


    def enter_fuel_surcharge(self, fuel_surcharge):
            fuel_surcharge_field = self.page.locator("#fr-fuel-rate")
            fuel_surcharge_field.scroll_into_view_if_needed()
            fuel_surcharge_field.fill(str(fuel_surcharge))
            return fuel_surcharge_field
        
    def select_fuel_surcharge_uom_and_basis(self, uom, basis):
            fuel_surcharge_uom_dropdown = self.page.locator("#fr-fuel-rate-unit")
            fuel_surcharge_uom_dropdown.scroll_into_view_if_needed()
            fuel_surcharge_uom_dropdown.select_option(label=uom)
    
            if uom == "kilogram":
                fuel_surcharge_basis_dropdown = self.page.locator("#fr-fuel-rate-basis")
                fuel_surcharge_basis_dropdown.scroll_into_view_if_needed()
                fuel_surcharge_basis_dropdown.select_option(label=basis)
                     

    def enter_notification(self, notification):
        notification_field = self.page.locator("#fr-fuel-notification")
        notification_field.fill(str(notification))
        return notification_field

    
    def select_carrier(self, carrier):
        carrier_field = self.page.locator("#fr-carrier")
        carrier_field.scroll_into_view_if_needed()
        carrier_field.select_option(label=carrier)
        return carrier_field
    

    def enter_transit_days(self, transit_days):
        transit_days_field = self.page.locator("#fr-transit-days")
        transit_days_field.fill(str(transit_days))
        return transit_days_field

    def enter_document_name(self, document_name):
             document_name_field = self.page.get_by_placeholder("e.g. Rate sheet")
             document_name_field.fill(document_name)
     
             return document_name_field

    