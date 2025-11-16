import logging

class Logger:
    def __init__(self, name="AutomationFramework"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

    def get_logger(self):
        return self.logger

