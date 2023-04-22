import time

from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def find_element(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get(self, url):
        return self.driver.get(url)

    def click_on_element(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        time.sleep(1)
        self.driver.find_element(*locator).click()


