from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://neap-stage.narayana.digital/")
    time.sleep(5)
    # Enter Global ID and submit
    driver.find_element(By.CSS_SELECTOR, "#userId").send_keys("test12345")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(5)
    # Find all OTP input fields and enter digits
    otp_digits = ['1', '1', '1', '1']
    otp_inputs = driver.find_elements(By.XPATH, "//input[@type='password']")

    for box, digit in zip(otp_inputs, otp_digits):
        box.send_keys(digit)
    time.sleep(5)
    # Click Login button
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/section[2]/div[2]/div[1]/div/div/div[2]/div[4]/button").click()
    driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
    driver.find_element(By.XPATH, "//button[normalize-space()='Start test']").click()


    # Optional pause to see result
    time.sleep(3)
finally:
    driver.quit()
