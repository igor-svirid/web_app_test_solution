class Config:
    """Framework configs"""
    TIMEOUTS: dict[str: int] = {
        "explicit_timeout": 10
    }
    FOLDER_NAME_FORMAT: str = "%d_%m_%Y"
    SCREENSHOT_NAME_FORMAT: str = "%d_%m_%Y_%H_%M_%S"
    SCREENSHOTS_DIRECTORY_TEMPLATE: str = '{}/results/screenshots/{}'
