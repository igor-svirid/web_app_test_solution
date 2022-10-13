from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.label import Label
from scenarios.enums.device_table_columns import TableColumn
from scenarios.pages.base_page import BasePage


class DevicesPage(BasePage):
    """Class to describe Device Page"""

    TABLE_CELL_TEMPLATE: str = "//tr[@data-row-key='{address}']//td[{column}]"
    CELL_BUTTON_LOC_TEMPLATE: str = f"{TABLE_CELL_TEMPLATE}//button"

    def __init__(self):
        """Initialize Device Page"""
        super().__init__(name='Device list')

    def click__button_for_device_by_column(self, address: str, column: TableColumn) -> None:
        """
        Clicks button in specified column for device in table
        :args:
         - address: string representation of device address in HEX format
         - column: TableColumn enum option for selected column
        """
        Button((By.XPATH, self.CELL_BUTTON_LOC_TEMPLATE.format(address=address, column=column)),
               f'{column.name} for {address}').click()

    def get_device_parameter_info(self, address: str, column: TableColumn) -> str:
        """
        Gets Label element in specified column for device in table
        :args:
         - address: string representation of device address in HEX format
         - column: TableColumn enum option for selected column
        :returns: string representation of parameter value for specified address and column
        """
        return Label((By.XPATH, self.TABLE_CELL_TEMPLATE.format(address=address, column=column)),
                     f'Cell {column.name} for device {address}').get_text()
