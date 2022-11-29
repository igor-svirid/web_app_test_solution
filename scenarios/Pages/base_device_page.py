from scenarios.models.device import Device
from scenarios.pages.base_page import BasePage


class BaseDevicePage(BasePage):
    """Class to describe base page specific to device"""

    DEVICE_PAGE_TITLE_TEMPLATE: str = '{} {} / {}'

    def is_device_page_title_correct(self, device: Device) -> bool:
        """
        Checks if page title matching device
        :arg:
         - device: device for which page has to be opened
        :returns: True if page title matching the device
        """
        return self.title == self.DEVICE_PAGE_TITLE_TEMPLATE.format(self.name, device.name, device.address)
