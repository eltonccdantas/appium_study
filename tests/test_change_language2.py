import time
import unittest
import pytest

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
    "appium:appPackage": "com.shopee.br",
    "appium:appActivity": "com.shopee.app.ui.home.HomeActivity_",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
    "appium:noReset": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)



el1 = driver.find_element(by=AppiumBy.XPATH,
                          value="//android.widget.LinearLayout[@resource-id=\"com.shopee.br:id/sp_bottom_tab_layout\"]/android.widget.FrameLayout[5]/android.widget.FrameLayout")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="(//android.view.ViewGroup[@resource-id=\"meEntranceView\"])[15]")
el2.click()

time.sleep(3)

el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id='com.shopee.br:id/text_view' and @text='Idioma / Language']")
el3.click()

time.sleep(3)

el4 = driver.find_element(by=AppiumBy.XPATH,
                          value="//android.widget.TextView[@resource-id='com.shopee.br:id/text' and @text='English']")
el4.click()
el5 = driver.find_element(by=AppiumBy.ID, value="com.shopee.br:id/sp_action")
el5.click()

time.sleep(3)

object = driver.find_element(by=AppiumBy.XPATH,
                             value="//android.widget.TextView[@resource-id='com.shopee.br:id/title' and @text='Me']")

assert object.text == "Me"
driver.quit()
