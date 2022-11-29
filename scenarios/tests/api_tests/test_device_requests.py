import allure
from pytest import mark
from requests.status_codes import codes

from framework.utils.assert_utils import Asserts
from scenarios.recources.error_messages import ErrorMessage
from scenarios.recources.test_data import TestData
from scenarios.steps.api_steps.device_steps import DeviceSteps


@mark.api
@allure.title("Check device list returned by api request not empty")
def test_get_devices_response():
    devices = DeviceSteps.get_all_devices(codes.ok)
    Asserts.not_empty(devices, 'Device list')


@mark.api
@allure.title("Check device parameters can be updated by api")
def test_device_parameters_can_be_updated(device):
    device.generate_new_random_parameters()
    DeviceSteps.update_device_info(device, codes.ok)

    updated_device = DeviceSteps.get_device(device.address)
    with allure.step(f"Asserting [{device.name}:{device.address}] parameters were updated"):
        Asserts.assert_equal(device, updated_device)


@mark.api
@allure.title("Check error message is received in response if incorrect parameter is sent")
@mark.parametrize('parameter', TestData.DEVICE_PATCH_PARAMETERS)
@mark.parametrize('value', TestData.INVALID_PARAMETER_VALUES)
def test_device_parameters_cant_be_updated_with_invalid_values(parameter, value):
    device_to_check = DeviceSteps.get_random_device()
    if isinstance(value, int) and value > 0:
        if parameter.startswith('duty'):
            expected_message = ErrorMessage.INVALID_DUTY_VALUE_TEMPLATE.format(parameter)
        else:
            expected_message = ErrorMessage.INVALID_FREQUENCY_VALUE_TEMPLATE.format(parameter)
    else:
        expected_message = ErrorMessage.INVALID_TYPE_MESSAGE_TEMPLATE.format(parameter)
    DeviceSteps.update_device_parameter_and_assert_message_and_status_code(
        device_to_check.address, codes.bad_request, expected_message, **{parameter: value})


@mark.api
@allure.title("Check error message is received in response if no parameters are sent")
@mark.parametrize('address', TestData.DEVICE_INVALID_ADDRESSES)
def test_error_message_received_if_parameters_for_update_are_not_sent(address, device):
    DeviceSteps.update_device_parameter_and_assert_message_and_status_code(
        device.address, codes.bad_request, ErrorMessage.SPECIFY_PARAMETERS_MESSAGE)


@mark.api
@allure.title("Check error message is received in response if address is not specified")
def test_error_message_received_if_address_in_not_sent():
    DeviceSteps.update_device_parameter_and_assert_message_and_status_code(
        address=None, expected_code=codes.bad_request,
        expected_message=ErrorMessage.SPECIFY_PARAMETER_MESSAGE_TEMPLATE.format(TestData.ADDRESS_PARAMETER_NAME))


@mark.api
@allure.title("Check error message is received in response if invalid address is specified")
@mark.parametrize('address', TestData.DEVICE_INVALID_ADDRESSES)
def test_error_message_received_if_invalid_address_is_sent(address):
    device = DeviceSteps.get_random_device()
    params = dict(zip(TestData.DEVICE_PATCH_PARAMETERS,
                      [device.pin_1_pwm_f, device.pin_2_pwm_f, device.pin_1_pwm_d, device.pin_2_pwm_d]))
    DeviceSteps.update_device_parameter_and_assert_message_and_status_code(
        address, codes.not_found, ErrorMessage.INVALID_ADDRESS_API_MESSAGE, **params)
