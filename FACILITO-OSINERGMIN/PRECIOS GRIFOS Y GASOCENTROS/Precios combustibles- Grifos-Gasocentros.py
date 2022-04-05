# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 18:05:22 2022

@author: Abner
"""

from selenium import webdriver
#import time
#//*[@id="browser"]/li[1]/ul/li[1]/ul/li[2]/span/a  # Demanda nacional de combustibles líquidos, Febrero 2022
# //*[@id="browser"]/li[1]/ul/li[2]/ul/li[1]/span/a # Demanda nacional de combustibles líquidos, Febrero 2021
# //*[@id="browser"]/li[9]/ul/li[1]/ul/li/span/a


####### //*[@id='browser']/li[9]/ul/li[2]/span ### 2022: 1; 2021: 2; 2020: 3...2019: 4
# //*[@id="browser"]/li[9]/ul/li[3]/ul/li[1]/span/a : 2020
# //*[@id="browser"]/li[9]/ul/li[4]/ul/li[1]/span/a :2019
# 2022 ok
#2021, NO CORRIÓ 5, 8, 10 12
# 2020, NO CORRIÓ 12
#2019, NO CORRIÓ NOVIEMBRE Y DICIEMBRE
for j in [12]: #range(1,12): #Mejor usar lista para las siguientes, para solo cambiar números si uno no corre
    l=str(j)
    DRIVER_PATH = 'C:/chromedriver.exe' 
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get("https://becas.osinergmin.gob.pe/empresas/hidrocarburos/Paginas/SCOP-DOCS/scop_docs.htm")
    driver.find_element_by_xpath("//*[@id='browser']/li[9]/span").click() #Procurar '' en vez de "" #9 es el para precio de combustibles
    driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li[2]/span").click()  # //*[@id="browser"]/li[9]/ul/li[18]/span  #18 es para 2005 y #//*[@id="browser"]/li[9]/ul/li[1]/span #para 2022
    try: 
        driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li[2]/ul/li["+l+"]/span/a").click() #//*[@id="browser"]/li[1]/ul/li[2]/span ##Hacer un bucle luego
            #//*[@id="browser"]/li[9]/ul/li[2]/ul/li[2]/span/a  #Febrero
            # //*[@id="browser"]/li[9]/ul/li[2]/ul/li[3]/span/a  #Marzo
    except Exception:
         continue
    import time
    time.sleep(2)   
    window_after = driver.window_handles[1] ###Ubicación 1 pues es la ventana 2
    driver.switch_to.window(window_after)  
    urlwd=driver.current_url
    print(urlwd) 
    time.sleep(2)
    import tabula as tb
    df= tb.read_pdf(urlwd, pages=2, area=(118, 124,483,719), output_format="dataframe", encoding='latin-1') #area=[box]
    df[0].to_excel('D:\\Git-Hub\\Works\\FACILITO-OSINERGMIN\\PRECIOS GRIFOS Y GASOCENTROS\\2021\\df2021grifos'+l+'.xlsx', index = True) #df es una lista con un dataframe en el primer elemento
 
    
df= tb.read_pdf(urlwd, pages=2, area=(118, 124,483,719), output_format="dataframe", encoding='latin-1') #area=[box]
df[0].to_excel('D:\\Git-Hub\\Works\\FACILITO-OSINERGMIN\\PRECIOS GRIFOS Y GASOCENTROS\\2021\\df2021grifos'+l+'.xlsx', index = True) #df es una lista con un dataframe en el primer elemento

for i in [11,12]:
    print(i)    
    
for j in [11,12]: ##Diciembre no bajó
    l=str(j)
    DRIVER_PATH = 'C:/chromedriver.exe' 
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get("https://becas.osinergmin.gob.pe/empresas/hidrocarburos/Paginas/SCOP-DOCS/scop_docs.htm")
    driver.find_element_by_xpath("//*[@id='browser']/li[9]/span").click() #Procurar '' en vez de "" #9 es el para precio de combustibles
    driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li[3]/span").click()  # //*[@id="browser"]/li[9]/ul/li[18]/span  #18 es para 2005 y #//*[@id="browser"]/li[9]/ul/li[1]/span #para 2022
    try: 
        driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li[3]/ul/li["+l+"]/span/a").click() #//*[@id="browser"]/li[1]/ul/li[2]/span ##Hacer un bucle luego
            #//*[@id="browser"]/li[9]/ul/li[2]/ul/li[2]/span/a  #Febrero
            # //*[@id="browser"]/li[9]/ul/li[2]/ul/li[3]/span/a  #Marzo
            #//*[@id="browser"]/li[9]/ul/li[2]/ul/li[5]/span/a 
    except Exception:
         continue
    import time
    time.sleep(2)   
    window_after = driver.window_handles[1] ###Ubicación 1 pues es la ventana 2
    driver.switch_to.window(window_after)  
    urlwd=driver.current_url
    print(urlwd) 
    time.sleep(2)
    import tabula as tb
    df= tb.read_pdf(urlwd, pages=2, area=(118, 124,483,719), output_format="dataframe", encoding='latin-1') #area=[box]
    df[0].to_excel('D:\\Git-Hub\\Works\\FACILITO-OSINERGMIN\\PRECIOS GRIFOS Y GASOCENTROS\\2020\\df2020grifos'+l+'.xlsx', index = True) 
    

DRIVER_PATH = 'C:/chromedriver.exe' 
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://becas.osinergmin.gob.pe/empresas/hidrocarburos/Paginas/SCOP-DOCS/scop_docs.htm")
driver.find_element_by_xpath("//*[@id='browser']/li[9]/span").click() #Procurar '' en vez de "" #9 es el para precio de combustibles
driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li[2]/span").click()  # //*[@id="browser"]/li[9]/ul/li[18]/span  #18 es para 2005 y #//*[@id="browser"]/li[9]/ul/li[1]/span #para 2022
driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li[2]/ul/li[12]/span/a ").click()
window_after = driver.window_handles[1] ###Ubicación 1 pues es la ventana 2
driver.switch_to.window(window_after)  
urlwd=driver.current_url
df= tb.read_pdf(urlwd, pages=2, area=(118, 124,483,719), output_format="dataframe") #area=[box]
df[0].to_excel('D:\\Git-Hub\\Works\\FACILITO-OSINERGMIN\\PRECIOS GRIFOS Y GASOCENTROS\\2021\\df2021grifos12.xlsx', index = True)

    
    
    
    
    

"""for j in range(1,12):
   for i in range(1,18): #//*[@id="browser"]/li[9]/ul/li[2]/ul/li[12]/span/a 
        DRIVER_PATH = 'C:/chromedriver.exe' 
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        s=str(i)
        driver.get("https://becas.osinergmin.gob.pe/empresas/hidrocarburos/Paginas/SCOP-DOCS/scop_docs.htm")
        driver.find_element_by_xpath("//*[@id='browser']/li[9]/span").click() #Procurar '' en vez de "" #9 es el para precio de combustibles
        driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li["+s+"]/span").click()  # //*[@id="browser"]/li[9]/ul/li[18]/span  #18 es para 2005 y #//*[@id="browser"]/li[9]/ul/li[1]/span #para 2022

# //*[@id="browser"]/li[9]/ul/li[2]/ul/li[1]/span/a
# //*[@id="browser"]/li[9]/ul/li[2]/ul/li[2]/span/a
        #window_after = driver.window_handles[0]
        l=str(j)
        try: 
           driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li["+l+"]/ul/li/span/a").click() #//*[@id="browser"]/li[1]/ul/li[2]/span ##Hacer un bucle luego
            #//*[@id="browser"]/li[9]/ul/li[2]/ul/li[2]/span/a 
        except Exception as e:
           print(e)
        import time
        time.sleep(5)   
        window_after = driver.window_handles[1] ###Ubicación 1 pues es la ventana 2
        driver.switch_to.window(window_after)  
        urlwd=driver.current_url
        print(urlwd) 
        time.sleep(2)"""




