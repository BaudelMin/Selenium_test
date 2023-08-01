from qrlib.QRComponent import QRComponent
from RPA.Browser.Selenium import Selenium


class DefaultComponent(QRComponent):
    
    def __init__(self):
        super().__init__()
        self.selenium = Selenium()
        self.driver = self.selenium

    def login(self):
        logger = self.run_item.logger
        try:
            link = 'https://www.onlinekhabar.com/'
            proxy = 'http://hoituser:Welcome%40123@10.13.0.245:8080'
            self.logger.info("Logging in...")
            self.selenium.open_available_browser(proxy=proxy)
            self.selenium.go_to(link)
            logger.info('=============  Source Page ===========')
            logger.info(self.browser.selenium.page_source)
            self.selenium.wait_until_element_is_visible('wait_until_element_is_visible', timeout=30)
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
