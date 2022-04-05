# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 22:24:11 2022

@author: Usuario
"""


import pandas as pd

df= pd.read_excel('D:\\Git-Hub\\Works\\FACILITO-OSINERGMIN\\PRECIOS MAYORISTAS\\2019\\df1-2019.xlsx')
lima2019_1= df.loc[df['DEPARTAMENTO'] == 'LIMA']

lima2019_1['Mes']= ['Enero'] #Añadimos el mes para que tenga 20 columnas y poder concatenar


for i in range(2,13): #Toma hasta el valor 12
    i=str(i)
    df= pd.read_excel('D:\\Git-Hub\\Works\\FACILITO-OSINERGMIN\\PRECIOS MAYORISTAS\\2019\\df'+i+'-2019.xlsx')
    df_lima=df.loc[df['DEPARTAMENTO'] == 'LIMA']
    if i=='1':
       j='Enero'
    if i=='2':
       j='Febrero'
    if i=='3':
       j='Marzo'
    if i=='4':
       j='Abril'
    if i=='5':
       j='Mayo'
    if i=='6':
       j='Junio'
    if i=='7':
       j='Julio'
    if i=='8':
       j='Agosto'
    if i=='9':
       j='Setiembre'
    if i=='10':
       j='Octubre'
    if i=='11':
       j='Noviembre'
    if i=='12':
       j='Diciembre'    
    df_lima['Mes']= [j]
    lima2019_1=pd.concat([lima2019_1, df_lima]) #El apendeo ya no corre

lima2019_1.to_excel('D:\\Git-Hub\\Works\\FACILITO-OSINERGMIN\\PRECIOS MAYORISTAS\\Datacons\\dfcons-2019.xlsx', index = True)
    
    #d["lima{}".format(i)]=df.loc[df['DEPARTAMENTO'] == 'LIMA']
    




"""
for value in d.values():
    
    print(type(value))
    lima2019_1.append(value)

lima2019_1.to_excel('D:\\Git-Hub\\Works\\FACILITO-OSINERGMIN\\PRECIOS MAYORISTAS\\Datacons\\dfcons-2019.xlsx', index = True)
    
type(d['lima2']) 
"""