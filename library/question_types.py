from element_waits import Waits
from element_codexes import ElementCodex
import time

class QuestionBuilder():
    def __init__(self,driver,codexFile):
        self.driver = driver
        self.WO = Waits(self.driver,codexFile+"_codexes.txt")
        self.ECO = ElementCodex(codexFile+"_codexes.txt")


    def createSurvey(self,question_title):
        '''
        It will create survey with given title
        :param question_title:  survey title
        :return: returns True if survey created successfully
        '''
        rv = self.waitForElement("createSurvey")
        if rv is False:
            return rv
        ele = self.getWebElement("createSurvey")
        if ele is not False:
            ele.click()
        else:
            return ele
        rv = self.waitForElement("createNewSurvey")
        if rv is False:
            return rv
        ele = self.getWebElement("createNewSurvey")
        if ele is not False:
            ele.click()
        else:
            return ele
        ele = self.getWebElement("createSurveyTitle")
        if ele is not False:
            ele.clear()
            ele.send_keys(question_title)
        else:
            return ele
        ele = self.getWebElement("createSurveyAfterTitleEntered")
        if ele is not False:
            ele.click()
        else:
            return ele

    def tearDown(self):
        '''
        Shutdown webdriver session
        :return: None
        '''
        self.driver.quit()

    def waitForElement(self,codex):
        '''
        Wait for element appearance
        :param codex: codex for eleement
        :return: return True if element found O.W. False
        '''
        rv = self.WO.waitUntilElementLocated(self.driver, codex)
        return rv

    def waitForCreateSurvey(self):
        '''
        Waiting for create survey button
        :return: returns true if element located O.W False
        '''
        rv = self.waitForElement("createSurvey")
        return rv

    def waitForQuestionContainer(self):
        '''
        Waiting for question container (i.e. for + button)
        :return: returns true if element located O.W False
        '''
        rv = self.waitForElement("questionTypesContainer(+)")
        return rv

    def getWebElement(self,codex):
        '''
        Used to return web element object
        :param codex: codex for web element
        :return: returns element O.W  False
        '''
        codex_details = self.ECO.get_codex(codex)
        ele = self.ECO.getElement(self.driver, codex_details)
        if ele != None:
            return ele
        else:
            return False


    def signOutUserLogin(self):
        '''
        signout for user
        :return: True if successfully signout O.W False
        '''
        ele = self.getWebElement("navigateUpTripleLineButton")
        if ele is not False:
            ele.click()
        else:
            return ele
        rv = self.waitForElement("wheelButtonForSignOut")
        if rv is False:
            return rv
        ele = self.getWebElement("wheelButtonForSignOut")
        if ele is not False:
            ele.click()
        else:
            return ele
        rv = self.waitForElement("signOutButton")
        if rv is False:
            return rv
        ele = self.getWebElement("signOutButton")
        if ele is not False:
            ele.click()
        else:
            return ele
        return True

    def userSignIn(self):
        '''
        user sign in
        :return: returns true if successfully signin O.W False
        '''
        rv = self.waitForElement("signInButton")
        if rv is False:
            return rv
        ele = self.getWebElement("signInButton")
        ele.click()
        ele = self.getWebElement("userNameEntry")
        ele.clear()
        ele.send_keys("InfoBeansP")
        ele = self.getWebElement("passwordEntry")
        ele.clear()
        ele.send_keys("InfoBeans!@#")
        ele = self.getWebElement("signInWithCredentials")
        ele.click()
        return True

    def verifyQuestionContainerIsOpen(self):
        rv = self.waitForElement("selectTextQuestionType")
        if rv:
            return True
        else:
            return False

    def openQuestionContainer(self,):
        rv = self.waitForQuestionContainer()
        if rv is False:
            return rv
        ele = self.getWebElement("questionTypesContainer(+)")
        ele.click()
        rv = self.verifyQuestionContainerIsOpen()
        if rv:
            return True
        else:
            return False

    def addTextTypeOfQuestion(self,question_title):
        rv = self.openQuestionContainer()
        if rv is False:
            return rv
        ele = self.getWebElement("selectTextQuestionType")
        ele.click()
        ele = self.getWebElement("textQuestionTypeTitle")
        ele.send_keys(question_title)
        rv = self.saveAnyTypeOfQuestion()
        if rv is False:
            return rv
        return True

    def web_addNextQuestionClick(self):
        rv = self.waitForElement("addNextQuestionButton")
        if rv is False:
            return rv
        ele = self.getWebElement("addNextQuestionButton")
        if ele is False:
            return False
        ele.click()

    def web_getDropdownMenuForQues(self):
        rv = self.waitForElement("changeQuesTypeDropdownButton")
        if rv is False:
            return rv
        ele = self.getWebElement("changeQuesTypeDropdownButton")
        if ele is False:
            return False
        ele.click()

    def web_addSingleTextTypeOfQueUsingAddNextQueButton(self, question_title):
        rv = self.web_addNextQuestionClick()
        if rv is False:
            return rv
        rv = self.web_getDropdownMenuForQues()
        if rv is False:
            return rv
        ele = self.getWebElement("selectSingleTextQueUsingDropdown")
        ele.click()
        ele = self.getWebElement("enterQuesTitle")
        ele.send_keys(question_title)
        rv = self.saveAnyTypeOfQuestion()
        if rv is False:
            return rv
        return True

    def web_addMultipleChoiceTypeOfQueUsingAddNextQueButton(self, question_title):
        time.sleep(3)
        rv = self.web_addNextQuestionClick()
        if rv is False:
            return rv
        rv = self.waitForElement("enterQuesTitle")
        if rv is False:
            return rv
        ele = self.getWebElement("enterQuesTitle")
        ele.send_keys(question_title)
        ele = self.getWebElement("multipleChoiceQueRow1")
        ele.send_keys("Regularly")
        ele = self.getWebElement("multipleChoiceQueRow2")
        ele.send_keys("Sometimes")
        ele = self.getWebElement("multipleChoiceQueRow3")
        ele.send_keys("Never Tried")
        rv = self.saveAnyTypeOfQuestion()
        if rv is False:
            return rv
        return True

    def web_addDropDownTypeOfQueUsingAddNextQueButton(self, question_title):
        time.sleep(3)
        rv = self.web_addNextQuestionClick()
        if rv is False:
            return rv
        rv = self.waitForElement("enterQuesTitle")
        if rv is False:
            return rv
        ele = self.getWebElement("enterQuesTitle")
        ele.send_keys(question_title)
        ele = self.getWebElement("dropDownQueTypeRow1")
        ele.send_keys("Yes")
        ele = self.getWebElement("dropDownQueTypeRow2")
        ele.send_keys("No")
        rv = self.saveAnyTypeOfQuestion()
        if rv is False:
            return rv
        return True

    def addCommentBoxTypeOfQuestion(self,question_title):
        rv = self.openQuestionContainer()
        if rv is False:
            return rv
        ele = self.getWebElement("selectCommentBoxQuestionType")
        ele.click()
        ele = self.getWebElement("commentBoxQuestionTypeTitle")
        ele.send_keys(question_title)
        rv = self.saveAnyTypeOfQuestion()
        if rv is False:
            return rv
        return True

    def addDropDownQuestionTypeOfQuestion(self,question_title):
        rv = self.openQuestionContainer()
        if rv is False:
            return rv
        ele = self.getWebElement("selectDropDownQuestionType")
        ele.click()
        rv = self.waitForElement("dropDownQuestionTypeTitle")
        if rv is False:
            return rv
        ele = self.getWebElement("dropDownQuestionTypeTitle")
        ele.send_keys(question_title)
        self.hideKeyboard()
        ele = self.getWebElement("dropDownAnswerChoices1")
        ele.send_keys("Yes")
        self.hideKeyboard()
        rv = self.waitForElement("dropDownAnswerChoices2")
        if rv is False:
            return rv
        ele = self.getWebElement("dropDownAnswerChoices2")
        ele.send_keys("No")
        self.hideKeyboard()
        rv = self.saveAnyTypeOfQuestion()
        if rv is False:
            return rv
        return True

    def addMatrixRatingTypeOfQuestion(self,question_title):
        rv = self.openQuestionContainer()
        if rv is False:
            return rv
        ele = self.getWebElement("selectMatrixRatingQuestionType")
        ele.click()
        rv = self.waitForElement("matrixRatingQuestionTypeTitle")
        if rv is False:
            return rv
        ele = self.getWebElement("matrixRatingQuestionTypeTitle")
        ele.send_keys(question_title)
        ele = self.getWebElement("matrixRatingQuestionTypeRows")
        ele.click()
        rv = self.waitForElement("enterMatrixRatingRowLable1")
        if rv is False:
            return rv
        ele = self.getWebElement("enterMatrixRatingRowLable1")
        ele.clear()
        ele.send_keys("Interface")
        rv = self.waitForElement("enterMatrixRatingRowLabel2")
        if rv is False:
            return rv
        ele = self.getWebElement("enterMatrixRatingRowLabel2")
        ele.clear()
        ele.send_keys("Survey design")
        rv = self.saveAnyTypeOfQuestion()
        if rv is False:
            return rv
        rv = self.saveAnyTypeOfQuestion()
        if rv is False:
            return rv
        return True


    def hideKeyboard(self):
        self.driver.hide_keyboard()


    def saveAnyTypeOfQuestion(self):
        ele = self.getWebElement("saveQuestion")
        if ele is None:
            return False
        else:
            ele.click()
            return True

    def web_saveAnyTypeOfQuestion(self):
        ele = self.getWebElement("saveQuestion")
        if ele is None:
            return False
        else:
            ele.click()
            return True


    def previewAndTestSurvey(self):
        rv = self.waitForElement("tripleDotButtonForPreviewAndTest")
        if rv is False:
            return rv
        ele = self.getWebElement("tripleDotButtonForPreviewAndTest")
        ele.click()
        ele = self.getWebElement("selectPreviewAndTestButton")
        ele.click()
        return True








