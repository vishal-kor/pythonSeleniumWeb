import re
import string
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class ElementCodex:

    def __init__(self,codexFile):
        self.whitespace_pattern = re.compile('^\s+$')
        self.newline_only_pattern = re.compile('\n')
        self.comment_pattern = re.compile('^\#.*')
        self.elements_dictionary = {}
        self.codex_file = codexFile
        self.read_codex(self.codex_file)

    def line_is_comment(self, line):
        if(self.comment_pattern.match(line)):
            return True
        else:
            return False

    def line_is_blank(self, line):
        if self.whitespace_pattern.match(line) or \
           self.newline_only_pattern.match(line):
            return True
        else:
            return False

    def read_codex(self, input_file):
        codex_file_path = os.path.abspath(os.path.join("/home/vishal/forAppiumDemo/demo/newAndroidWebDemo/resources/",input_file))
        codex_filestream = open(codex_file_path, 'r')
        for line in codex_filestream:
            # if the line is empty, skip
            if self.line_is_blank(line):
                continue
            # if the line starts with # it is a comment
            if self.line_is_comment(line):
                continue
            self.add_codex_entry(line)


    def add_codex_entry(self, line):
        split_on_dq = string.split(line, '"')
        result_count = len(split_on_dq)
        # we expect 3 fields: 1 is everything befoerhte start of the idstring,
        # one is the idstring itself, one is everything after the idstring
        if result_count < 3:
            print("Looking for idstring(s). We did not get the " +
                  "expected >=3 elements, we got " + str(result_count))
            print(line)
            return
        else:
            # without quotes
            idstringlist = split_on_dq[1::2]
            # everything that came before the first string,
            # split by whitespace
            pre_string_fields = string.split(split_on_dq[0])
            result_count = len(pre_string_fields)
            if result_count < 2:
                print("Looking for name and ident. We did not get the " +
                      "expected >=2 elements, we got " + str(result_count))
                print(line)
                return
            else:
                name = pre_string_fields[0]
                ident = pre_string_fields[1]
                self.elements_dictionary[name] = [ident,idstringlist[0]]

    def get_codex(self, codex_name):
        result_codex = self.elements_dictionary[codex_name]
        return result_codex

    def getElement(self,driver,codex_details):
        '''
        :param driver: appium webdriver
        :param codex_details: contains attribute type and attribute id
        :return:  element if element found otherwise False
        '''
        if codex_details[0] == "id":
            return driver.find_element_by_id(codex_details[1])
        elif codex_details[0] == "name":
            return driver.find_element_by_name(codex_details[1])
        elif codex_details[0] == "class":
            return driver.find_element_by_class_name(codex_details[1])
        elif codex_details[0] == "xpath":
            return driver.find_element_by_xpath(codex_details[1])
        else:
            return False


    def isElementLocated(self,codex_details):
        '''
        :param codex_details: contains attribute type and attribute id
        :return: element if element located otherwise False
        '''
        if codex_details[0] == "id":
            return expected_conditions.presence_of_element_located(
            (By.ID, codex_details[1]))
        elif codex_details[0] == "class":
            return expected_conditions.presence_of_element_located(
            (By.CLASS_NAME, codex_details[1]))
        elif codex_details[0] == "xpath":
            return expected_conditions.presence_of_element_located(
            (By.XPATH, codex_details[1]))
        else:
            return False

