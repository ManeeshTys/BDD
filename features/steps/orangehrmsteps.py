import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome("C:/Users/gmaneesh/Drivers/chromedriver.exe")

@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(30)

@then('verify that the logo present on home page')
def verifyLogo(context):
    status=context.driver.find_element("xpath", "//img[@alt='company-branding']")
    #assert status is True if status

@then('close the browser')
def scloseBrowser(context):
    context.driver.close()