from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from framework.logger.logger import Logger
from framework.utils.browser_utils import Browser
from framework.utils.wait_utils import WaitUtils


class BaseElement:
    """Class realize base actions with all elements"""

    def __init__(self, locator: tuple[By, str], name: str):
        """
        Initialize base element
        :args:
         - locator: tuple(By, value)
         - name: name of element
        """
        self._type = self.__class__.__name__
        self._locator = locator
        self._name = name

    def __str__(self):
        return f'{self._type} {self._name}'

    @classmethod
    def get_list_of_elements(cls, locator_template, name_template) -> list['BaseElement']:
        """
        Collects list of elements by specified locator template
        :args:
         - locator_template: template of locator to be iterated to find elements
         - name_template: template of element name to be iterated
        :returns: List of elements inherited from BaseElement
        """
        Logger.info(f"Getting list of {cls.__class__}")
        element_number = 1
        elements = []

        while True:
            element = cls((locator_template[0], locator_template[1].format(element_number)),
                          name_template.format(element_number))
            if element.is_exist():
                elements.append(element)
                element_number += 1
            else:
                break
        return elements

    def click(self, scroll_required=True) -> None:
        """
        Waiting element to be clickable and click.
        :optional arg:
         - scroll_required: bool -> should be True if it is required to scroll to element
        """
        Logger.info(f'Clicking {self}')
        if scroll_required:
            self.scroll_to_element()
        self.wait_for_clickable().click()

    def get_text(self) -> str:
        """
        Method returns text of element
        :returns: string representation of element text
        """
        Logger.info(f'Getting {self} text')
        return self.wait_for_element_present().text

    def get_attribute_value(self, attribute_name: str) -> str:
        """
        Method returns value of an attribute for the element
        :arg:
         - attribute_name: name of the attribute
         :returns: string representation of the passed attribute
        """
        Logger.info(f'Getting {self} {attribute_name} attribute value')
        return self.wait_for_element_present().get_attribute(attribute_name)

    def scroll_to_element(self) -> None:
        """Scrolls to element by js script"""
        Logger.info(f'Scrolling to {self}')
        Browser.execute_script(Browser.SCROLL_INTO_VIEW, self.wait_for_element_present())

    def is_exist(self) -> bool:
        """
        Checks if element exist
        :returns: True if element exist or False if not
        """
        try:
            Browser.find_element(self._locator)
            return True
        except NoSuchElementException:
            return False

    def is_displayed(self) -> bool:
        """
        Checks if element visible
        :returns: True if element visible to user
        """
        Logger.info(f"Checking if {self} displayed")
        return Browser.find_element(self._locator).is_displayed()

    def wait_for_element_present(self) -> WebElement:
        """
        Wait for element to be present and returns it or False
        :returns: WebElement if present
        """
        Logger.info(f'Waiting for {self} to present')
        return WaitUtils.wait_for_element_present(self._locator)

    def wait_for_displayed(self) -> WebElement:
        """
        Wait for element to be visible and returns it or False
        :returns: WebElement if visible
        """
        Logger.info(f'Waiting for {self} displayed')
        return WaitUtils.wait_for_element_visible(self._locator)

    def wait_for_clickable(self) -> WebElement:
        """
        Wait for element to be present and returns it or False
        :returns: WebElement if element is clickable
        """
        Logger.info(f'Waiting for {self} to be clickable')
        return WaitUtils.wait_for_element_to_be_clickable(self._locator)

    def wait_for_text_contains(self, text: str) -> WebElement:
        """
        Wait for element Text contains specified string
        :arg:
         -text: value to be found in Text
        :returns: WebElement if specified string is in Text of element
        """
        Logger.info(f'Waiting for {self} to contain {text}')
        return WaitUtils.wait_for_element_contains_text(self._locator, text)
