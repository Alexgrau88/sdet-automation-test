import datetime
import sys

import allure
import pytest
from amazoncaptcha import AmazonCaptcha
from datetime import datetime

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

"""Left the pytest_addoption in place as a reference, tried making headless parameterizable, but wa unable to do so.
    Kept getting ValueError: no option named '--headless' error displayed
    I also left the rest of the code for this commented in the chrome_driver function"""
# def pytest_addoption(parser):
#     parser.addoption("--headless", action="store_true", default=True, help="Run tests in headless mode")


@pytest.fixture(scope="session")
def chrome_driver():
    # headless = request.config.getoption("--headless")

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--start-fullscreen')
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--pageLoadStrategy=normal')
    chrome_options.add_argument('--headless')  # disable if you want to run without headless
    # if headless:
    #     chrome_options.add_argument('--headless')

    # Create an instance of the Chrome driver
    chrome_driver_path = "C:\\Program Files (x86)\\SeleniumDrivers\\chromedriver.exe"
    service = Service(chrome_driver_path)
    driver = Chrome(service=service, options=chrome_options)

    yield driver

    # Teardown: Close the browser after all tests
    driver.quit()


# Amazon captcha solver
def captcha_check(driver):
    while "Type the characters you see in this image:" in driver.page_source:
        sys.stdout.write('\r')
        sys.stdout.write("Trying to bypass")
        sys.stdout.flush()
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class = 'a-row a-text-center']"))
            )
            link = driver.find_element(By.XPATH, "//div[@class = 'a-row a-text-center']").find_element(By.TAG_NAME, "img").get_attribute("src")
            captcha = AmazonCaptcha.fromlink(link)
            solution = captcha.solve()
            driver.find_element(By.ID, "captchacharacters").send_keys(solution)
            driver.find_element(By.CLASS_NAME, "a-button-text").click()
            sys.stdout.write('\r')
            sys.stdout.write("Captcha Bypass Successfully\n")
            sys.stdout.flush()
        except TimeoutException:
            sys.stdout.write('\r')
            sys.stdout.write("Timeout while waiting for captcha elements\n")
            sys.stdout.flush()
        except NoSuchElementException:
            sys.stdout.write('\r')
            sys.stdout.write("Unable to locate captcha elements\n")
            sys.stdout.flush()


def capture_screenshot(driver, name_prefix="screenshot", directory=None):
    if directory is None:
        # Provide a default directory if not specified
        directory = "D:\\Git_Repo\\OnceMore\\Swapcard\\test_Screenshots"

    timestamp = datetime.now().strftime("%Y.%m.%d_%H.%M.%S")
    file_name = f"{directory}\\Fail_{name_prefix}_{timestamp}.png"
    driver.get_screenshot_as_file(file_name)

    # Attach the screenshot to the Allure report
    with allure.step(f"Attach Screenshot: {name_prefix}"):
        allure.attach.file(file_name, name=f"{name_prefix}_screenshot", attachment_type=allure.attachment_type.PNG)


# Not used, left for reference
def wait_for_element(driver, by_locator, condition, timeout=10):
    return WebDriverWait(driver, timeout).until(lambda driver: condition(by_locator))
