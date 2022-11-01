# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:36:21 2022

@author: alumno
"""

from ej_2.clases import NodoArbol 
from ej_2.clases import ArbolAVL
from ej_2.clases import Iterador
from datetime import datetime 


#%%

class Temperaturas_DB:
    
    def __init__(self):
        self.mediciones = ArbolAVL()
        
    def __str__(self):
        lista=[]
        for nodo in self.mediciones:
            lista.append([(nodo.clave.date()), nodo.carga_util])
        return str(lista)

    
    def __iter__(self):
        return str(self.mediciones)

#%%        

    def guardar_temperatura(self,temperatura,fecha):
        convertir_fecha = datetime.strptime(fecha,"%d/%m/%Y")
        self.mediciones.agregar(convertir_fecha,temperatura)

        
    def devolver_temperatura(self,fecha):
        convertir_fecha = datetime.strptime(fecha,"%d/%m/%Y")
        temp = self.mediciones.obtener(convertir_fecha)
        return temp
        
        
    def max_temp_rango(self,fecha1, fecha2):
        f_uno = datetime.strptime(fecha1, "%d/%m/%Y")
        f_dos = datetime.strptime(fecha2, "%d/%m/%Y")
        temp_max = self.mediciones.obtener(f_uno)
        ITERADOR = Iterador(self.mediciones, f_uno)
        l_temp = []

        for i in ITERADOR:
            if f_uno <= i.clave <= f_dos:
                conversion = [str(i.clave.date()), i.carga_util]
                l_temp.append(conversion)
                if i.carga_util > temp_max:
                    temp_max = i.carga_util
        return temp_max
    
    def min_temp_rango(self,fecha1, fecha2):
        f_uno = datetime.strptime(fecha1, "%d/%m/%Y")
        f_dos = datetime.strptime(fecha2, "%d/%m/%Y")
        temp_max = self.mediciones.obtener(f_uno)
        Iter = Iterador(self.mediciones, f_uno)
        l_temp = []
        for i in Iter:
            if f_uno <= i.clave <= f_dos:
                conversion = [str(i.clave.date()), i.carga_util]
                l_temp.append(conversion)
                if i.carga_util < temp_max:
                    temp_max = i.carga_util
        return temp_max
    
    def temp_extremos_rango(self,fecha1,fecha2):
        f_uno = datetime.strptime(fecha1, "%d/%m/%Y")
        f_dos = datetime.strptime(fecha2, "%d/%m/%Y")
        
        
    def borrar_temperatura(self,fecha):
        self.mediciones.remover(fecha) 
    
    """Método para mostrar la totalidad de temperaturas 
    medidas entre una fecha y otra."""
    def mostrar_temperaturas_rango(self,fecha1,fecha2):
        f_uno = datetime.strptime(fecha1, "%d/%m/%Y")
        f_dos = datetime.strptime(fecha2, "%d/%m/%Y")
        Iter = Iterador(self.mediciones,f_uno)
        lista=[]
        for i in Iter:
            if f_uno <= i.clave <= f_dos:
                lista.append(i.carga_util)
        print(lista)
    
    
    def mostrar_cantidad_muestras(self):
        cantidad = self.mediciones.tamano
        return cantidad
        

if __name__ == "__main__":
    obj=Temperaturas_DB()
    obj.guardar_temperatura(30,"20/10/2022")
    obj.guardar_temperatura(27,"21/10/2022")
    obj.guardar_temperatura(26,"22/10/2022")
    obj.guardar_temperatura(25,"23/10/2022")
    obj.guardar_temperatura(23,"24/10/2022")
    obj.guardar_temperatura(15,"25/10/2022")
    obj.guardar_temperatura(12,"26/10/2022")
    obj.guardar_temperatura(9,"27/10/2022")
    obj.guardar_temperatura(3,"28/10/2022")
    print(obj.devolver_temperatura("25/10/2022"))
    print()
    print("MAX",obj.max_temp_rango("20/10/2022", "28/10/2022"))
    print("MIN",obj.min_temp_rango("20/10/2022", "28/10/2022")  )  
    print(obj.borrar_temperatura("25/10/2022"))
    
    
    # (obj.mostrar_temperaturas_rango("2022/10/20", "2022/10/25"))
    
    # print(obj.mostrar_cantidad_muestras())