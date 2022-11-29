import json
from typing import Union, Any

from requests import Response

from framework.utils.api_utils import ApiRequests
from scenarios.recources.api_urls import ApiUrls


class ApiRequestsHelper:
    """Helper class for sending specific requests to api"""

    @staticmethod
    def get_all_devices() -> Response:
        """
        Gets response for GET /devices request
        :returns: requests.Response for GET /devices request
        """
        return ApiRequests.get(ApiUrls.DEVICES)

    @staticmethod
    def get_report_for_device(address: str, report_name: Union[str, int]) -> Response:
        """
        Gets response for GET /report request for a device
        :args:
         - address: string representation of device address in HEX format
         - report_name: name of the report
        :returns: requests.Response for GET /devices request
        """
        return ApiRequests.get(ApiUrls.REPORT, address=address, repId=report_name)

    @staticmethod
    def update_device_info(**params) -> Response:
        """
        Gets response for PATCH /devices request for a device
        :arg:
         - params: required address and at least one of [freq1, duty1, freq2, duty2]
        """
        return ApiRequests.patch(ApiUrls.DEVICES, **params)

    @staticmethod
    def get_websocket_parameters_for_device_by_type(address: str, message_type: str) -> list[Any]:
        """
        Gets websocket message containing message_type
        :args:
         - address: string representation of device address in HEX format
         - message_type: type of message that expected [freqs or duties]
         :returns: list of parameters
        """
        message = ApiRequests.get_websocket_message_with_text(f'{ApiUrls.MONITORING}{address}', message_type)
        json_message = json.loads(message)
        return json_message[message_type]
