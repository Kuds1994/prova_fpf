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
    
except TimeoutError:
    print()

button = driver.find_element_by_id('menu_wl2g')    
button.click()    

try:
    nivelIframe2()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'ssid')))
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'mode'))) 
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'channel'))) 
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'ssidBroadcast')))           
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Salvar']")))      

except TimeoutError:
    print()

espera()
campo = driver.find_element_by_id('ssid')
campo.clear()  
campo.send_keys("Wi-fi")

espera()
modo = Select(driver.find_element_by_id('mode'))
modo.select_by_value('g')

espera()
modo = Select(driver.find_element_by_id('channel'))
modo.select_by_value('5')

espera()
nome = driver.find_element_by_id('ssidBroadcast')
nome.click()

espera()
salvar = driver.find_element_by_xpath("//input[@value='Salvar']")
salvar.click() 
