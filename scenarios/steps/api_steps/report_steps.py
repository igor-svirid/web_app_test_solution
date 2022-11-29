import allure

from framework.utils.assert_utils import Asserts
from scenarios.helpers.requests_helper import ApiRequestsHelper


class ReportSteps:
    """Steps to perform api actions with reports"""
    @staticmethod
    def get_report_for_device(address=None, report_name=None, expected_code=None, expected_message=None) -> str:
        """
        Gets specified report for specified device address
        :optional arg:
         - address: Union[str, int] -> device address for which report is needed
         - report_name: Union[str, int] -> name of the report required
         - expected_code: requests.status_codes -> expected code from api response. If specified - assert performs
        :returns: string representation of the specified report for the device
        """
        with allure.step(f"Getting [{report_name}] report for device with [{address}] address"):
            response = ApiRequestsHelper.get_report_for_device(address, report_name)
            actual_message = response.text.strip()
            if expected_code:
                with allure.step(f"Asserting status code is [{expected_code}]"):
                    Asserts.assert_equal(expected_code, response.status_code)
            if expected_message:
                with allure.step(f"Asserting response message to be {expected_message}"):
                    Asserts.assert_equal(expected_message, actual_message)
            return actual_message
