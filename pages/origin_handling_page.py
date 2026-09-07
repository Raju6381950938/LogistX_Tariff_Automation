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

