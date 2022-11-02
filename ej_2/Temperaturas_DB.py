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
        self.tamano = 0
        
    # def __str__(self):
    #     lista=[]
    #     for nodo in self.mediciones:
    #         lista.append([(nodo.clave.date()), nodo.carga_util])
    #     return str(lista)
    #pasar a la clase nodo

    
    def __iter__(self):
        return str(self.mediciones)

#%%        

    def guardar_temperatura(self,fecha,temperatura):
        convertir_fecha = datetime.strptime(fecha,"%d/%m/%Y")
        self.mediciones.agregar(convertir_fecha,temperatura)
        self.tamano += 1

        
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
        temp_min = self.mediciones.obtener(f_uno)
        Iter = Iterador(self.mediciones, f_uno)
        l_temp = []
        for i in Iter:
            if f_uno <= i.clave <= f_dos:
                # conversion = [str(i.clave.date()), i.carga_util]
                # l_temp.append(conversion)
                if i.carga_util < temp_min:
                    temp_min = i.carga_util
        return temp_min
    
    def temp_extremos_rango(self,fecha1,fecha2):
        min_ = self.min_temp_rango(fecha1, fecha2)
        max_ = self.max_temp_rango(fecha1, fecha2)
        return f" MINIMO: {min_} MÁXIMO: {max_}"        
        
    def borrar_temperatura(self,fecha_str):
        fecha_conv = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.mediciones.eliminar(fecha_conv) 
        self.tamano -= 1
    
    """Método para mostrar la totalidad de temperaturas 
    medidas entre una fecha y otra."""
    def mostrar_temperaturas_rango(self,fecha1,fecha2):
        f_uno = datetime.strptime(fecha1, "%d/%m/%Y")
        f_dos = datetime.strptime(fecha2, "%d/%m/%Y")
        Iter = Iterador(self.mediciones,f_uno)
        lista=[]
        for i in Iter:
            if f_uno <= i.clave <= f_dos:
                lista.append((str(i.clave.date()) ,i.valor))
        print(lista)
    
    
    def mostrar_cantidad_muestras(self):
        cantidad = self.mediciones.tamano
        return cantidad
        

if __name__ == "__main__":
    obj=Temperaturas_DB()
    print("Guardar Temperatura"), obj.guardar_temperatura("20/10/2022",30)
    obj.guardar_temperatura("21/10/2022",27)
    obj.guardar_temperatura("22/10/2022",26)
    obj.guardar_temperatura("23/10/2022",25)
    obj.guardar_temperatura("24/10/2022",23)
    obj.guardar_temperatura("25/10/2022",22)
    obj.guardar_temperatura("26/10/2022",12)
    obj.guardar_temperatura("27/10/2022",10)
    obj.guardar_temperatura("28/10/2022",5)
    #----------------------------------------------------------------------
    print("Delvolver temp",obj.devolver_temperatura("23/10/2022"))
    # -------------------------------------------------------------------
    print("MAX temp en un rango",obj.max_temp_rango("20/10/2022", "28/10/2022"))
    #----------------------------------------------------------------------

    print("MIN temp en un rango",obj.min_temp_rango("20/10/2022", "28/10/2022"))
    # -------------------------------------------------------------------
    print("Borrar temperatura"), obj.borrar_temperatura("25/10/2022")
    # -------------------------------------------------------------------
    print("max y min en un rango",obj.temp_extremos_rango("20/10/2022", "28/10/2022"))
    # -------------------------------------------------------------------
    print("mostrar temps en un rango"),obj.mostrar_temperaturas_rango("20/10/2022", "28/10/2022")
    
    print("mostrar cantidad de muestras registradas", obj.mostrar_cantidad_muestras())
    
 
    