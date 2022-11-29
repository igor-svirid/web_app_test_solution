class BrowsersConfig:
    """Class with configs for supported browsers"""
    CHROME = "chrome"
    CHROME_CAPABILITIES: dict[str: str] = {
        "browserName": "chrome",
        "browserVersion": "latest"
    }
    CHROME_OPTIONS: list[str] = ["--start-maximized", "--headless"]
