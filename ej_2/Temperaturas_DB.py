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
    def mostrar_temperaturas(self, p_fecha1, p_fecha2):
        fecha1_dt = datetime.strptime(p_fecha1, "%Y/%m/%d")
        fecha2_dt = datetime.strptime(p_fecha2, "%Y/%m/%d")
            
        iterador = Iterador(self.mediciones, fecha1_dt)
        listado=[]
            
        for nodo in iterador:
            if  fecha1_dt <= nodo.clave <= fecha2_dt:
                listado.append([str(nodo.clave.date()), nodo.carga_util])
        print(listado) #uestra por consola un listado de las mediciones 




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
        f_uno = datetime.strptime(fecha1, "%Y/%m/%d")
        f_dos = datetime.strptime(fecha2, "%Y/%m/%d")
        temp_max = self.mediciones.obtener(f_uno)
        ITERADOR = Iterador(self.mediciones, f_dos)
        l_temp = []
        for i in ITERADOR:
            if f_uno >= NodoArbol.clave >= f_dos:
                conversion = [str(NodoArbol.clave.date()), NodoArbol.carga_util]
                l_temp.append(conversion)
                if NodoArbol.carga_util < temp_max:
                    temp_max = NodoArbol.carga_util
        return temp_max
    
    

        
        
#%%

if __name__ == "__main__":
    obj=Temperaturas_DB()
    obj.guardar_temperatura(30,"2022/10/20")
    obj.guardar_temperatura(27,"2022/10/21")
    obj.guardar_temperatura(26,"2022/10/22")
    obj.guardar_temperatura(25,"2022/10/23")
    obj.guardar_temperatura(23,"2022/10/24")
    obj.guardar_temperatura(15,"2022/10/25")
    print(obj.mostrar_temperaturas("2022/10/20", "2022/10/25"))