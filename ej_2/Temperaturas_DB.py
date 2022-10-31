# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:36:21 2022

@author: alumno
"""

from ej_2.clases import ArbolAVL, NodoArbol 
from datetime import datetime 
from ej_2.clases import Iterador

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
        convertir_fecha = datetime.strptime(fecha,"%Y/%m/%d")
        self.mediciones.agregar(convertir_fecha,temperatura)
        
    def devolver_temperatura(self,fecha):
        convertir_fecha = datetime.strptime(fecha,"%Y/%m/%d")
        self.mediciones.obtener(convertir_fecha)
        
    def max_temp_rango(self,fecha1, fecha2):
        f_uno = datetime.strptime(fecha1, "%Y/%m/%d")
        f_dos = datetime.strptime(fecha2, "%Y/%m/%d")
        temp_max = self.mediciones.obtener(f_uno)
        ITERADOR = Iterador(self.mediciones, f_dos)
        
        for i in ITERADOR:
            if f_uno <= NodoArbol.clave <= f_dos:
                if NodoArbol.carga_util > temp_max:
                    temp_max = NodoArbol.carga_util
        return temp_max
    
    def min_temp_rango(self,fecha1, fecha2):
        f_uno = datetime.strptime(fecha1, "%Y/%m/%d").date()
        f_dos = datetime.strptime(fecha2, "%Y/%m/%d").date()
        temp_max = self.mediciones.obtener(f_uno)
        ITERADOR = Iterador(self.mediciones, f_dos)
        
        for i in ITERADOR:
            if f_uno >= NodoArbol.clave >= f_dos:
                if NodoArbol.carga_util < temp_max:
                    temp_max = NodoArbol.carga_util
        return temp_max
        
#%%

if __name__ == "__main__":
    obj=Temperaturas_DB()
    obj.guardar_temperatura(30,"2022/10/29")
    obj.guardar_temperatura(10,"2022/10/30")
    # obj.max_temp_rango("2022/10/29","2022/10/30")
    print(obj)