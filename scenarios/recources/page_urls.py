from scenarios.recources.config import Config


class PageUrls:
    """Class with specific pages' urls"""
    DEVICES: str = f'{Config.BASE_URL}#/device/'
    MONITORING: str = f'{Config.BASE_URL}#/monitoring/'
    DIAGNOSTICS: str = f'{Config.BASE_URL}#/diagnostics/'
