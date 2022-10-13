import allure
from pytest import mark

from framework.utils.assert_utils import Asserts
from scenarios.recources.test_data import TestData
from scenarios.steps.api_steps.websocket_steps import WebsocketSteps


@mark.api
@allure.title("Check device parameters can be received by websocket request")
@mark.xfail(reason="Websocket connect performs by DEC device address instead of HEX")
@mark.parametrize('parameter_with_value_names', TestData.WEBSOCKET_MESSAGES_PARAMS)
def test_websocket_frequencies_for_device(parameter_with_value_names, device):
    parameter_name = parameter_with_value_names[0]
    expected_device_parameters = [getattr(device, name) for name in parameter_with_value_names[1]]
    actual_device_parameters = WebsocketSteps.get_params_for_device(device, parameter_name)
    with allure.step(f"Asserting [{device.name}:{device.address}] {parameter_name} are correct in websocket response"):
        Asserts.assert_equal(expected_device_parameters, actual_device_parameters)
