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


    
    