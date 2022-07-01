from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):

    lang = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    instance = Chrome(options=options)
    instance.implicitly_wait(10)
    yield instance
    instance.quit()
