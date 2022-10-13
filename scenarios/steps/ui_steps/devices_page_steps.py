import allure

from framework.utils.assert_utils import Asserts
from scenarios.enums.device_table_columns import TableColumn
from scenarios.models.device import Device
from scenarios.pages.base_device_page import BaseDevicePage
from scenarios.pages.devices_page import DevicesPage
from scenarios.pages.diagnostics_page import DiagnosticsPage
from scenarios.pages.monitoring_page import MonitoringPage


class DevicesPageSteps:
    """Class to describe steps on the Devices page"""

    TABLE_DEVICE_PARAMS: list[str] = ['name', 'type', 'address']

    def __init__(self, devices_page: DevicesPage):
        """Initialize steps class instance"""
        self.page = devices_page

    def open_page_for_device(self, device: Device, column: TableColumn) -> BaseDevicePage:
        """
        Click button for specified column to open appropriate device page
        :args:
         - device: device to open page for
         - column: column to open page for [Monitoring, Diagnostics]
        :returns: [Monitoring, Diagnostics] -> opened page for specified device
        """
        with allure.step(f"Moving to [{column.name}] page for [{device.address}:{device.name}] device"):
            self.page.click__button_for_device_by_column(device.address, column)
            return DiagnosticsPage() if column == TableColumn.DIAGNOSTICS else MonitoringPage()

    def assert_device_info(self, device: Device) -> None:
        """
        Assert displayed device parameter [Name, Address, Type]
        :arg:
         - device: Device object to check parameters
        """
        with allure.step(f"Asserting parameters for [{device.address}:{device.name}] device"):
            expected_values = dict(zip(self.TABLE_DEVICE_PARAMS, [device.name, device.type, device.address]))

            actual_values = dict(zip(self.TABLE_DEVICE_PARAMS,
                                     [self.page.get_device_parameter_info(device.address, TableColumn.NAME),
                                      self.page.get_device_parameter_info(device.address, TableColumn.TYPE),
                                      self.page.get_device_parameter_info(device.address, TableColumn.ADDRESS)]))

            Asserts.soft_are_equal(expected_values, actual_values)
