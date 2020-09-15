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
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'menu_pc')))            
    
except TimeoutError:
    print()  

menu = driver.find_element_by_id('menu_pc')  
menu.click()

try:
    nivelIframe2()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'ParentCtr_en')))  
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 't_copy1')))
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'saveClkBtn')))  
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'mac1')))  
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'timeS'))) 
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'timeE')))  
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@value='Adicionar']"))) 
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'urlInfo')))
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'saveBtn')))         
    
except TimeoutError:
    print()  

adicionar = driver.find_elements_by_xpath("//input[@value='Adicionar']")    

espera()
check = driver.find_element_by_id('ParentCtr_en')
check.click()

espera()
copy = driver.find_element_by_id('t_copy1')
copy.click()

espera()
buttonS = driver.find_element_by_id('saveClkBtn')
buttonS.click()

espera()
endereco = driver.find_element_by_id('mac1')
endereco.send_keys('74:D4:35:A1:0C:CB')

espera()
timeS = Select(driver.find_element_by_id('timeS'))
timeS.select_by_value('12')

espera()
timeE = Select(driver.find_element_by_id('timeE'))
timeE.select_by_value('39')

espera()
adicionar[0].click()

espera()
url = driver.find_element_by_id('urlInfo')
url.send_keys('www.google.com')

espera()
adicionar[1].click()

espera()
salvar = driver.find_element_by_id('saveBtn')
salvar.click()






