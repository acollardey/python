#!/usr/bin/python3

# using selenium webdriver and pytest
# v1 tests login/logout for an email account and a facebook test account 
# manually enter in password for facebook_password variable before running
# afterwards run the python script sample.py to remove the facebook test account from the db
 

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from faker import Faker

fake = Faker() 
wait_time = 20
user_name = fake.name()
user_email = fake.safe_email()
facebook_email = "example@tfbnw.net"
facebook_password = ""
facebook_name = fake.name()

class TestLogins():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def wait_until_clickable(self, xpath_var):
    WebDriverWait(self.driver, timeout=wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath_var))).click()

  def click_through_interceptions(self, xpath_var):
     while True:
      try:
        WebDriverWait(self.driver, timeout=wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath_var))).click()
        break
      except ElementClickInterceptedException:
        pass

  def log_out(self):
    action = ActionChains(self.driver)
    # hover over account menu icon
    firstLevelMenu = self.driver.find_element_by_id("...")
    action.move_to_element(firstLevelMenu).perform()
    # click Sign Out
    WebDriverWait(self.driver, timeout=wait_time).until(EC.element_to_be_clickable((By.XPATH, "..."))).click()
  
  def test_logins(self):
    self.driver.get("...")
    self.driver.set_window_size(1567, 936)

    action = ActionChains(self.driver)
    main_window = self.driver.current_window_handle

# create new accounts, enter some info, log out, log in

    # create new email account
    self.driver.find_element(By.XPATH, "...").click()
    self.wait_until_clickable("...")
    self.driver.find_element(By.XPATH, "...").send_keys(user_email)
    self.driver.find_element(By.XPATH, "...").click()
    self.driver.find_element(By.XPATH, "...").send_keys("...")
    self.driver.find_element(By.XPATH, "...").click()
    WebDriverWait(self.driver, timeout=wait_time).until(EC.element_to_be_clickable((By.XPATH, "...")))
    element = self.driver.find_element(By.XPATH, "...")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.XPATH, "...").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "...")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.click_through_interceptions("...")
    self.wait_until_clickable("...")
    self.click_through_interceptions("...")
    self.log_out()
   # click Log In, enter existing email and password, then log out
    WebDriverWait(self.driver, timeout=wait_time).until(EC.element_to_be_clickable((By.XPATH, "..."))).click()
    self.wait_until_clickable("...")
    self.driver.find_element(By.XPATH, "...").send_keys(user_email)
    self.driver.find_element(By.XPATH, "...").send_keys("..." + Keys.RETURN)
    WebDriverWait(self.driver, timeout=wait_time).until(EC.element_to_be_clickable((By.ID, "sub-nav"))) 
    self.log_out()

    # facebook
    self.wait_until_clickable("...")
    self.wait_until_clickable("...")
    # find and select login popup window
    for handle in self.driver.window_handles: 
      if handle != main_window: 
        login_window = handle 
    self.driver.switch_to_window(login_window)
    WebDriverWait(self.driver, timeout=wait_time).until(EC.element_to_be_clickable((By.ID, "email"))).click()
    self.driver.find_element(By.ID, "email").send_keys(facebook_email)
    self.driver.find_element(By.ID, "pass").send_keys(facebook_password + Keys.RETURN)
    self.driver.switch_to_window(main_window)
    # start sequence
    WebDriverWait(self.driver, timeout=wait_time).until(EC.element_to_be_clickable((By.XPATH, "...")))
    element = self.driver.find_element(By.XPATH, "...")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.XPATH, "...").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "...")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.click_through_interceptions("...")
    self.wait_until_clickable("...")
    self.wait_until_clickable("...")
    self.driver.find_element(By.XPATH, "...").send_keys(facebook_name)
    self.driver.find_element(By.XPATH, "...").click()
    self.click_through_interceptions("...")
    self.driver.find_element(By.XPATH, "...").click()
    WebDriverWait(self.driver, timeout=wait_time).until(EC.element_to_be_clickable((By.XPATH, "...")))
    self.driver.find_element(By.XPATH, "...]").send_keys("...")
    self.driver.find_element(By.XPATH, "...").send_keys("...")
    self.driver.find_element(By.XPATH, "...").send_keys("...")
    self.click_through_interceptions("...")
    self.log_out()
    # click Log In, auto-login with existing account info, log out
    WebDriverWait(self.driver, timeout=wait_time).until(EC.element_to_be_clickable((By.XPATH, "..."))).click()
    self.wait_until_clickable("...")
    WebDriverWait(self.driver, timeout=wait_time).until(EC.element_to_be_clickable((By.ID, "...")))
    self.log_out()






    # google




   # find and select login popup window
   # for handle in self.driver.window_handles: 
   #     if handle != main_window: 
   #         login_window = handle 
   # self.driver.switch)to_window(login_window)


# try bad logins, verify errors

    # email

    # facebook

    # google


# clean up

# wipe facebook test user from db

# wipe google test user from db
