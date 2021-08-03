from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@given(u'launch chrome browser')
def step_impl(context):
    option = Options()
    option.add_argument('--no-sandbox')
    option.add_experimental_option('useAutomationExtension', False)
    context.driver = webdriver.Chrome(executable_path="/home/manish/Documents/browsers/chromedriver", options=option)


@when(u'open google home page')
def step_impl(context):
    context.driver.get("https://www.google.com")


@then(u'verify logo present on the page')
def step_impl(context):
    status = context.driver.find_element_by_css_selector("#hplogo").is_displayed()
    assert status


@then(u'close browser')
def step_impl(context):
    context.driver.close()
