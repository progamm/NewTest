from behave import *
from selenium import webdriver
import time

@given("Launch Chrome Browser")
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")


@when("Open Pointzi home Page")
def step_impl(context):
    context.driver.get("https://dashboard.pointzi.com/login")
    time.sleep(5)




@step("Enter all details")
def step_impl(context):
    context.driver.find_element_by_xpath("//input[@type='email']").send_keys('mazhar@yahoo.com')
    time.sleep(2)
    context.driver.find_element_by_xpath("//input[@name='password']").send_keys('maz123456')
    time.sleep(1)


@then("click Login")
def step_impl(context):
    context.driver.find_element_by_xpath("//button[normalize-space()='Login']").click()
    time.sleep(1)


@then("Login to Dashboard")
def step_impl(context):
        context.driver.get("https://dashboard.pointzi.com/tutorial")
        time.sleep(10)

