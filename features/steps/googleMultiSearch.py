from behave import *
from selenium.webdriver.common.keys import Keys


@then(u'enter text "{searchTxt}" and hit enter')
def step_impl(context, searchTxt):
    # context.driver.find_element_by_name("q").send_keys(searchTxt, Keys.RETURN)
    context.driver.find_by_name("q").send_keys(searchTxt, Keys.RETURN)


@then(u'verify the page title has Google Search')
def step_impl(context):
    # assert "Google Search" in context.driver.get_title()
    assert "Google Search" in context.driver.title


