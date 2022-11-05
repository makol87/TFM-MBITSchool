#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


# In[2]:


from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver_manager


# In[3]:


manager = ChromeDriverManager()


# In[4]:


metadata = manager.driver_cache.get_metadata()


# In[5]:


key = list(metadata)[0]


# In[6]:


url = "https://keepa.com/#!data"

chrome_options = Options()
#chrome_options.add_argument('--headless')
webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get(url)


# In[7]:


usuario = 'makol'
password = '13032019'


# default search query
with webdriver as driver:
    # Set timeout time 
    wait = WebDriverWait(driver, 10)

    # retrive url in headless browser
    driver.get(url)
    
    # click login
    time.sleep(3)
    wait.until(presence_of_element_located((By.XPATH, "//button[@class='mdc-button mdc-button--raised']"))).click()
   
    # Insertar las claves
    user = wait.until(presence_of_element_located((By.XPATH, "//input[@id='username']")))
    user.send_keys(usuario)
    
    user = wait.until(presence_of_element_located((By.XPATH, "//input[@id='password']")))
    user.send_keys(password + Keys.RETURN)  
    
    # Click to best seller
    time.sleep(3)
    wait.until(presence_of_element_located((By.LINK_TEXT,'Product Best Sellers'))).click()

    # Click to electronica
    time.sleep(3)
    wait.until(presence_of_element_located((By.LINK_TEXT,'Electrónica'))).click()

    # Desplegable filas
    time.sleep(3)
    wait.until(presence_of_element_located((By.XPATH, "//span[@class='tool__row mdc-menu-anchor']"))).click()
 
    # Seleccíon 5000
    time.sleep(3)
    #wait.until(presence_of_element_located((By.XPATH, "//li[@class='mdc-list-item']/[@data-value='5000']"))).click()
    #wait.until(presence_of_element_located((By.LINK_TEXT,'5000'))).click()
    wait.until(presence_of_element_located((By.XPATH, "//*[@id='tool-row-menu']/ul/li[7]"))).click()

    # Espero 5000 filas
    time.sleep(260)
    
    #click 1er export
    time.sleep(3)
    wait.until(presence_of_element_located((By.XPATH, "//*[@id='grid-tools-bestseller']/div[1]/span[3]/span/i"))).click()
    
    #click 2 export
    time.sleep(3)
    try: 
        print('1er intento')
        export = wait.until(presence_of_element_located((By.XPATH, "//*[@class='fa fa-download']")))
        export.click()
        export.click()
        time.sleep(5) 
  
    except:
        print('2 intento')
        wait.until(presence_of_element_located((By.XPATH, "//button[@id='exportSubmit']"))).click()


    driver.close()


# In[ ]:





# In[ ]:





# In[ ]:




