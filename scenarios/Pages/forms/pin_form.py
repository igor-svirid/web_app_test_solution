from typing import Union

from selenium.webdriver.common.by import By

from framework.elements.button import Button
from scenarios.elements.web_ui_dropdown import WebUiDropdown
from framework.elements.label import Label
from framework.elements.textbox import Textbox
from framework.utils.string_utils import StringUtils
from scenarios.enums.parameter_units import ParameterUnits
from scenarios.pages.forms.base_form import BaseForm


class PinForm(BaseForm):
    """Class to describe Pin form"""

    FORM_LOC_TEMPLATE: str =\
        "//div[@class='ant-card-head-title' and text()='{form_name}']/ancestor::div[@class='ant-card']"
    PARAMETER_VALUE_LOC_TEMPLATE: str = "{form_locator}//article[contains(text()[2],'{parameter_units}')]"
    DUTY_TEXTBOX_LOC_TEMPLATE: str = "{form_locator}//input"
    FREQUENCY_DROPDOWN_LOC_TEMPLATE: str = "{form_locator}//span[@class='ant-select-selection-search']//input"
    SAVE_BTN_LOC_TEMPLATE: str = "{form_locator}//button"

    def __init__(self, pin_number):
        super().__init__(f'Pin {pin_number}')
        self.pin_number = pin_number
        self.locator_value = self.FORM_LOC_TEMPLATE.format(form_name=self.name)
        self.duty_textbox = Textbox(
            (By.XPATH, self.DUTY_TEXTBOX_LOC_TEMPLATE.format(form_locator=self.locator_value)), f"Duty for {self.name}")
        self.frequency_dropdown = WebUiDropdown(
            (By.XPATH, self.FREQUENCY_DROPDOWN_LOC_TEMPLATE.format(form_locator=self.locator_value)),
            f"Frequency dropdown for {self.name}")
        self.save_btn = Button(
            (By.XPATH, self.SAVE_BTN_LOC_TEMPLATE.format(form_locator=self.locator_value)), 'Save button')

    def get_parameter_label(self, units: ParameterUnits) -> Label:
        """
        Gets Label element for Pin parameter value
        :arg:
         - units: ParameterUnits enum option that matching parameter units
        :returns: Label element for parameter by specified units
        """
        return Label((
            By.XPATH,
            self.PARAMETER_VALUE_LOC_TEMPLATE.format(form_locator=self.locator_value, parameter_units=units.value)),
            f"Duty for {self.name}")

    def get_parameter(self, units: ParameterUnits) -> int:
        """
        Gets Pin parameter value
        :arg:
         - units: ParameterUnits enum option that matching parameter units
        :returns: integer representation of parameter value by specified units
        """
        return StringUtils.get_ints_from_string(self.get_parameter_label(units).get_text())

    def wait_for_parameter_to_change(self, units: ParameterUnits, value: Union[str, int]) -> None:
        """
        Waits for Pin parameter value equals to specified value
        :args:
         - units: ParameterUnits enum option that matching parameter units
         - value: value that should get parameter specified by units
        """
        self.get_parameter_label(units).wait_for_text_contains(f'{value}{units.value}')

    def set_duty(self, duty: Union[str, int]) -> None:
        """
        Sets duty value for Pin
        :args:
         - duty: value of duty that should be entered to textbox
        """
        self.duty_textbox.type(duty, keys_clear=True)

    def select_frequency(self, frequency: Union[str, int]) -> None:
        """
        Sets frequency value for Pin
        :args:
         - frequency: value of frequency that should be selected in dropdown
        """
        self.frequency_dropdown.select_value(frequency)

    def get_available_frequencies(self) -> list[str]:
        """
        Gets available frequencies values in Pin frequency dropdown
        :returns: list of string representations for pin frequency dropdown
        """
        return self.frequency_dropdown.available_options

    def save_pin_parameters(self) -> None:
        """Clicks Save button for Pin"""
        self.save_btn.click()

    def is_duty_error_message_for_pin_displayed(self) -> bool:
        """
        Checks if error message for duty displayed
        :returns: True if error message displayed
        """
        raise NotImplementedError("Add locator when the [WebUI-0042: Monitoring page: "
                                  "Duty error message is not displayed upon saving invalid values] bug will be fixed")
        return Label((By.XPATH, ""), f'{self.name} Duty error message')