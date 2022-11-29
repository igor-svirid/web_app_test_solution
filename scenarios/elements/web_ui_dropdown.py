from typing import Union

from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.label import Label


class WebUiDropdown:
    """Class to realize actions specific to WebUI Dropdown"""
    __DROPDOWN_ELEMENT_LOCATOR_TEMPLATE: str = "//div[@id='{}']//following-sibling::div//div[@{}]"
    __LABEL: str = 'label'

    def __init__(self, locator: tuple[By, str], name: str):
        """
        Initializes dropdown specific to WebUI app
        :args:
         - locator: dropdown locator as tuple of By and locator value
         - name: name of the dropdown
        """
        self.__name = name
        self.__type = self.__class__.__name__
        self.__button_locator = (locator[0], f"{locator[1]}//ancestor::div[@class='ant-select-selector']")
        self.__button = Button(self.__button_locator, f'{self.__class__.__name__}[{self.__name}] {Button.__name__}')
        self.__box = Label(locator, name)

    @property
    def id_attribute(self) -> str:
        """
        Gets aria-controls attribute that is equal to id attribute for values of the dropdown
        :returns: aria-controls attribute value
        """
        return self.__box.get_attribute_value('aria-controls')

    @property
    def available_options(self) -> list[str]:
        """
        Return list of options specified in the dropdown
        :returns: list of string representation of the dropdown values
        """
        locator_template = f"{self.__DROPDOWN_ELEMENT_LOCATOR_TEMPLATE.format(self.id_attribute, self.__LABEL)}[{{}}]"
        self.__button.click()
        all_value_elements = Label.get_list_of_elements(
            (By.XPATH, locator_template), f"{self.__class__.__name__} select line {{}}")

        return [element.get_attribute_value(self.__LABEL) for element in all_value_elements]

    def select_value(self, value_to_select: Union[str, int]) -> None:
        """
        Opens dropdown and selects passed option by value attribute
        :arg:
         -value_to_select: dropdown option that should be selected
        """
        self.__button.click()
        element_to_select = Label(
            (By.XPATH, str.format(
                self.__DROPDOWN_ELEMENT_LOCATOR_TEMPLATE, self.id_attribute, f"{self.__LABEL}='{value_to_select}'")),
            f'Dropdown item {value_to_select}')
        element_to_select.click()
