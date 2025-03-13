from lib.base import doc, MonitorBase, shell_cmd
import logging

class PutApp:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    def init(self):
        self._capa = 10
        self._loss = 10
        self._sdrate = 1000

    def check(self):
        self.logger.warning('Check Disk Space')
        self.logger.warning(shell_cmd('df -h'))




if __name__ == "__main__":

    mon = PutApp()
    mon.check()