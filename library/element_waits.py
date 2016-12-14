from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from element_codexes import ElementCodex

class Waits():
    def __init__(self, driver,codexFile):
        self.driver = driver
        self.time_interval = 50
        self.ECO = ElementCodex(codexFile)

    def waitUntilElementLocated(self,driver,codex):
        '''
        It will wait until element is not located till tiem interval
        :param driver: webdriver
        :param codex: codex for element
        :return: true if element located O.W False
        '''
        codex_details = self.ECO.get_codex(codex)
        try:
            visible = self.ECO.isElementLocated(codex_details)
            WebDriverWait(driver, self.time_interval).until(visible)
        except TimeoutException:
            print "Unable to locate element"
            return False
        return True


