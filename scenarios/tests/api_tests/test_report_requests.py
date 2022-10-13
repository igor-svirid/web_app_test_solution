import allure
from pytest import mark
from requests import codes

from framework.utils.assert_utils import Asserts
from scenarios.recources.error_messages import ErrorMessage
from scenarios.recources.test_data import TestData
from scenarios.steps.api_steps.report_steps import ReportSteps


@mark.api
@allure.title("Check report can be got by api")
@mark.parametrize('report_name', TestData.AVAILABLE_REPORT_TYPES)
def test_report_generated_for_device(report_name, device):
    report = ReportSteps.get_report_for_device(device.address, report_name, codes.ok)
    with allure.step("Asserting report body is not empty"):
        Asserts.not_empty(report, f"Report [{report_name}] body")
    with allure.step("Asserting report body has no error"):
        Asserts.not_equal(ErrorMessage.REPORT_MISSING_ERROR_MESSAGE, report, f"Report [{report_name}] message")


@allure.title("Check error message is received in response if specified report invalid")
@mark.parametrize('report_name', TestData.INVALID_PARAMETER_VALUES)
def test_error_message_received_if_specified_report_invalid(device, report_name):
    if isinstance(report_name, int) and report_name > 0:
        expected_message = ErrorMessage.REPORT_MISSING_ERROR_MESSAGE
    else:
        expected_message = ErrorMessage.INVALID_TYPE_MESSAGE_TEMPLATE.format(TestData.REPORT_ID_PARAMETER_NAME)
    ReportSteps.get_report_for_device(device.address, report_name, codes.not_found, expected_message)


@allure.title("Check error message is received in response if report is not specified")
def test_error_message_received_if_report_is_not_specified(device):
    expected_message = ErrorMessage.SPECIFY_PARAMETER_MESSAGE_TEMPLATE.format(TestData.REPORT_ID_PARAMETER_NAME)
    ReportSteps.get_report_for_device(
        device.address, expected_code=codes.bad_request, expected_message=expected_message)


@allure.title("Check error message is received in response if address is not specified")
@mark.parametrize('report_name', TestData.AVAILABLE_REPORT_TYPES)
def test_error_message_received_if_address_is_not_specified(report_name):
    expected_message = ErrorMessage.SPECIFY_PARAMETER_MESSAGE_TEMPLATE.format(TestData.ADDRESS_PARAMETER_NAME)
    ReportSteps.get_report_for_device(
        report_name=report_name, expected_code=codes.bad_request, expected_message=expected_message)


@allure.title("Check error message is received in response if specified address invalid")
@mark.parametrize('report_name', TestData.AVAILABLE_REPORT_TYPES)
@mark.parametrize('address', TestData.DEVICE_INVALID_ADDRESSES)
def test_error_message_received_if_invalid_address_specified(report_name, address):
    ReportSteps.get_report_for_device(address, report_name, codes.bad_request, ErrorMessage.INVALID_ADDRESS_API_MESSAGE)
