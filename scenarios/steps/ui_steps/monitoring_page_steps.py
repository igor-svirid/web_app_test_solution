from typing import Union

import allure

from framework.utils.assert_utils import Asserts
from scenarios.models.device import Device
from scenarios.pages.monitoring_page import MonitoringPage


class MonitoringPageSteps:
    """Class to describe steps on the Monitoring page"""

    def __init__(self, monitoring_page: MonitoringPage):
        """Initialize steps class instance"""
        self.page = monitoring_page

    def assert_pin_parameters_are_correct(self, pin_number: int, expected_duty: int, expected_frequency: int) -> None:
        """
        Asserts correct Pin duty and frequency are displayed
        :arg:
         - pin_number: number of Pin to check
         - expected_duty: duty expected for Pin
         - expected_frequency: frequency expected for Pin
        """
        with allure.step(f"Asserting parameters for Pin {pin_number}"):
            actual_duty = self.page.get_pin_duty(pin_number)
            actual_frequency = self.page.get_pin_frequency(pin_number)
            checks = [
                (expected_duty == actual_duty, f'Expected duty: {expected_duty}. Actual duty: {actual_duty}'),
                (expected_frequency == actual_frequency,
                 f'Expected frequency: {expected_frequency}. Actual frequency: {actual_frequency}')
            ]
            Asserts.soft_assert(checks)

    def enter_duty_for_pin(self, pin_number: int, duty: Union[str, int]) -> None:
        """
        Set duty for Pin
        :args:
         - pin_number: number of Pin to set duty for
         - duty: value of duty to set
        """
        with allure.step(f"Entering duty for Pin {pin_number}"):
            self.page.set_pin_duty(pin_number, duty)

    def select_frequency_for_pin(self, pin_number: int, frequency: Union[str, int]) -> None:
        """
        Set frequency for Pin
        :args:
         - pin_number: number of Pin to set duty for
         - frequency: value of frequency to set
        """
        with allure.step(f"Selecting frequency for Pin {pin_number}"):
            self.page.select_pin_frequency(pin_number, frequency)

    def save_pin_parameters(self, pin_number: int) -> None:
        """
        Save parameters for Pin
        :arg:
         - pin_number: number of Pin to save parameters for
        """
        with allure.step(f"Saving parameters for Pin {pin_number}"):
            self.page.save_pin_parameters(pin_number)

    def wait_for_pin_parameters_to_be(self, pin_number: int, duty: Union[str, int], frequency: Union[str, int]) -> None:
        """
        Waiting for Pin parameters to display changed values
        :args:
         - pin_number: number of Pin to wait having expected parameters for
         - frequency: value of frequency to display
         - duty: value of duty to display
        """
        with allure.step(f"Waiting parameters for Pin {pin_number} to be changed"):
            self.page.wait_for_pin_duty_to_change(pin_number, duty)
            self.page.wait_for_pin_frequency_to_change(pin_number, frequency)

    def get_new_random_frequency_for_pin(self, pin_number: int) -> int:
        """
        Generates random frequency not equal to displayed
        :args:
         - pin_number: number of Pin to generate frequency for
        :returns: integer value of new frequency
        """
        with allure.step(f"Getting new random frequency Pin {pin_number}"):
            return int(Device.generate_random_frequency_not_equal_to(
                self.page.get_pin_frequency(pin_number),
                self.page.get_available_frequencies_for_pin(pin_number)
                )
            )

    def get_new_random_duty_for_pin(self, pin_number: int) -> int:
        """
        Generates random duty not equal to displayed
        :args:
         - pin_number: number of Pin to generate duty for
        :returns: integer value of new duty
        """
        with allure.step(f"Getting new random frequency for Pin {pin_number}"):
            return Device.generate_random_duty_not_equal_to(self.page.get_pin_duty(pin_number))

    @allure.step("Asserting if all forms are displayed on Monitoring page")
    def assert_all_forms_displayed(self) -> None:
        """
        Asserts if all forms displayed
        """
        Asserts.soft_assert([(is_displayed, f'Form {form_name} is not displayed')
                             for form_name, is_displayed
                             in self.page.are_forms_displayed().items()])

    @allure.step("Asserting if invalid duty cannot be saved for pin on Monitoring page")
    def assert_invalid_duty_cannot_be_saved_for_pin(self, pin_number, expected_duty) -> None:
        """
        Asserts duty invalid duty cannot be saved for specified pin
        :args:
         - pin_number: number of pin to check
         - expected_duty: expected pin duty to display
        """
        actual_duty = self.page.get_pin_duty(pin_number)
        check_duty_value = (expected_duty == actual_duty, f"Expected duty {expected_duty}. Actual {actual_duty}")
        check_error_message_displayed = (self.page.is_duty_error_message_displayed_for_pin(pin_number),
                                         f"Error message for pin {pin_number} is not displayed")
        Asserts.soft_assert([check_duty_value, check_error_message_displayed])
