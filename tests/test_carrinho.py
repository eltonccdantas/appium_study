# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.shopee.br",
    "appium:appActivity": "com.shopee.app.ui.home.HomeActivity_",
    "appium:noReset": True,
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="tab_bar_button_mall")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@resource-id=\"imageSearchBar\"]")
el2.click()

time.sleep(3)

el4 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
el4.send_keys("nintendo switch")
el5 = driver.find_element(by=AppiumBy.XPATH,
                          value="//android.view.ViewGroup[@resource-id=\"viewSearchBar\"]/android.view.ViewGroup[2]/android.view.ViewGroup")
el5.click()

time.sleep(3)

el6 = driver.find_element(by=AppiumBy.XPATH,
                          value="//android.widget.TextView[@resource-id=\"labelItemCardItemName_22426285151\"]")
el6.click()

time.sleep(3)

valor_do_item = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='labelProductPageProductPriceActual']")
assert valor_do_item.text == "R$2.049,90"

el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.ViewGroup[@resource-id=\"buttonProductAddCart\"]")
el7.click()


el8 = driver.find_element(by=AppiumBy.XPATH,
                          value="//android.view.ViewGroup[@resource-id=\"buttonActionBarView\"]/android.view.ViewGroup")
el8.click()

time.sleep(3)

total = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='labelSubTotalPrice']")

assert total.text == "R$2.049,90"


el9 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='+']")
el9.click()

total = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='labelSubTotalPrice']")

assert total.text == "R$4.099,80"

driver.quit()
