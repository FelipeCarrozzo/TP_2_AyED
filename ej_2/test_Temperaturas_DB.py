import unittest 
from ej_2.Temperaturas_DB import Temperaturas_DB
import random
from datetime import datetime


class TestTemperaturasDB(unittest.TestCase):
    """Test de la clase Temperaturas_DB"""
    
    def setUp(self):
        self.cant_temp = 0
        self.lista_fecha = ["21/10/2022","22/10/2022","23/10/2022","24/10/2022"]
        self.temperatura = [24,27,14,10]
        self.temp = Temperaturas_DB() 
         
    def test_guardar_temperatura(self):
        for fecha,temp in zip (self.lista_fecha,self.temperatura):
            self.temp.guardar_temperatura(fecha, temp)   
            self.cant_temp +=1
        self.assertEqual(self.temp.tamano, self.cant_temp)


    def test_





if __name__ == "__main__":
    unittest.main()
        
        
