# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:36:21 2022

@author: alumno
"""

from  Temperaturas_DB import ArbolAVL, NodoArbol 
from datetime import datetime 

#%%

class Temperaturas_DB:
    
    def __init__(self):
        self.mediciones = ArbolAVL()
        
    def __str__(self):
        return str(self.mediciones)
    def __iter__(self):
        return str(self.mediciones)

#%%        
    def guardar_temperatura(self,temperatura,fecha):
        self.mediciones.agregar(temperatura, fecha)
        
    def devolver_temperatura(self,fecha):
        self.mediciones.obtener(fecha)
        
    def max_temp_rango(self,fecha1, fecha2):
        f_uno = datetime.strptime(fecha1, "%Y/%m/%d")
        f_dos = datetime.strptime(fecha2, "%Y/%m/%d")
        temp_max = self.mediciones.obtener(f_uno)
        ITERADOR = iterador(self.mediciones, f_dos)
        
        for i in ITERADOR:
            if f_uno <= nodo.clave <= f_dos:
                if nodo.carga_util > temp_max:
                    temp_max = nodo.carga_util
        return temp_max
    
    def min_temp_rango(self,fecha1, fecha2):
        f_uno = datetime.strptime(fecha1, "%Y/%m/%d")
        f_dos = datetime.strptime(fecha2, "%Y/%m/%d")
        temp_max = self.mediciones.obtener(f_uno)
        ITERADOR = iterador(self.mediciones, f_dos)
        
        for i in ITERADOR:
            if f_uno >= nodo.clave >= f_dos:
                if nodo.carga_util < temp_max:
                    temp_max = nodo.carga_util
        return temp_max
        
    