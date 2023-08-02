from qrlib.QRComponent import QRComponent
from RPA.Browser.Selenium import Selenium
from seleniumwire import webdriver
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import time

class DefaultComponent(QRComponent):
    
    def __init__(self):
        super().__init__()
        self.selenium = Selenium()
        # self.driver = webdriver

    def login(self):
        logger = self.run_item.logger
        try:
            proxy_address = "10.13.0.245"
            proxy_port = "8080"
            proxy_username = "hoituser"
            proxy_password = "Welcome@123"


            firefox_options = FirefoxOptions()
            firefox_options.set_preference('network.proxy.type', 1)
            firefox_options.set_preference('network.proxy.http', proxy_address)
            firefox_options.set_preference('network.proxy.http_port', proxy_port)
            firefox_options.set_preference('network.proxy.socks_username', proxy_username)
            firefox_options.set_preference('network.proxy.socks_password', proxy_password)





            
            link = 'https://www.onlinekhabar.com/'
            proxy = 'http://hoituser:Welcome%40123@10.13.0.245:8080'
            self.logger.info("Logging in...")
            self.selenium.open_available_browser(headless=True, maximized=True, options=firefox_options, browser_selection='firefox')
            self.selenium.go_to(link)
            BuiltIn().log_to_console('=============  Source Page ===========')
            BuiltIn().log_to_console(self.selenium.driver.page_source)
            # self.selenium.wait_until_element_is_visible('wait_until_element_is_visible', timeout=30)
        except Exception as e:
            self.run_item.logger.error("Failed to login")
            self.run_item.notification.data = {"reason": "Login failed"}
            raise e
            
    def logout(self):
        try:
            self.logger.info("Logging out...")
        except Exception as e:
            self.logger.error("Failed to logout")
            raise e

    def test(self):
        try:
            self.logger.info("Test task")
        except Exception as e:
            self.logger.error("Test task failed")
            raise e
