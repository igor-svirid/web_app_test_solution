from datetime import datetime

import allure
from pytest import fixture, hookimpl

from framework.browser_factory.browsers_config import BrowsersConfig
from framework.config.config import Config
from framework.logger.logger import Logger
from framework.utils.browser_utils import Browser
from framework.utils.os_utils import OsUtils
from scenarios.helpers.requests_helper import ApiRequestsHelper
from scenarios.models.device import Device
from scenarios.pytest_custom_options import CustomOptions
from scenarios.recources.page_urls import PageUrls


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call) -> None:
    """Hook to set base logging and saving outcome"""

    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)
    if rep.when == 'setup':
        Logger.info(f'Test [{item.name}] started')
    if call.excinfo:
        Logger.error(''.join([str(element) for element in call.excinfo.traceback]))
    if rep.when == 'teardown':
        Logger.info(f'Test [{item.name}] finished')


@fixture()
def base_ui(request) -> None:
    """
    Fixture for base UI actions: start and quit Browser
    Saves screenshot for last opened page for failed tests
    """
    Browser(request.config.getoption(CustomOptions.BROWSER))
    yield
    if request.node.rep_call.failed:
        directory = Config.SCREENSHOTS_DIRECTORY_TEMPLATE.format(
            OsUtils.get_current_work_dir(), datetime.now().strftime(Config.FOLDER_NAME_FORMAT))
        screenshot_name = f"{request.node.name}_{datetime.now().strftime(Config.SCREENSHOT_NAME_FORMAT)}.png"
        OsUtils.create_directory_if_not_exist(directory)

        Browser.save_screenshot(f'{directory}/{screenshot_name}')
        allure.attach.file(
            f'{directory}/{screenshot_name}', name=screenshot_name, attachment_type=allure.attachment_type.PNG)
    Browser.quit_driver()


@fixture
def ui_with_base_page(base_ui) -> None:
    """Fixture with navigating to start page in tests"""
    Browser.navigate_to(PageUrls.DEVICES)
    yield


@fixture(params=Device.get_list_of_devices_from_response(ApiRequestsHelper.get_all_devices()))
def device(request) -> Device:
    """Fixture to get list of Device objects for tests parametrization"""
    return request.param


def pytest_addoption(parser) -> None:
    """Adding custom option for pytest"""
    parser.addoption(
        CustomOptions.BROWSER,
        action="store",
        default=BrowsersConfig.CHROME,
        help="Browser to run"
    )

