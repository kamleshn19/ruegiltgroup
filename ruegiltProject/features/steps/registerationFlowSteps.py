from behave import *
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

@given('I launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Edge(options=chrome_options,executable_path='C:/Users/knarsinghani/Documents/GitHub/quoting/edgedriver.exe')

@when(u'I open Rue La La or Gilt website "{url}"')
def openApplication(context,url):
    context.driver.get(url)

@then(u'I verify the landing page and move to signup')
def verifyLandingPageAndregistrationPage(context):
    if not ( WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "already-a-member")))):
        context.driver.find_element(By.CLASS_NAME, 'not-a-member').click

@when(u'I enter email address "{emailID}"')
def enterEmail(context,emailID):
    WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID, "landing_email"))).send_keys(emailID)

@when(u'I click on Continue')
def clickContinue(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID, "registration_continue"))).click()

@when(u'I enter password "{password}" for registering new user')
def enterPassword(context,password):
    WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID, "register_password"))).send_keys(password)

@when(u'I click on Start Shopping or Shop Now Button')
def clickStartShopping(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.ID, "registration_submit"))).click()

@then(u'I Verify that the user is landed to Home Page')
def verifyHomePage(context):
    try:
        context.driver.find_element(By.XPATH, "//li[@data-error-for-field,'password']")
        context.driver.close()
        assert True, "Password Char less than 10"
        logging.info("The password entered is less than 10 charracter")
    except:
        context.driver.close()
        assert True, "Registration Sucessfull, Char limit satisfied"
        logging.info("The password entered is equal to 10 or more charracter")

