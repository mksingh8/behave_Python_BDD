from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helper.helper_base import HelperFunc


def get_browser(browser):
    if browser == 'chrome':
        option = Options()
        option.add_argument('--no-sandbox')
        option.add_experimental_option('useAutomationExtension', False)
        return HelperFunc(webdriver.Chrome(executable_path="/home/manish/Documents/browsers/chromedriver",
                                           options=option))
