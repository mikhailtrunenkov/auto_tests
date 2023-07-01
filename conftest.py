import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    
    parser.addoption('--browser_lang', action='store', default="--language=ru",
                     help="Choose language: '--language=it', '--language=ru', '--language=fr', '--language=es' ")

@pytest.fixture(scope="function")
def browser(request):
        
    browser_name = request.config.getoption("browser_name")
    browser_lang = request.config.getoption("browser_lang")
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_lang})
    
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", browser_lang)
    
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome/firefox + browser_lang should be en/ru")
    yield browser
    print("\nquit browser..")
    browser.quit()