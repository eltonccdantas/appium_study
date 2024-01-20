# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.google.android.calculator",
    "appium:appActivity": "com.android.calculator2.Calculator",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="7")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="multiplicar")
el2.click()
el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="8")
el3.click()
el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="igual")
el4.click()

result = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/result_final")

assert result.text == "56"

driver.quit()
