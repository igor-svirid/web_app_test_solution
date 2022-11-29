from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from framework.browser_factory.browsers_config import BrowsersConfig
from framework.logger.logger import Logger


class BrowserFactory:
    """Class to set browser version and settings"""

    @staticmethod
    def get_browser(browser=BrowsersConfig.CHROME) -> webdriver:
        """
        Initialize instance of specified browser
        For now only chrome is supported
        :optional arg:
         - browser: str -> browser name to start
        """
        if browser.lower() == BrowsersConfig.CHROME:
            Logger.info("Driver chrome is initialized")
            options = BrowsersConfig.CHROME_OPTIONS
            capabilities = BrowsersConfig.CHROME_CAPABILITIES
            chrome_options = webdriver.ChromeOptions()

            if options:
                for option in options:
                    chrome_options.add_argument(option)
            if capabilities:
                for capability in list(capabilities.items()):
                    chrome_options.set_capability(*capability)

            return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        else:
            Logger.error(f"Browser {browser} is not initialized")
            raise NotImplementedError(f"Browser {browser}  is not supported")
