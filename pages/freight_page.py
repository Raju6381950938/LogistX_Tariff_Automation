from playwright.sync_api import Page


class freightPage:

    def __init__(self, page: Page):
        self.page = page

    def get_page_title(self):
        return self.page.title()

    def wait_for_page(self):
        self.page.wait_for_timeout(5000)
