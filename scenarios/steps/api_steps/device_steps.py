import random
from typing import Optional

import allure
from requests import status_codes

from framework.utils.assert_utils import Asserts
from scenarios.helpers.requests_helper import ApiRequestsHelper
from scenarios.models.device import Device


class DeviceSteps:
    """Steps to perform api actions with devices"""

    @staticmethod
    @allure.step("Getting list of available devices from api")
    def get_all_devices(expected_code=None) -> list[Device]:
        """
        Gets list of devices from api and asserts response code
        :optional arg:
         - expected_code: requests.status_codes -> expected code from api response. If specified - assert performs
        :returns: list of Device objects
        """
        response = ApiRequestsHelper.get_all_devices()
        if expected_code:
            with allure.step(f"Asserting status code to be {expected_code}"):
                Asserts.assert_equal(expected_code, response.status_code)
        return Device.get_list_of_devices_from_response(response)

    @staticmethod
    @allure.step("Getting random device from available devices in api")
    def get_random_device() -> Device:
        """
        Gets random device from api
        :returns: random Device object from api GET /devices request
        """
        return random.choice(DeviceSteps.get_all_devices())

    @staticmethod
    def update_device_info(device, expected_code=None) -> None:
        """
        Update devices parameters in api and asserts response code
        :arg:
         - device: device that requires to update parameters in api
        :optional arg:
         - expected_code: requests.status_codes -> expected code from api response. If specified - assert performs
        :returns: list of Device objects
        """
        with allure.step(f"Updating {device.name}"):
            response = ApiRequestsHelper.update_device_info(
                address=device.address,
                freq1=device.pin_1_pwm_f, duty1=device.pin_1_pwm_d,
                freq2=device.pin_2_pwm_f, duty2=device.pin_2_pwm_d)
            if expected_code:
                with allure.step(f"Asserting status code to be {expected_code}"):
                    Asserts.assert_equal(expected_code, response.status_code)

    @staticmethod
    def get_device(address) -> Device:
        """
        Get specified Device from api
        :arg:
         - address: address of the device to get
        :returns: Device object by specified address
        """
        with allure.step(f"Getting device with [{address}] address"):
            for device in DeviceSteps.get_all_devices():
                if device.address == address:
                    return device

    @staticmethod
    def update_device_parameter_and_assert_message_and_status_code(
            address: Optional[str], expected_code: status_codes, expected_message: str, **kwargs) -> None:
        """
        Updating parameter and asserting status code and received message
        :args:
         - address: device address to update
         - expected_code: expected status code
         - expected_message: expected response message
        :optional arg:
         - **kwargs: device parameters to update {'freq1': int, 'freq2': str, 'duty1': str, 'duty2': str}
        """
        checking_values = ['status code', 'response message']
        with allure.step(f"Updating device with [{address}] address with [{kwargs}]"):
            response = ApiRequestsHelper.update_device_info(address=address, **kwargs)
            with allure.step(f"Asserting status code and message"):
                expected_values = dict(zip(checking_values, [expected_code, expected_message]))
                actual_values = dict(zip(checking_values, [response.status_code, response.text]))
                Asserts.soft_are_equal(expected_values, actual_values)
