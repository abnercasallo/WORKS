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


####### //*[@id='browser']/li[9]/ul/li[2]/span ### 2022: 1; 2021: 2; 2020: 3...2019: 4
# //*[@id="browser"]/li[9]/ul/li[3]/ul/li[1]/span/a : 2020
# //*[@id="browser"]/li[9]/ul/li[4]/ul/li[1]/span/a :2019
#2021, NO CORRIÓ 5, 8, 10 12
# 2020, NO CORRIÓ 12
#2019, NO CORRIÓ NOVIEMBRE Y DICIEMBRE
for j in range(1,12):
    l=str(j)
    DRIVER_PATH = 'C:/chromedriver.exe' 
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get("https://becas.osinergmin.gob.pe/empresas/hidrocarburos/Paginas/SCOP-DOCS/scop_docs.htm")
    driver.find_element_by_xpath("//*[@id='browser']/li[9]/span").click() #Procurar '' en vez de "" #9 es el para precio de combustibles
    driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li[4]/span").click()  # //*[@id="browser"]/li[9]/ul/li[18]/span  #18 es para 2005 y #//*[@id="browser"]/li[9]/ul/li[1]/span #para 2022
    try: 
        driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li[4]/ul/li["+l+"]/span/a").click() #//*[@id="browser"]/li[1]/ul/li[2]/span ##Hacer un bucle luego
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
    df= tb.read_pdf(urlwd, pages=1, area=(115, 54,374,788), output_format="dataframe", encoding='latin-1') #area=[box]
    df[0].to_excel('D:\\Git-Hub\\Works\\FACILITO-OSINERGMIN\\2019\\df'+l+'.xlsx', index = True) #df es una lista con un dataframe en el primer elemento
    
    
    
for i in [12]:
    print(i)    
    
for j in [12]: ##Diciembre no bajó
    l=str(j)
    DRIVER_PATH = 'C:/chromedriver.exe' 
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get("https://becas.osinergmin.gob.pe/empresas/hidrocarburos/Paginas/SCOP-DOCS/scop_docs.htm")
    driver.find_element_by_xpath("//*[@id='browser']/li[9]/span").click() #Procurar '' en vez de "" #9 es el para precio de combustibles
    driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li[4]/span").click()  # //*[@id="browser"]/li[9]/ul/li[18]/span  #18 es para 2005 y #//*[@id="browser"]/li[9]/ul/li[1]/span #para 2022
    try: 
        driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li[4]/ul/li["+l+"]/span/a").click() #//*[@id="browser"]/li[1]/ul/li[2]/span ##Hacer un bucle luego
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
    df= tb.read_pdf(urlwd, pages=1, area=(115, 54,374,788), output_format="dataframe", encoding='latin-1') #area=[box]
    df[0].to_excel('D:\\Git-Hub\\Works\\FACILITO-OSINERGMIN\\2019\\df'+l+'.xlsx', index = True) #df es una lista con un dataframe en el primer elemento
    
    

DRIVER_PATH = 'C:/chromedriver.exe' 
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://becas.osinergmin.gob.pe/empresas/hidrocarburos/Paginas/SCOP-DOCS/scop_docs.htm")
driver.find_element_by_xpath("//*[@id='browser']/li[9]/span").click() #Procurar '' en vez de "" #9 es el para precio de combustibles
driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li[1]/span").click()  # //*[@id="browser"]/li[9]/ul/li[18]/span  #18 es para 2005 y #//*[@id="browser"]/li[9]/ul/li[1]/span #para 2022
driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li[1]/ul/li[1]/span/a ").click()
window_after = driver.window_handles[1] ###Ubicación 1 pues es la ventana 2
driver.switch_to.window(window_after)  
urlwd=driver.current_url
df= tb.read_pdf(urlwd, pages=1, area=(115, 54,374,788), output_format="dataframe") #area=[box]
df[0].to_excel('D:\\Git-Hub\\Works\\FACILITO-OSINERGMIN\\2022\\df1.xlsx', index = True) #df es una lista con un dataframe en el primer elemento

    
    
    
    
    
    """ ###FUNCIONA, PERO SE ROMPE A VECES:   
for i in range (2,18):#Del 2021 al 2005
    s=str(i)
    for j in range(1,12):
        l=str(j)
        DRIVER_PATH = 'C:/chromedriver.exe' 
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get("https://becas.osinergmin.gob.pe/empresas/hidrocarburos/Paginas/SCOP-DOCS/scop_docs.htm")
        driver.find_element_by_xpath("//*[@id='browser']/li[9]/span").click() #Procurar '' en vez de "" #9 es el para precio de combustibles
        driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li["+s+"]/span").click()  # //*[@id="browser"]/li[9]/ul/li[18]/span  #18 es para 2005 y #//*[@id="browser"]/li[9]/ul/li[1]/span #para 2022
        try: 
            driver.find_element_by_xpath("//*[@id='browser']/li[9]/ul/li["+s+"]/ul/li["+l+"]/span/a").click() #//*[@id="browser"]/li[1]/ul/li[2]/span ##Hacer un bucle luego
                #//*[@id="browser"]/li[9]/ul/li[2]/ul/li[2]/span/a  #Febrero
                # //*[@id="browser"]/li[9]/ul/li[2]/ul/li[3]/span/a  #Marzo
                # //*[@id="browser"]/li[9]/ul/li[2]/ul/li[11]/span/a
                # //*[@id="browser"]/li[9]/ul/li[4]/ul/li[8]/span/a  # Agotos 2019
                # //*[@id="browser"]/li[9]/ul/li[4]/ul/li[9]/span/a #setiembre 2019
        except Exception:
             continue   #Noviembre y diciembre no jala bien
        import time
        time.sleep(1)   
        window_after = driver.window_handles[1] ###Ubicación 1 pues es la ventana 2
        driver.switch_to.window(window_after)  
        urlwd=driver.current_url
        print(urlwd) 
        time.sleep(2)""" 
        
"""import tabula as tb
        df= tb.read_pdf(urlwd, pages=1, area=(247, 138,823,2080), output_format="dataframe") #area=[box]
        df.to_excel('D:\\Webscraping\\Python\\df'+j+'2.xlsx', index = True)"""
        
        

#driver.get("https://becas.osinergmin.gob.pe/seccion/centro_documental/hidrocarburos/SCOP/SCOP-DOCS/2022/01-Demanda-Nacional-Combustibles-Liquidos-Enero-2022.pdf")

"""from tabula import read_pdf
import tabula as tb
try: 
    df1=read_pdf(urlwd, pages=1, encoding='latin1') #, output_format="json"
    print(df1)
except Exception as e:
    print(e)


box = [304, 24, 695, 589]#Tabula needs the area to be specified as the top(y1), left (x1) , bottom (y2) and right (x2) distance
fc = 28.28
         
for i in range(0, len(box)):
    box[i] *= fc
df3 = tb.read_pdf(urlwd, pages=1, area=(247, 138,823,2080), output_format="dataframe") #area=[box]



df=df3[0]
df.to_excel('D:\\Webscraping\\Python\\df2.xlsx', index = True)
#df.to_excel('df1.xlsx', index = True)"""


