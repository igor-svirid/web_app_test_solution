class LoggerConfig:
    """Logger configuration file"""
    LOG_DIRECTORY_TEMPLATE: str = '{}/results/logs'
    LOG_FORMAT: str = '%(asctime)s - %(levelname)s - %(message)s'
    LOG_TIME_FORMAT: str = '%H:%M:%S'
    LOG_FILE_NAME_FORMAT: str = '%Y_%m_%d_%H_%M'
