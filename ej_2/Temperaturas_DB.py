from ej_2.clases import ArbolAVL
from ej_2.clases import Iterador
from datetime import datetime 

#%%

class Temperaturas_DB:
    
    def __init__(self):
        self.mediciones = ArbolAVL()
        self.tamano = 0
        
    def __str__(self):
        lista=[]
        for nodo in self.mediciones:
            lista.append([str(nodo.clave.date()), nodo.carga_util])
        return str(lista)

    def __iter__(self):
        return str(self.mediciones)
    
    def __len__(self):
        return len(self.mediciones)

#%%        

    """Método que agrega a la base de datos una clave y un valor 
    (en este caso, fecha y temperatura, respectivamente), los cuales
    se pasan por parámetro."""
    def guardar_temperatura(self,fecha,temperatura):
        convertir_fecha = datetime.strptime(fecha,"%d/%m/%Y")
        self.mediciones.agregar(convertir_fecha,temperatura)
        self.tamano += 1
        
    """Método que retorna el valor (temperatura) en una fecha exacta.
    Recibe por parámetro una clave (fecha)."""
    def devolver_temperatura(self,fecha):
        convertir_fecha = datetime.strptime(fecha,"%d/%m/%Y")
        temp = self.mediciones.obtener(convertir_fecha)
        return temp
    
    """Método que retorna, dentro de un rango de fechas, la máxima 
    temperatura registrada. Se pasa por parámetro dos claves (fechas)."""        
    def max_temp_rango(self,fecha1, fecha2):
        f_uno = datetime.strptime(fecha1, "%d/%m/%Y")
        f_dos = datetime.strptime(fecha2, "%d/%m/%Y")
        temp_max = self.mediciones.obtener(f_uno)  #max_temp contiene la temperatura
        
        ITERADOR = Iterador(self.mediciones, f_uno)
        for i in ITERADOR:
            if i.clave <= f_dos:
                if i.carga_util > temp_max:
                    temp_max = i.carga_util 
            else:
                break
        return temp_max
    
    
    """Método que retorna, dentro de un rango de fechas, la mínima 
    temperatura registrada. Se pasa por parámetro dos claves (fechas)."""
    def min_temp_rango(self,fecha1, fecha2):
        f_uno = datetime.strptime(fecha1, "%d/%m/%Y")
        f_dos = datetime.strptime(fecha2, "%d/%m/%Y")
        temp_min = self.mediciones.obtener(f_uno)
        ITERADOR = Iterador(self.mediciones, f_uno)
        for i in ITERADOR:
            if i.clave <= f_dos:
                if i.carga_util < temp_min:
                    temp_min = i.carga_util
        return temp_min
    
    
    """Método que devuelve la primer y última temperatura en un rango
    de fecha. Se pasa por parámetro dos claves (fechas)"""
    def temp_extremos_rango(self,fecha1,fecha2):
        min_ = self.min_temp_rango(fecha1, fecha2)
        max_ = self.max_temp_rango(fecha1, fecha2)
        # return f" MINIMO: {min_} MÁXIMO: {max_}"
        return min_,max_
    
    
    """Método para borrar una temperatura (y por lo tanto una fecha) del
    árbol. Se recibe por parametro la clave a borrar (fecha)"""        
    def borrar_temperatura(self,fecha):
        fecha_conv = datetime.strptime(fecha, "%d/%m/%Y")
        self.mediciones.eliminar(fecha_conv) 
        self.tamano -= 1
    
    
    """Método para mostrar la totalidad de temperaturas 
    medidas entre una fecha y otra."""
    def mostrar_temperaturas(self,fecha1,fecha2):
        f_uno = datetime.strptime(fecha1, "%d/%m/%Y")
        Iter = Iterador(self.mediciones,f_uno)
        lista=[]
        for i in Iter:
                lista.append((str(i.clave.date()),i.valor))
        return(lista)
    
    """Método que retorna un entero (int) que representa el
    tamaño del árbol. No recibe ningún dato por parámetro."""
    def mostrar_cantidad_muestras(self):
        cantidad = self.tamano
        return cantidad
    
#%%

if __name__ == "__main__":
    obj=Temperaturas_DB()
    obj.guardar_temperatura("20/10/2022",30)
    obj.guardar_temperatura("21/09/2022",27)
    obj.guardar_temperatura("06/08/2022",26)
    obj.guardar_temperatura("29/10/2022",25)
    obj.guardar_temperatura("07/03/2022",23)
    obj.guardar_temperatura("09/01/2022",22)
    obj.guardar_temperatura("15/06/2022",12)
    obj.guardar_temperatura("19/07/2022",10)
    obj.guardar_temperatura("03/12/2022",5)

    # ----------------------------------------------------------------------
    print("Delvolver temp",obj.devolver_temperatura("29/10/2022"))
    # -------------------------------------------------------------------
    print("MAX temp en un rango",obj.max_temp_rango("07/03/2022", "29/10/2022"))
    # ----------------------------------------------------------------------
    print("MIN temp en un rango",obj.min_temp_rango("07/03/2022", "29/10/2022"))
    # -------------------------------------------------------------------
    print("Borrar temperatura"), obj.borrar_temperatura("29/10/2022")
    # -------------------------------------------------------------------
    print("max y min en un rango",obj.temp_extremos_rango("07/03/2022", "29/10/2022"))
    # -------------------------------------------------------------------
    print("mostrar temps en un rango"),obj.mostrar_temperaturas("07/03/2022", "29/10/2022")
    # -------------------------------------------------------------------
    print("mostrar cantidad de muestras registradas", obj.mostrar_cantidad_muestras())
    # -------------------------------------------------------------------    
    print(obj) 
