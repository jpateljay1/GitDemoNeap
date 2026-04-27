from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import datetime
import pytest

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")



@pytest.fixture()
def setup(request):
    chrome_options = Options()
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

# Define screenshot directory relative to project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOT_DIR = os.path.join(project_root, "Screenshots")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshots automatically when a test case fails.
    """
    outcome = yield
    rep = outcome.get_result()

    # Only capture screenshot when the test itself (not setup/teardown) fails
    if rep.when == "call" and rep.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            # Ensure the folder exists
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)

            # Name the file with test name + timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            path = os.path.join(SCREENSHOT_DIR, file_name)

            # Capture the screenshot
            driver.save_screenshot(path)
            print(f"\n📸 Screenshot captured: {path}")

            # Attach to pytest-html report (if available)
            if hasattr(rep, "extra"):
                rep.extra.append(pytest.html.extras.image(path, mime_type='image/png'))