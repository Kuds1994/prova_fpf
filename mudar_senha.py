from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'menu_wl2g'))) 
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'menu_wlsec')))         
    
except TimeoutError:
    print()    


menu = driver.find_element_by_id('menu_wl2g')    
menu.click()   

espera()
within_menu = driver.find_element_by_id('menu_wlsec')
within_menu.click() 

try:
    nivelIframe2()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'pskSecret')))
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Salvar']"))) 
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'secPSK')))   
    
except TimeoutError:
    print() 

espera()
select = driver.find_element_by_id('secPSK')
select.click()

espera()
campo = driver.find_element_by_id('pskSecret')
campo.clear()
campo.send_keys('senha1')

espera()
campo = driver.find_element_by_xpath("//input[@value='Salvar']")
campo.click()

espera()
driver.switch_to.alert.accept()