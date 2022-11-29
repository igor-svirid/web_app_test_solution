import allure
from pytest import mark

from scenarios.pages.diagnostics_page import DiagnosticsPage
from scenarios.recources.error_messages import ErrorMessage
from scenarios.recources.page_urls import PageUrls
from scenarios.recources.test_data import TestData
from scenarios.steps.api_steps.device_steps import DeviceSteps
from scenarios.steps.api_steps.report_steps import ReportSteps
from scenarios.steps.ui_steps.common_steps import CommonSteps
from scenarios.steps.ui_steps.diagnostics_page_steps import DiagnosticsPageSteps
from scenarios.steps.ui_steps.navigation_steps import NavigationSteps


@mark.ui
@allure.title("Check correct report generates at the Diagnostics page")
@mark.parametrize('report_name', TestData.AVAILABLE_REPORT_TYPES)
def test_report_with_correct_values_generated(base_ui, report_name, device):
    expected_report = ReportSteps.get_report_for_device(device.address, report_name)
    diagnostic_page = CommonSteps.navigate_to_diagnostics_page_and_generate_report_for_device(report_name, device)
    DiagnosticsPageSteps(diagnostic_page).assert_report_with_correct_info_loaded(expected_report)


@mark.ui
@allure.title("Check report with correct columns and lines generates at the Diagnostics page")
@mark.parametrize('report_name', TestData.AVAILABLE_REPORT_TYPES)
def test_correct_report_type_generated(base_ui, device, report_name):
    expected_report = ReportSteps.get_report_for_device(device.address, report_name)
    diagnostic_page = CommonSteps.navigate_to_diagnostics_page_and_generate_report_for_device(device, report_name)
    DiagnosticsPageSteps(diagnostic_page).assert_correct_report_type_loaded(expected_report)


@mark.ui
@allure.title("Check error message displayed when report is not selected at the Diagnostics page")
def test_error_message_displayed_if_report_is_not_selected(base_ui, device):
    diagnostic_page = CommonSteps.navigate_to_diagnostics_page_and_generate_report_for_device(device)
    DiagnosticsPageSteps(diagnostic_page).assert_error_message_displayed(
        ErrorMessage.INVALID_TYPE_MESSAGE_TEMPLATE.format(TestData.REPORT_ID_PARAMETER_NAME))


@mark.ui
@allure.title("Check Devices page opened clicking Test UI link at the Diagnostics page")
def test_devices_pages_opens_from_diagnostics_page_clicking_test_ui_link(base_ui):
    device = DeviceSteps.get_random_device()
    NavigationSteps.navigate_to_page_for_device(PageUrls.DIAGNOSTICS, device)
    CommonSteps.assert_device_page_opened_upon_click_test_ui_link(DiagnosticsPage())
