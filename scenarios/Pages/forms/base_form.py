from selenium.webdriver.common.by import By

from framework.elements.label import Label


class BaseForm:
    """Base form class"""
    HEADER_LOC_TEMPLATE: str = "//div[@class='ant-card-head-title' and text()='{}']"

    def __init__(self,  name: str):
        """
        Initialization of BaseForm
        :arg:
         - name: title of the form
        """
        self.name = name
        self.form_header = Label((By.XPATH, self.HEADER_LOC_TEMPLATE.format(name)), f'{name} form header')

    def is_displayed(self) -> bool:
        """
        Checks if form displayed
        :returns: True if form is displayed
        """
        return self.form_header.is_displayed()
