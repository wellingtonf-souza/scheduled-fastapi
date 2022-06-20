import logging
import sys
from datetime import datetime

class Logger(logging.Logger):
    def __init__(self, level=logging.INFO, filename = 'src/logs/server.log'):
        self.level = level

        logging.getLogger('apscheduler').propagate = False
        self.logger = logging.getLogger()
        self.logger.setLevel(self.level)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)-8s %(message)s'))

        file_handler = logging.FileHandler(filename)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def info(self, message, *args, **kwargs):
        content = self._generate_content(message = message)
        self.logger.info(content)

    def error(self, message, *args, **kwargs):
        content = self.__generate_content(message = message)
        self.logger.error(content)

    def debug(self, message, *args, **kwargs):
        content = self.__generate_content(message = message)
        self.logger.debug(content)

    def warn(self, message, *args, **kwargs):
        content = self.__generate_content(message = message)
        self.logger.warn(content)

    def _generate_content(self, message):
        frame = sys._getframe(2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = frame.f_code.co_filename
        funcName = frame.f_code.co_name
        lineno = frame.f_lineno
        return {
            'timestamp': timestamp, 'message': message, 'filename': filename, 'funcName': funcName, 'lineno': lineno
        }
