from typing import Union

from selenium.webdriver.common.by import By

from framework.elements.button import Button
from scenarios.elements.web_ui_dropdown import WebUiDropdown
from framework.elements.label import Label
from scenarios.pages.base_device_page import BaseDevicePage


class DiagnosticsPage(BaseDevicePage):
    """Class to describe Diagnostics Page"""

    REPORT_DROPDOWN_LOC: tuple[By, str] = (By.XPATH, "//span[@class='ant-select-selection-search']//input")
    LOAD_REPORT_BTN_LOC: tuple[By, str] = (By.XPATH, '//main//button')
    REPORT_LOC: tuple[By, str] = (By.XPATH, '//main//pre')

    def __init__(self):
        """Initialize Diagnostics page for device"""
        super().__init__(name='Diagnostics')
        self.report_dropdown = WebUiDropdown(self.REPORT_DROPDOWN_LOC, "Report dropdown")
        self.load_report_btn = Button(self.LOAD_REPORT_BTN_LOC, "Load Report")
        self.report_label = Label(self.REPORT_LOC, "Loaded report")

    def select_report(self, report_name: Union[str, int]) -> None:
        """
        Select report in dropdown
        :arg:
         - report_name: string or integer representation of report name
        """
        self.report_dropdown.select_value(report_name)

    def load_report(self) -> None:
        """Clicks Load Report button"""
        self.load_report_btn.click()

    def is_report_loaded(self) -> bool:
        """
        Checks if report displayed
        :returns: True if report is displayed on the page
        """
        return self.report_label.is_displayed()

    def get_report(self) -> str:
        """
        Gets report text on the page
        :returns: string representation of the report text on the page
        """
        return self.report_label.get_text()
