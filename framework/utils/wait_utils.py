from typing import Union

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as exp_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework.config.config import Config
from framework.utils.browser_utils import Browser


class WaitUtils:
    """Class to handle web driver waits"""

    @classmethod
    def get_webdriver_wait_with_timeout(cls, timeout=Config.TIMEOUTS['explicit_timeout']) -> WebDriverWait:
        """
        Sets timeout and return WebDriverWait
        :optional arg:
         - timeout: int -> timeout value in seconds
        :returns: WebDriverWait
        """
        return WebDriverWait(Browser.get_driver(), timeout)

    @classmethod
    def wait_for_element_visible(cls, locator: tuple[By, str]) -> WebElement:
        """
        Waits for visibility of an element and returns it
        :arg:
         - locator: tuple of By and locator value
        :returns: WebElement if visible
        :raises: TimeoutException if element is not visible
        """
        return cls.get_webdriver_wait_with_timeout().until(
            exp_conditions.visibility_of_element_located(locator=locator))

    @classmethod
    def wait_for_element_present(cls, locator: tuple[By, str]) -> WebElement:
        """
        Waits for presence of an element and returns it
        :arg:
         - locator: tuple of By and locator value
        :returns: WebElement if present
        :raises: TimeoutException if element is not present in the DOM
        """
        return cls.get_webdriver_wait_with_timeout().until(exp_conditions.presence_of_element_located(locator=locator))

    @classmethod
    def wait_for_element_contains_text(cls, locator: tuple[By, str], text: str) -> WebElement:
        """
        Waits for an element text to contain specified string and returns it
        :args:
         - locator: tuple of By and locator value
         - text: string that needs to be in element's text
        :returns: WebElement if specified string is in Text of element
        :raises: TimeoutException if element is doesn't contain specified string
        """
        return cls.get_webdriver_wait_with_timeout().until(
            exp_conditions.text_to_be_present_in_element(locator=locator, text_=text))

    @classmethod
    def wait_for_element_to_be_clickable(cls, element: Union[WebElement, tuple[By, str]]) -> WebElement:
        """
        Waits for an element to be clickable and returns it
        :arg:
         - element: WebElement or tuple of By and locator value for element to locate
        :returns: WebElement if element is clickable
        :raises: TimeoutException if element is not clickable
        """
        return cls.get_webdriver_wait_with_timeout().until(exp_conditions.element_to_be_clickable(element))
