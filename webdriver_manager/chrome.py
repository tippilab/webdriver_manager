import os

from webdriver_manager.driver import ChromeDriver
from webdriver_manager.manager import DriverManager
from webdriver_manager import utils


class ChromeDriverManager(DriverManager):
    def __init__(self, version=None,
                 os_type=utils.os_type()):
        DriverManager.__init__(self)
        # there is no driver with 64 bit
        if os_type == "win64":
            os_type = "win32"
        self.driver = ChromeDriver(version=version,
                                   os_type=os_type)

    def install(self):
        bin_file = self._file_manager.download_driver(self.driver)
        os.chmod(bin_file.path, 0o755)
        return bin_file.path
