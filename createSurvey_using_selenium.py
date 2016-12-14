# Import question builder class
from library.question_types import QuestionBuilder
import time
import pytest
# Importing setlog file for logging purpose
from library.setlog import Logger
loggerObj = Logger()
logger = loggerObj.setLogger("logs")

# Testcase 1 : This testcase will sign-in and create survey with 4 questions
def test_singInWithCreateSurveyAndSignOut(setUpWeb,codexFile):
    driver = setUpWeb
    driver.get("http://surveymonkey.com")
    driver.maximize_window()
    QB = QuestionBuilder(driver,codexFile)
    logger.info("Executing Testcase 1...........")
    logger.info("Signing in..........")

    # User sign in
    rv = QB.userSignIn()
    assert rv

    # create survey
    rv = QB.createSurvey("survey 1")
    if rv == False:
        logger.info("survey creation failed")
        QB.tearDown()
        assert rv
    else:
        logger.info("Survey created")

    # Question 1 : Single text question
    rv = QB.web_addSingleTextTypeOfQueUsingAddNextQueButton("Surveymonkey web automaton demo")
    if rv is False:
        logger.info("Failed to add single text type of question")
        QB.tearDown()
        assert rv
    else:
        logger.info("Added single text type of question")

    # Question 2 : Multiple choice question
    rv = QB.web_addMultipleChoiceTypeOfQueUsingAddNextQueButton("How often do you use SurveyMonkey?")
    if rv is False:
        logger.info("Failed to add multiple choice type of question")
        QB.tearDown()
        assert rv
    else:
        logger.info("Added multiple choice type of question")

    # Question 3 : Dropdown question
    rv = QB.web_addDropDownTypeOfQueUsingAddNextQueButton("Did you get meaningful data from survey analysis?")
    if rv is False:
        logger.info("Failed to add Dropdown type of question")
        QB.tearDown()
        assert rv
    else:
        logger.info("Added Dropdown type of question")

    #sign out
    logger.info("Signing out..........")
    rv = QB.signOutUserLogin()
    if rv is False:
        logger.info("Testcase 1 failed")
        assert rv
    else:
        logger.info("successfully signout")
        logger.info("Testcase 1 passed")
        QB.tearDown()
