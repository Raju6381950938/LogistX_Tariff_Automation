from playwright.sync_api import Page


class OriginHandlingPage:

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
        terminal_field = self.page.get_by_label("terminal")

        terminal_field.fill(str(terminal))

        return terminal_field

    def enter_start_date(self, start_date):
        start_date_field = self.page.get_by_label("Start Date")

        start_date_field.fill(str(start_date))

        return start_date_field


    def enter_end_date(self, end_date):
        end_date_field = self.page.get_by_label("End Date")

        end_date_field.fill(str(end_date))

        return end_date_field


    def enter_Export_Documents(self, export_documents):
        export_documents_field = self.page.locator("#ff-export_documents")

        export_documents_field.fill(str(export_documents))

        return export_documents_field

    def select_uom(self, uom):
        uom_dropdown = self.page.locator("#ff-export_documents-unit")
        uom_dropdown.select_option(label=uom)

        return uom_dropdown

    def select_basis(self, basis):
        basis_dropdown = self.page.locator("#ff-export_documents-basis")
        basis_dropdown.select_option(label=basis)

        return basis_dropdown

    def select_uom_and_basis(self, uom, basis):
        self.select_uom(uom)

        if uom == "kilogram":
            self.select_basis(basis)    

    def enter_Origin_Customs(self, origin_customs):
        origin_customs_field = self.page.locator("#ff-origin_customs")
        origin_customs_field.scroll_into_view_if_needed()
        origin_customs_field.fill(str(origin_customs))
        return origin_customs_field

    def select_Origin_Customs_uom_and_basis(self, uom, basis):
        origin_customs_uom_dropdown = self.page.locator("#ff-origin_customs-unit")
        origin_customs_uom_dropdown.scroll_into_view_if_needed()
        origin_customs_uom_dropdown.select_option(label=uom)

        if uom == "kilogram":
            origin_customs_basis_dropdown = self.page.locator("#ff-origin_customs-basis")
            origin_customs_basis_dropdown.scroll_into_view_if_needed()
            origin_customs_basis_dropdown.select_option(label=basis)

    def enter_CMR_Fee(self, cmr_fee):
        cmr_fee_field = self.page.locator("#ff-cmr")
        cmr_fee_field.scroll_into_view_if_needed()
        cmr_fee_field.fill(str(cmr_fee))
        return cmr_fee_field

    def select_CMR_Fee_uom_and_basis(self, uom, basis):
        cmr_fee_uom_dropdown = self.page.locator("#ff-cmr-unit")
        cmr_fee_uom_dropdown.scroll_into_view_if_needed()
        cmr_fee_uom_dropdown.select_option(label=uom)

        if uom == "kilogram":
            cmr_fee_basis_dropdown = self.page.locator("#ff-cmr-basis")
            cmr_fee_basis_dropdown.scroll_into_view_if_needed()
            cmr_fee_basis_dropdown.select_option(label=basis)

    def enter_Export_Licence_Fee(self, export_licence_fee):
        export_licence_fee_field = self.page.locator("#ff-export_licence")
        export_licence_fee_field.scroll_into_view_if_needed()
        export_licence_fee_field.fill(str(export_licence_fee))
        return export_licence_fee_field

    def select_Export_Licence_Fee_uom_and_basis(self, uom, basis):
        export_licence_fee_uom_dropdown = self.page.locator("#ff-export_licence-unit")
        export_licence_fee_uom_dropdown.scroll_into_view_if_needed()
        export_licence_fee_uom_dropdown.select_option(label=uom)

        if uom == "kilogram":
            export_licence_fee_basis_dropdown = self.page.locator("#ff-export_licence-basis")
            export_licence_fee_basis_dropdown.scroll_into_view_if_needed()
            export_licence_fee_basis_dropdown.select_option(label=basis)

    def enter_CISS_Fee(self, ciss_fee):
        ciss_fee_field = self.page.locator("#ff-origin_ciss_fee")
        ciss_fee_field.scroll_into_view_if_needed()
        ciss_fee_field.fill(str(ciss_fee))
        return ciss_fee_field

    def select_CISS_Fee_uom_and_basis(self, uom, basis):
        ciss_fee_uom_dropdown = self.page.locator("#ff-origin_ciss_fee-unit")
        ciss_fee_uom_dropdown.scroll_into_view_if_needed()
        ciss_fee_uom_dropdown.select_option(label=uom)

        if uom == "kilogram":
            ciss_fee_basis_dropdown = self.page.locator("#ff-origin_ciss_fee-basis")
            ciss_fee_basis_dropdown.scroll_into_view_if_needed()
            ciss_fee_basis_dropdown.select_option(label=basis)

    def enter_Origin_Carrier_Fee(self, origin_carrier_fee):
        origin_carrier_fee_field = self.page.locator("#ff-origin_carrier_fee")
        origin_carrier_fee_field.scroll_into_view_if_needed()
        origin_carrier_fee_field.fill(str(origin_carrier_fee))
        return origin_carrier_fee_field

    def select_Origin_Carrier_Fee_uom_and_basis(self, uom, basis):
        origin_carrier_fee_uom_dropdown = self.page.locator("#ff-origin_carrier_fee-unit")
        origin_carrier_fee_uom_dropdown.scroll_into_view_if_needed()
        origin_carrier_fee_uom_dropdown.select_option(label=uom)

        if uom == "kilogram":
            origin_carrier_fee_basis_dropdown = self.page.locator("#ff-origin_carrier_fee-basis")
            origin_carrier_fee_basis_dropdown.scroll_into_view_if_needed()
            origin_carrier_fee_basis_dropdown.select_option(label=basis)

    def enter_FOB_Tax(self, fob_tax):
        fob_tax_field = self.page.locator("#ff-fob_tax")
        fob_tax_field.scroll_into_view_if_needed()
        fob_tax_field.fill(str(fob_tax))
        return fob_tax_field

    def select_FOB_Tax_uom_and_basis(self, uom, basis):
        fob_tax_uom_dropdown = self.page.locator("#ff-fob_tax-unit")
        fob_tax_uom_dropdown.scroll_into_view_if_needed()
        fob_tax_uom_dropdown.select_option(label=uom)

        if uom == "kilogram":
            fob_tax_basis_dropdown = self.page.locator("#ff-fob_tax-basis")
            fob_tax_basis_dropdown.scroll_into_view_if_needed()
            fob_tax_basis_dropdown.select_option(label=basis)

    
    def enter_fee_name(self, fee_name):
        fee_name_field = self.page.locator("#oh-additional-fee-name-1")
        fee_name_field.scroll_into_view_if_needed()
        fee_name_field.fill(str(fee_name))

        return fee_name_field

    def enter_rate(self, rate):
        rate_field = self.page.locator("#oh-additional-fee-amount-1")
        rate_field.scroll_into_view_if_needed()
        rate_field.fill(str(rate))

        return rate_field

    def select_fee_uom_and_basis(self, uom, basis):
        fee_uom_dropdown = self.page.locator("#oh-additional-fee-unit-1")
        fee_uom_dropdown.scroll_into_view_if_needed()
        fee_uom_dropdown.select_option(label=uom)

        if uom == "kilogram":
            fee_basis_dropdown = self.page.locator("#oh-additional-fee-basis-1")
            fee_basis_dropdown.scroll_into_view_if_needed()
            fee_basis_dropdown.select_option(label=basis)
    
    def select_fixed_rate_unit(self, unit, rate):
        fixed_rate_unit = self.page.locator("#handling-fixed-unit-0-type")
        fixed_rate_unit.scroll_into_view_if_needed()
        fixed_rate_unit.select_option(label=unit)

        rate_field = self.page.locator("#handling-fixed-unit-0-rate")
        rate_field.fill(str(rate))

        if unit in ["VAN", "TRUCK"]:
            self.page.locator("#handling-fixed-unit-0-vehicle-id").fill("01")
            self.page.locator("#handling-fixed-unit-0-max-weight-kg").fill("1200")
            self.page.locator("#handling-fixed-unit-0-max-cubic-capacity-m3").fill("14")
            self.page.locator("#handling-fixed-unit-0-max-standard-pallets").fill("6")
            self.page.locator("#handling-fixed-unit-0-max-euro-pallets").fill("8")

        return fixed_rate_unit, rate_field
    
    def enter_document_name(self, document_name):
        document_name_field = self.page.get_by_placeholder("e.g. Rate sheet")
        document_name_field.fill(document_name)

        return document_name_field