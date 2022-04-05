# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 20:54:47 2022

@author: Usuario
"""

########DIESEL############

from bs4 import BeautifulSoup ###No usaremos, es una página dinámica (tiene java script// .do)
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select

text_dropdown1 = "LIMA"
text_dropdown2 = "LIMA"
text_dropdown3 = "ANCON"
diesel ='Diesel B5 UV'
DB5='DB5 S-50 UV'

DRIVER_PATH = 'C:/chromedriver.exe' 
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
my_page = 'https://www.facilito.gob.pe/facilito/pages/facilito/buscadorEESS.jsp'
driver.get(my_page)
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/a[14]").click() ###FULLLL XPATH

select1 = Select(driver.find_element_by_xpath('//*[@id="contenido_listado"]/div[5]/div[2]/select[2]'))
select1.select_by_visible_text(text_dropdown2)
Select(driver.find_element_by_xpath('//*[@id="contenido_listado"]/div[5]/div[2]/select[3]')).select_by_visible_text(text_dropdown3)

#####TIPO DE COMBUSTIBLE
Select(driver.find_element_by_xpath('//*[@id="contenido_listado"]/div[5]/div[2]/select[4]')).select_by_visible_text(diesel)
Select(driver.find_element_by_xpath('//*[@id="contenido_listado"]/div[5]/div[2]/select[4]')).select_by_visible_text(DB5)




dropdown_locator = driver.find_element_by_xpath('//*[@id="contenido_listado"]/div[5]/div[2]/select[1]') 
dropdown_locator.click()
select = Select("dropdown_locator")
if locator is not None:
    for option in select.options:
        select.select_by_visible_text(text_dropdown)



soup = BeautifulSoup(open(my_page),"lxml")
DRIVER_PATH = 'C:/chromedriver.exe' ###Recordar tener el .exe compatible con el Chrome.
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://observatorio.osinfor.gob.pe/Observatorio/Home/listaRoja")
driver.find_element_by_xpath("//img[@src='/Observatorio/Imagenes/iconos/map_sisfor.png']").click()