import allure

from scenarios.helpers.requests_helper import ApiRequestsHelper
from scenarios.models.device import Device


class WebsocketSteps:
    """Steps to perform api actions with websocket messages"""

    @staticmethod
    def get_params_for_device(device: Device, param: str) -> list[int]:
        """
        Gets list of frequencies from websocket by device
        :arg:
         - device: Device object to request params
         - param: parameters to receive in message
        :returns: list of specified parameters
        """
        with allure.step(f"Getting frequencies for [{device.address}:{device.name}] device"):
            return ApiRequestsHelper.get_websocket_parameters_for_device_by_type(device.address, param)
