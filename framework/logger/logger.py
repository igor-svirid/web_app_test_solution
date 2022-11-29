import datetime
import logging

from framework.logger.logger_config import LoggerConfig
from framework.patterns.singleton_meta import Singleton
from framework.utils.os_utils import OsUtils


class Logger(metaclass=Singleton):
    """Class for logging events"""

    __logger: logging.Logger = None

    def __init__(self):
        """Initialize instance of Logger and two handlers: FileHandler and StreamHandler"""
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logs_dir = LoggerConfig.LOG_DIRECTORY_TEMPLATE.format(OsUtils.get_current_work_dir())
        OsUtils.create_directory_if_not_exist(logs_dir)

        logger.addHandler(self.__init_handler(logging.FileHandler(
            f'{logs_dir}/{datetime.datetime.today().strftime(LoggerConfig.LOG_FILE_NAME_FORMAT)}.log')))
        logger.addHandler(self.__init_handler(logging.StreamHandler()))
        self.__logger = logger

    @classmethod
    def info(cls, message):
        """
        Add message on INFO level
        :arg:
         - message: message to be logged
        """
        Logger().__logger.info(message)

    @classmethod
    def error(cls, message):
        """
        Add message on ERROR level
        :arg:
         - message: message to be logged
        """
        Logger().__logger.error(message)

    @classmethod
    def __init_handler(cls, handler, log_level=logging.INFO) -> logging.Handler:
        """
        Specifying logging level and message format for handler
        :arg:
         - handler: logging.Handler that needs to specify level and message format
        :optional arg:
         - log_level: logging level or handler
        """
        handler.setLevel(log_level)
        handler.setFormatter(logging.Formatter(LoggerConfig.LOG_FORMAT, LoggerConfig.LOG_TIME_FORMAT))
        return handler
