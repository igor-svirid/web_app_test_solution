class Config:
    """Config class for WebUI"""
    PORT: str = 5585
    BASE_URL: str = f'http://localhost:{PORT}/'
    WEBSOCKET_BASE: str = f'ws://localhost:{PORT}/'
