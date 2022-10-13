from typing import Any

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from framework.browser_factory.browser_factory import BrowserFactory
from framework.logger.logger import Logger
from framework.patterns.singleton_meta import Singleton


class Browser(metaclass=Singleton):
    """Class to realize actions with Browser"""
    __driver: webdriver = None
    SCROLL_INTO_VIEW: str = 'arguments[0].scrollIntoView();'

    def __init__(self, browser):
        """Initialize singleton instance of Browser"""
        Logger.info("Starting browser")
        driver = BrowserFactory.get_browser(browser)
        Browser.__driver = driver

    @staticmethod
    def get_driver() -> webdriver:
        """Return instance of webdriver"""
        return Browser.__driver

    @staticmethod
    def quit_driver() -> None:
        """Closes browser and remove Browser instance from Singleton"""
        Logger.info("Closing browser")
        Browser.get_driver().quit()
        Singleton.instances.pop(Browser)

    @staticmethod
    def navigate_to(url: str) -> None:
        """
        Navigating to the passed url
        :arg:
         - url: string representation of url to be navigated to
        """
        Logger.info(f'Navigating to {url}')
        Browser.get_driver().get(url)

    @staticmethod
    def find_element(locator: tuple[By, str]) -> WebElement:
        """
        Search for element and returns it
        :arg:
         -locator: tuple with By and locator values
        :returns: selenium WebElement
        """
        Logger.info(f"Searching element by {locator} locator")
        return Browser.get_driver().find_element(*locator)

    @staticmethod
    def save_screenshot(path_to_file: str) -> None:
        """
        Saves screenshot by provided path
        :arg:
         - path_to_file: full path to file where screenshot needs to be saved
        """
        Logger.info(f'Saving screenshot to {path_to_file}')
        Browser.get_driver().save_screenshot(path_to_file)

    @staticmethod
    def get_url() -> str:
        """
        Gets current url
        :returns: string representation of current url
        """
        return Browser.get_driver().current_url

    @staticmethod
    def execute_script(script: str, *args: Any) -> None:
        """
        Executes provided js script
        :args:
         - script: js scrip to be executed
         - *args: any applicable arguments for script
        """
        Logger.info(f"Executing {script} script with {args}")
        Browser.get_driver().execute_script(script, *args)
