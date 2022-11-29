from selenium.webdriver.common.by import By

from framework.elements.label import Label
from framework.elements.link import Link


class BasePage:
    """Class to describe base page"""

    PAGE_LOC_TEMPLATE: str = "//h2[contains(text(),'{}')]"
    TITLE_LOC: tuple[By, str] = (By.XPATH, '//h2')
    TEST_UI_LINK_LOC: tuple[By, str] = (By.XPATH, '//header/a')

    def __init__(self, name):
        """
        Initialize object of a page
        :arg:
         - name: name of a page
        """
        self.name = name
        self.title_label = Label((By.XPATH, self.PAGE_LOC_TEMPLATE.format(name)), 'Title')
        self.test_ui_link = Link(self.TEST_UI_LINK_LOC, 'Test UI')

    @property
    def title(self) -> str:
        """
        Gets page title
        :returns: page title text
        """
        return self.title_label.get_text()

    def is_page_opened(self) -> bool:
        """
        Checks if page opened
        :returns: True if page opened
        """
        return self.title_label.is_displayed()

    def wait_for_page_opened(self) -> None:
        """Waits for page to be opened"""
        self.title_label.wait_for_displayed()

    def click_device_page_link(self) -> None:
        """Clicks Test UI link"""
        self.test_ui_link.click()
