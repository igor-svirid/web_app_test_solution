import allure

from framework.utils.assert_utils import Asserts
from framework.utils.browser_utils import Browser
from scenarios.models.device import Device
from scenarios.pages.base_device_page import BaseDevicePage
from scenarios.pages.base_page import BasePage
from scenarios.pages.devices_page import DevicesPage
from scenarios.pages.diagnostics_page import DiagnosticsPage
from scenarios.recources.page_urls import PageUrls
from scenarios.steps.ui_steps.diagnostics_page_steps import DiagnosticsPageSteps
from scenarios.steps.ui_steps.navigation_steps import NavigationSteps


class CommonSteps:
    """Class for function that perform similar steps"""
    @staticmethod
    def navigate_to_diagnostics_page_and_generate_report_for_device(device, report_name=None):
        """
        Navigates to diagnostics page for the specified device and generates selected report
        :arg:
         - device: device for which diagnostics page should be open
        :optional arg:
         - report_name: Union[str, int] -> report name to be generated. If none, report won't be selected
        """
        NavigationSteps.navigate_to_page_for_device(PageUrls.DIAGNOSTICS, device)
        diagnostics_page = DiagnosticsPage()
        diagnostics_page_steps = DiagnosticsPageSteps(diagnostics_page)
        diagnostics_page_steps.load_report_by_name(report_name)
        return diagnostics_page

    @staticmethod
    def assert_device_page_opened_upon_click_test_ui_link(page: BasePage) -> None:
        """
        Clicks Test UI link and asserts Device page opened
        :arg:
         - Union[MonitoringPage, DiagnosticsPage] -> current page
        """
        page.click_device_page_link()
        device_page = DevicesPage()
        Asserts.assert_true(device_page.is_page_opened(), f"{page.__class__.__name__} opened")

    @staticmethod
    def assert_correct_device_page_for_device_opened(device: Device, page: BaseDevicePage) -> None:
        """
        Asserts page title to verify page for correct device opened
        :arg:
         - device: Device to verify opened page for
         - page: [Monitoring, Diagnostics] -> opened page object
        """
        with allure.step(f"Asserting {page.name} page for [{device.address}:{device.name}] opened"):
            page.wait_for_page_opened()
            current_url = Browser.get_url()
            expected_url =\
                f"{PageUrls.DIAGNOSTICS if isinstance(page, DiagnosticsPage) else PageUrls.MONITORING}{device.address}"

            checks = [
                (page.is_page_opened(), f"{page.name} page didn't open"),
                (page.is_device_page_title_correct(device),
                 f"Actual title is {page.title}."
                 f" Expected title to contain name [{device.name}] and address [{device.address}]"),
                (expected_url == current_url, f"Expected url [{expected_url}]. Actual [{current_url}]")
            ]
            Asserts.soft_assert(checks)
