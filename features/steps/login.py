from behave import *
from selenium import webdriver
import time




@given("I launch Chrome Browser")
def step_impl(context):
       context.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")


@when("I open Pointzi home Page")
def step_impl(context):
        context.driver.get("https://dashboard.pointzi.com/login")
        time.sleep(5)


@step("Click on Register button")
def step_impl(context):
    context.driver.find_element_by_xpath("//button[normalize-space()='Register']").click()
    time.sleep(3)
    context.driver.find_element_by_xpath("//input[@type='email']").send_keys('hghggkjkh@gmail.com')
    time.sleep(1)
    context.driver.find_element_by_xpath("//input[@name='password']").send_keys('maz78954')
    time.sleep(1)
    context.driver.find_element_by_xpath("//input[@name='confirmPassword']").send_keys('maz78954')
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[normalize-space()='Next']").click()
    time.sleep(1)




@then("select from dropdwons")
def step_impl(context):
    # driver = webdriver.Chrome()
    # context.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

    ey = context.driver.find_element_by_name("role")
    ey.send_keys("Developer")
    time.sleep(2)
    ez = context.driver.find_element_by_name("number_users")
    ez.send_keys("250,000+")
    time.sleep(2)
    context.driver.find_element_by_xpath("//button[normalize-space()='Next']").click()

@then("enter  final details")
def step_impl(context):
    # context.driver.get("https://dashboard.pointzi.com/Register")

    context.driver.find_element_by_xpath("//input[@name='first_name']").send_keys('mansoor')
    time.sleep(1)
    context.driver.find_element_by_xpath("//input[@name='last_name']").send_keys('syed')
    time.sleep(1)
    context.driver.find_element_by_xpath("//input[@name='company_name']").send_keys('Pointzi')
    time.sleep(2)
    context.driver.find_element_by_xpath("//input[@name='phone']").send_keys('450768654')
    time.sleep(2)
    context.driver.find_element_by_css_selector("div.md-container").click()
    time.sleep(5)

@then("Signup")
def step_impl(context):
    context.driver.find_element_by_xpath("//button[normalize-space()='Sign up']").click()
    time.sleep(15)


