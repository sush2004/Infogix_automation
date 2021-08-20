#file storing all the fixtures(common steps)
import pytest
from selenium import webdriver


#command line trigger pytest convention
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

#Pre-requisite test steps
@pytest.fixture(scope="class") #declaring scope of fixture at class level
def setup(request):
    #selecting browser on runtime
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

    elif browser_name == "firefox":
        print("Firefox")  #gecho driver for firefox

    else:
        print("IE")      #driver for IE

    driver.get("https://www.infogix.com/")
    driver.maximize_window()
    #assigning local instance driver to class driver
    request.cls.driver = driver
    #post run test steps
    yield
    driver.close()

