import os
from configparser import ConfigParser

from helper.helper_web import get_browser


def before_all(context):
    config = ConfigParser()
    # print(os.path.join(os.getcwd(), 'setup.cfg'))
    setup_file = os.path.join(os.getcwd(), 'setup.cfg')
    config.read(setup_file)

    # Reading the browser type from the configuration file
    helper_funct = get_browser(config.get('Environment', 'Browser'))
    context.driver = helper_funct


def after_all(context):
    context.driver.close()



