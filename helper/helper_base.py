from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HelperFunc(object):
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver_wait = WebDriverWait(driver, self.TIMEOUT)
        self.driver = driver

    def open_maximize_browser(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def close(self):
        self.driver.close()

#     helper function that will help to identify the web-elements
    def find_by_xpath(self, xpath):
        return self.driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_name(self, name):
        return self.driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self.driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def find_by_css_selector(self, css_selector):
        return self.driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

    def get_title(self):
        title = self.driver.title
        return title
