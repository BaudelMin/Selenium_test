from qrlib.QRComponent import QRComponent
from RPA.Browser.Selenium import Selenium
from seleniumwire import webdriver
from robot.libraries.BuiltIn import BuiltIn

import time

class DefaultComponent(QRComponent):
    
    def __init__(self):
        super().__init__()
        self.selenium = Selenium()
        # self.driver = webdriver

    def login(self):
        logger = self.run_item.logger
        try:
            
            proxy_host = "10.13.0.245"
            proxy_port = "8080"
            proxy_username = "hoituser"
            proxy_password = "Welcome@123"

            # Proxy URL with authentication
            proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"

            # Chrome WebDriver options with proxy settings
            
            # http://hoituser:Welcome%40123@10.13.0.245:8080
            options = {
                'proxy': {
                    'http': proxy_url,
                    'https': proxy_url,
                    'no_proxy': 'localhost,127.0.0.1'  # Optional: exclude localhost from the proxy
                }
            }

            # Create the WebDriver instance with the desired options
            driver = webdriver.Chrome(seleniumwire_options=options)

            # Now you can use the driver to navigate to a website through the proxy
            driver.get("https://www.onlinekhabar.com/")
            
            logger.info(driver.page_source)
            
            BuiltIn().log_to_console(driver.page_source)
            
            time.sleep(10)
            # Add your scraping or testing code here

            # Close the WebDriver
            driver.quit()





            
            # link = 'https://www.onlinekhabar.com/'
            # proxy = 'http://hoituser:Welcome%40123@10.13.0.245:8080'
            # self.logger.info("Logging in...")
            # self.selenium.open_available_browser(proxy=proxy)
            # self.selenium.go_to(link)
            # logger.info('=============  Source Page ===========')
            # logger.info(self.browser.selenium.page_source)
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
