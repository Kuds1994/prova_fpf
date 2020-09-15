from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://emulator.tp-link.com/C50V4_BR_Emulator/Emulator/index.htm")


def nivelIframe1():
    driver.switch_to.default_content()
    driver.switch_to.frame(0)
    driver.switch_to.frame(1)

def nivelIframe2():
    driver.switch_to.default_content()
    driver.switch_to.frame(0)
    driver.switch_to.frame(2)  

def espera(tempo=2):
    time.sleep(tempo)             

try:
    nivelIframe1()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'menu_qs')))      
    
except TimeoutError:
    print()


id = driver.find_element_by_id('menu_qs')    
id.click()

try:
    nivelIframe2()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Próximo']")))      
    
except TimeoutError:
    print()

espera()
button = driver.find_element_by_xpath("//input[@value='Próximo']")
button.click()

try:    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "auto")))  
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Próximo']")))    
    
except TimeoutError:
    print()

espera(1)
button = driver.find_element_by_id("auto")
button.click()
espera(1)
button = driver.find_element_by_xpath("//input[@value='Próximo']")
button.click()

espera()
driver.switch_to.alert.accept()

