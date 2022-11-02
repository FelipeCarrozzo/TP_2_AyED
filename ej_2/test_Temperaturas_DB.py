import unittest 
from ej_2.Temperaturas_DB import Temperaturas_DB
import random
from datetime import datetime


class TestTemperaturasDB(unittest.TestCase):
    """Test de la clase Temperaturas_DB"""
    
    def setUp(self):
        self.temp = Temperaturas_DB()
        self.cant_temp = 0
        self.lista_fecha = ["21/10/2022","22/10/2022","23/10/2022","24/10/2022"]
        self.temperatura = [24,27,14,10]
        self.fechamin = "21/10/2022"
        self.fechamax = "24/10/2022"
        self.fecha_temp = ("21/10/2022",24)
        
    
    
    def test_guardar_temperatura(self):
        for fecha,temp in zip (self.lista_fecha,self.temperatura):
            self.temp.guardar_temperatura(fecha, temp)   
            self.cant_temp +=1
        self.assertEqual(self.temp.tamano, self.cant_temp)
        #LISTO


    def test_devolver_temperatura(self):
        
        self.temp.guardar_temperatura("21/10/2022",24)
        self.temp.guardar_temperatura("22/10/2022",27)
        self.temp.guardar_temperatura("23/10/2022",14)
        self.temp.guardar_temperatura("24/10/2022",10)
        dev = self.temp.devolver_temperatura("21/10/2022")
        self.assertEqual(self.fecha_temp[1],dev)
        #LISTO
        
        
    def test_max_temp_rango(self):
        mayor = 27
        self.fechamin = "21/10/2022"
        self.fechamax = "24/10/2022"
        self.temp.guardar_temperatura("21/10/2022",24)
        self.temp.guardar_temperatura("22/10/2022",27)
        self.temp.guardar_temperatura("23/10/2022",14)
        self.temp.guardar_temperatura("24/10/2022",10)
        
        dev = self.temp.max_temp_rango(self.fechamin, self.fechamax)
        self.assertEqual(mayor, dev)
        
        
        
    def test_min_temp_rango(self):
        mini = 10
        self.fechamin = "21/10/2022"
        self.fechamax = "24/10/2022"
        self.temp.guardar_temperatura("21/10/2022",24)
        self.temp.guardar_temperatura("22/10/2022",27)
        self.temp.guardar_temperatura("23/10/2022",14)
        self.temp.guardar_temperatura("24/10/2022",10)
        
        dev = self.temp.min_temp_rango(self.fechamin, self.fechamax)
        self.assertEqual(mini, dev)
        
    
    
    def test_temp_extremos_rango(self):
        mini = 10
        mayor = 27
        self.temp.temp_extremos_rango(self.fechamin, self.fechamax)


    # def test_borrar_temperatura(self):
    #     self.temp.borrar_temperatura(self.fechamax)
        
        
        
    # def test_mostrar_temperaturas_rango(self):
    #     self.temp.mostrar_temperaturas_rango(self.fechamin, self.fechamax)
        
    # def test

if __name__ == "__main__":
    unittest.main()
        
