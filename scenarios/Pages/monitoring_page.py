from typing import Union

from scenarios.enums.parameter_units import ParameterUnits
from scenarios.pages.base_device_page import BaseDevicePage
from scenarios.pages.forms.g_form import GForm
from scenarios.pages.forms.pin_form import PinForm


class MonitoringPage(BaseDevicePage):
    """Class to describe Monitoring Page"""

    def __init__(self):
        """Initialize Monitoring page for device"""
        super().__init__(name='Monitoring')
        self.forms = {
            2: PinForm(2),
            3: PinForm(3),
            'G': GForm()
        }

    def get_pin_duty(self, pin_number: int) -> int:
        """
        Gets Pin duty value
        :arg:
         - pin_number: number of Pin
        :returns: integer representation of duty value by specified Pin
        """
        return self.forms[pin_number].get_parameter(ParameterUnits.DUTY)

    def get_pin_frequency(self, pin_number: int) -> int:
        """
        Gets Pin frequency value
        :arg:
         - pin_number: number of Pin
        :returns: integer representation of frequency value by specified Pin
        """
        return self.forms[pin_number].get_parameter(ParameterUnits.FREQUENCY)

    def set_pin_duty(self, pin_number: int, duty: Union[str, int]) -> None:
        """
        Sets duty value for Pin
        :args:
         - pin_number: number of Pin
         - duty: value of duty that should be entered to textbox
        """
        self.forms[pin_number].set_duty(duty)

    def select_pin_frequency(self, pin_number: int, frequency: Union[str, int]) -> None:
        """
        Sets frequency value for Pin
        :args:
         - pin_number: number of Pin
         - frequency: value of frequency that should be selected in dropdown
        """
        self.forms[pin_number].select_frequency(frequency)

    def save_pin_parameters(self, pin_number: int) -> None:
        """
        Clicks Save button for Pin
        :arg:
         - pin_number: number of Pin
        """
        self.forms[pin_number].save_pin_parameters()

    def wait_for_pin_duty_to_change(self, pin_number: int, value: Union[str, int]) -> None:
        """
        Waits for Pin duty value equals to specified value
        :args:
         - pin_number: number of Pin
         - value: value that should get duty for Pin
        """
        self.forms[pin_number].wait_for_parameter_to_change(ParameterUnits.DUTY, value)

    def wait_for_pin_frequency_to_change(self, pin_number: int, value: Union[str, int]) -> None:
        """
        Waits for Pin frequency value equals to specified value
        :args:
         - pin_number: number of Pin
         - value: value that should get frequency for Pin
        """
        self.forms[pin_number].wait_for_parameter_to_change(ParameterUnits.FREQUENCY, value)

    def get_available_frequencies_for_pin(self, pin_number: int) -> list[str]:
        """
        Gets available frequencies values in Pin frequency dropdown
        :arg:
         - pin_number: number of Pin
        :returns: list of string representations for pin frequency dropdown
        """
        return self.forms[pin_number].get_available_frequencies()

    def are_forms_displayed(self) -> dict[str: bool]:
        """
        Checks if all forms displayed
        :returns: dict with form name as key and bool result of form visibility as value
        """
        return {form.name: form.is_displayed() for form in self.forms.values()}

    def is_duty_error_message_displayed_for_pin(self, pin_number: int) -> bool:
        """
        :arg:
        - pin_number: number of pin to check
        :return: True if duty error message is displayed for pin
        """
        return self.forms[pin_number].is_duty_error_message_for_pin_displayed()
