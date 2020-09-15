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
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'menu_ddns')))          
    
except TimeoutError:
    print()      

menu = driver.find_element_by_id("menu_ddns")
menu.click() 

try:
    nivelIframe2()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "noipDomain")))
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ddns_usr"))) 
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ddns_pwd"))) 
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "ddns_pwd"))) 
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "save"))) 
            
    
except TimeoutError:
    print()   

espera()
campo = driver.find_element_by_id("noipDomain")
campo.send_keys("www.dominio.com")

espera()
campo = driver.find_element_by_id("ddns_usr")
campo.send_keys("eduardo")

espera()
campo = driver.find_element_by_id("ddns_pwd")
campo.send_keys("12345678")

espera()
salvar = driver.find_element_by_id("save")
salvar.click()

