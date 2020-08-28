#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

browser = webdriver.Firefox()
browser.get('http://www.trustandwill.com/')

# Complete get started workflow with options for married with kids and will
WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.ID, 'get-started-nav-item'))).click()
WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.ID, 'kids'))).click()
browser.find_element_by_id('married').click()
browser.find_element_by_id('recommend').click()
browser.find_element_by_xpath('/html/body/main/div/section/div[2]/div[2]/div[1]/button').click()

# Enter new customer email address and password
browser.find_element_by_id('email').send_keys('adam.collardey+50@gmail.com' + Keys.RETURN)
browser.find_element_by_id('password').send_keys('Testing123' + Keys.RETURN)

# Start new customer onboarding dialogue
WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/mat-sidenav-container/mat-sidenav-content/div/div/div/app-welcome/div[2]/app-start/app-row-wrapping-container/div/div[1]/div[4]/div/div/app-button/div/span/button/div/span'))).click()
WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/mat-sidenav-container/mat-sidenav-content/div/div/div/app-welcome/div[2]/app-here-to-help/app-row-wrapping-container/div/div[1]/div[4]/div[1]/div/app-button/div/span/button'))).click()
WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/mat-sidenav-container/mat-sidenav-content/div/div/div/app-welcome/div[2]/app-sections/app-row-wrapping-container/div/div[1]/div[4]/div/div/app-button/div/span/button/div'))).click()

# Enter in new customer name, State, and logout
browser.find_element_by_css_selector('#user-name').send_keys('Adam P Collardey' + Keys.RETURN)
WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/mat-sidenav-container/mat-sidenav-content/div/div/div/app-my-info/div[2]/app-state/app-row-wrapping-container/div/div[1]/div[3]/div/mat-form-field/div/div[1]/div/mat-select/div/div[1]/span'))).click()
browser.find_element_by_id('mat-option-4').click() #California
WebDriverWait(browser, timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.dropdown-hover-nav > ul:nth-child(1)'))).click()


#Previous unused code
#WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/mat-sidenav-container/mat-sidenav-content/div/div/div/app-my-info/div[2]/app-state/app-row-wrapping-container/div/div[1]/div[4]/div/div/app-button/div/span/button/div/span'))).click()
#WebDriverWait(browser, timeout=10).until(EC.element_to_be_selected((By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/mat-sidenav-container/mat-sidenav-content/div/div/div/app-my-info/div[2]/app-age/app-row-wrapping-container/div/div[1]/div[4]/div/div/app-button/div/span/button/div/span')))
#ActionChains(browser).send_keys('11' + Keys.TAB + '16' + Keys.TAB + '1999' + Keys.RETURN)
#WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/mat-sidenav-container/mat-sidenav-content/div/div/div/app-my-info/div[2]/app-age/app-row-wrapping-container/div/div[1]/div[3]/div/app-dob/div/div[1]'))).click()
#browser.find_element_by_xpath('/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/mat-sidenav-container/mat-sidenav-content/div/div/div/app-my-info/div[2]/app-age/app-row-wrapping-container/div/div[1]/div[3]/div/app-dob/div/div[1]').send_keys('10' + Keys.TAB + '06' + Keys.TAB + '1980' + Keys.RETURN)

