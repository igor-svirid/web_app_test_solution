import allure
from pytest import mark

from scenarios.enums.device_table_columns import TableColumn
from scenarios.pages.devices_page import DevicesPage
from scenarios.recources.test_data import TestData
from scenarios.steps.ui_steps.common_steps import CommonSteps
from scenarios.steps.ui_steps.devices_page_steps import DevicesPageSteps


@mark.ui
@allure.title("Check appropriate page opens for a devices by clicking table button")
@mark.parametrize('table_page_button', TestData.DEVICE_PAGE_BUTTON_COLUMNS)
def test_appropriate_device_page_opens_for_device_by_table_button(ui_with_base_page, device, table_page_button):
    opened_page = DevicesPageSteps(DevicesPage()).open_page_for_device(device, TableColumn.MONITORING)
    CommonSteps.assert_correct_device_page_for_device_opened(device, opened_page)


@mark.ui
@allure.title("Check device parameters at the Device page")
def test_device_parameters(ui_with_base_page, device):
    DevicesPageSteps(DevicesPage()).assert_device_info(device)
