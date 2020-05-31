import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

class TestMallkosik():

  def await_element(self, locator, timeout = 10):
        try:
            myElem = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            print("Loading took too much time!")
            return False

  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_mallkosik(self):
    self.driver.get("https://www.mall.cz/")
    self.driver.set_window_size(1696, 900)
    self.driver.set_window_position(0,0)
    self.await_element((By.LINK_TEXT, "Mobily, PC a kancelář"))
    element = self.driver.find_element(By.LINK_TEXT, "Mobily, PC a kancelář")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Mobily").click()
    self.driver.find_element(By.LINK_TEXT, "Nejvyšší ceny").click()
    sleep(3)
    element = self.driver.find_element(By.CSS_SELECTOR, ".product-list.lst-product")
    self.driver.execute_script("arguments[0].scrollIntoView();", element)
    self.await_element((By.CSS_SELECTOR, ".lst-product-item-body .btn-group.m-0.row-more-compare .btn-inset.lay-block"))
    buttons = self.driver.find_elements(By.CSS_SELECTOR, ".lst-product-item-body .btn-group.m-0.row-more-compare .btn-inset.lay-block")
    # add the first two most expensive products
    buttons[0].click()
    sleep(3)
    buttons[1].click()
    sleep(3)
    element = self.driver.find_element(By.CSS_SELECTOR, ".nav-customer-item *[data-sel='nav-widget-cart']")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.await_element((By.CSS_SELECTOR, "#proceed-to-cart > .btn-inset"))
    self.driver.find_element(By.CSS_SELECTOR, "#proceed-to-cart > .btn-inset").click()
  
if __name__ == "__main__":
  test = TestMallkosik()
  test.setup_method(None)
  test.test_mallkosik()
  sleep(10)
  test.teardown_method(None)