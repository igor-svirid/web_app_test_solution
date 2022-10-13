import random

import allure
from pytest import mark

from scenarios.pages.monitoring_page import MonitoringPage
from scenarios.recources.page_urls import PageUrls
from scenarios.recources.test_data import TestData
from scenarios.steps.api_steps.device_steps import DeviceSteps
from scenarios.steps.ui_steps.common_steps import CommonSteps
from scenarios.steps.ui_steps.monitoring_page_steps import MonitoringPageSteps
from scenarios.steps.ui_steps.navigation_steps import NavigationSteps


@mark.ui
@allure.title("Check correct device info displayed at the Monitoring Page")
@mark.parametrize('pin_number', TestData.PIN_NUMBERS)
def test_correct_device_info_displayed(base_ui, device, pin_number):
    NavigationSteps.navigate_to_page_for_device(PageUrls.MONITORING, device)
    MonitoringPageSteps(MonitoringPage()).assert_pin_parameters_are_correct(
        pin_number,
        device.get_duty_for_pin(pin_number),
        device.get_frequency_by_pin(pin_number)
    )


@mark.ui
@allure.title(f"Check device info can be updated at the Monitoring Page")
@mark.parametrize('pin_number', TestData.PIN_NUMBERS)
def test_update_pin_parameters(base_ui, pin_number):
    device_to_check = random.choice(DeviceSteps.get_all_devices())

    NavigationSteps.navigate_to_page_for_device(PageUrls.MONITORING, device_to_check)
    monitoring_page_steps = MonitoringPageSteps(MonitoringPage())

    duty_to_set = monitoring_page_steps.get_new_random_duty_for_pin(pin_number)
    frequency_to_set = monitoring_page_steps.get_new_random_frequency_for_pin(pin_number)

    monitoring_page_steps.enter_duty_for_pin(pin_number, duty_to_set)
    monitoring_page_steps.select_frequency_for_pin(pin_number, frequency_to_set)
    monitoring_page_steps.save_pin_parameters(pin_number)
    monitoring_page_steps.wait_for_pin_parameters_to_be(pin_number, duty_to_set, frequency_to_set)
    monitoring_page_steps.assert_pin_parameters_are_correct(pin_number, duty_to_set, frequency_to_set)


@mark.ui
@allure.title("Check device outputs displayed at the Monitoring Page")
def test_all_device_outputs_displayed(base_ui, device):
    NavigationSteps.navigate_to_page_for_device(PageUrls.MONITORING, device)
    monitoring_page_steps = MonitoringPageSteps(MonitoringPage())
    monitoring_page_steps.assert_all_forms_displayed()


@mark.ui
@allure.title("Check Devices page opened clicking Test UI link at the Monitoring page")
def test_devices_pages_opens_from_diagnostics_page_clicking_test_ui_link(base_ui):
    device = DeviceSteps.get_random_device()
    NavigationSteps.navigate_to_page_for_device(PageUrls.MONITORING, device)
    CommonSteps.assert_device_page_opened_upon_click_test_ui_link(MonitoringPage())


@mark.ui
@allure.title("Check duty with invalid value cannot be saved for pin")
@mark.parametrize('pin_number', TestData.PIN_NUMBERS)
@mark.parametrize('duty_value', TestData.INVALID_PARAMETER_VALUES)
def test_invalid_duty_cannot_be_saved_for_pin(base_ui, pin_number, duty_value):
    device = DeviceSteps.get_random_device()
    NavigationSteps.navigate_to_page_for_device(PageUrls.MONITORING, device)
    monitoring_page_steps = MonitoringPageSteps(MonitoringPage())
    monitoring_page_steps.enter_duty_for_pin(pin_number, duty_value)
    monitoring_page_steps.save_pin_parameters(pin_number)
    monitoring_page_steps.assert_invalid_duty_cannot_be_saved_for_pin(pin_number, device.get_duty_for_pin(pin_number))
