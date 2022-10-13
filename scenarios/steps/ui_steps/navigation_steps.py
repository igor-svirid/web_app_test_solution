import allure

from framework.utils.browser_utils import Browser
from scenarios.models.device import Device


class NavigationSteps:
    """Class to describe navigation steps"""
    @staticmethod
    def navigate_to_page_for_device(page_url: str, device: Device) -> None:
        """
        Navigates to provided page for the device
        :args:
         - page_url: device specific page urls [Monitoring, Diagnostics]
         - device: device to open page for
        """
        url = f'{page_url}{device.address}'
        with allure.step(f"Navigating to [{url}]"):
            Browser.navigate_to(url)
