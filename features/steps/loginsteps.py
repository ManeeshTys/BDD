import time
from behave import *
from selenium import webdriver
@given('I launch chrome browser')
def launchbrowser(context):
    #context.driver = webdriver.Chrome("C:/Users/gmaneesh/Drivers/chromedriver.exe")
    context.driver = webdriver()

@when('I open orange HRM homepage')
def openhomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)


@when('enter username "{user}" and password "{pwd}"')
def entercredentials(context,user,pwd):
    context.driver.find_element("xpath", "//input[@name='username']").send_keys(user)
    context.driver.find_element("xpath", "//input[@name='password']").send_keys(pwd)



@when('click on login button')
def step_impl(context):
    context.driver.find_element("xpath", "//button[@type='submit']").click()
    time.sleep(5)


@then('user must successfully login to the dashboard')
def step_impl(context):
    try:
        text = context.driver.find_element("xpath","//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
    except:
        context.driver.close()
        assert False, "Test case failed"
        print(text)
    if text == 'Dashboard':
        context.driver.close()
        assert True, "Test passed"
    