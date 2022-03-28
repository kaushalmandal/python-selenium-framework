import inspect
import logging


class Utils:
    def customLogger(logLevel=logging.DEBUG):
        logger_name=inspect.stack()[1][3]
        logger=logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        fh=logging.FileHandler("automation.log")
        formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s",datefmt='%Y - %m - %d %H: %M: %S')
        fh.setFormatter(fh)
        return logger
