from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@given(u'launch chrome browser')
def step_impl(context):
    # below code is commented as implemented setup.cfg, helper_web, environment and helper_base module
    # option = Options()
    # option.add_argument('--no-sandbox')
    # option.add_experimental_option('useAutomationExtension', False)
    # context.driver = webdriver.Chrome(executable_path="/home/manish/Documents/browsers/chromedriver", options=option)
    context.driver.open_maximize_browser("https://www.google.com")


@when(u'open google home page')
def step_impl(context):
    # this code is not required anymore because of implementation on helper_base
    # context.driver.get("https://www.google.com")
    pass


@then(u'verify logo present on the page')
def step_impl(context):
    # status = context.driver.find_element_by_css_selector("#hplogo").is_displayed()
    # assert status
    status = context.driver.find_by_xpath("//img[@class='lnXdpd']").is_displayed()
    assert status


@then(u'close browser')
def step_impl(context):
    # this is also not required as because before_all and after_all method would take care of it.
    # context.driver.close()
    pass
