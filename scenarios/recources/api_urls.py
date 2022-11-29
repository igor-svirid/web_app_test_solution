from scenarios.recources.config import Config


class ApiUrls:
    """Class with specific api urls"""
    DEVICES: str = f'{Config.BASE_URL}devices'
    REPORT: str = f'{Config.BASE_URL}report'
    MONITORING: str = f'{Config.WEBSOCKET_BASE}start_monitoring/'
