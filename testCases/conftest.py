import pytest
from selenium import webdriver
import pytest
import os
import datetime



@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

SCREENSHOT_DIR = "/Users/jaypatel/PycharmProjects/NEAP Demo/Screenshots"

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