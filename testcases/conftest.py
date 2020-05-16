from datetime import datetime

import pytest,os,json,time
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from utils.ReadJson import ReadJson

driver = None
@pytest.yield_fixture()
def setup(getBrowserName):
    global driver
    if getBrowserName== 'chrome':
        driver = webdriver.Chrome(executable_path=os.getcwd() + "/drivers/chromedriver.exe")
    elif getBrowserName== 'firefox':
        driver = webdriver.Firefox(executable_path=os.getcwd() + "/drivers/geckodriver.exe")
    driver.get(ReadJson.getConfigData('testurl'))
    driver.maximize_window()
    wait=WebDriverWait(driver,10)
    yield driver,wait
    driver.quit()
def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture
def getBrowserName(request):
    return request.config.getoption("--browser")

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = os.getcwd()+"\\reports\\"+str(os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0])+".png"
            _capture_screenshot(file_name)
            if file_name:
                # html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                #        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.image(file_name))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)