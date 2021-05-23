from selenium import webdriver
import pytest

'''
@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver
'''

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver = webdriver.firefox()
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption('--browser')
    
@pytest.fixture()
def browser(request):
    return request.config.getadoption('--browser')

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Vaibhav'

def pytest_metadata(metadata):
    metadata.pop("JavaHome",None)
    metadata.pop("plugins", None)
    


