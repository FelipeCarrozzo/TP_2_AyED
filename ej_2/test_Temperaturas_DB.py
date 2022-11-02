import unittest 
from ej_2.Temperaturas_DB import Temperaturas_DB
import random
from datetime import datetime


class TestTemperaturasDB(unittest.TestCase):
    """Test de la clase Temperaturas_DB"""
    
    def SetUp(self):
        self.val_aleat_min = 5
        self.val_aleat_max = 40
        self.cant_temp = 30
        self.inicio_fecha = datetime(10, 5, 2022)
        self.fin_fecha = datetime(25, 5, 2022)
        self.temp = Temperaturas_DB() 
         

    
    def test_guardar_temperatura(self):
        lista_aux = []
        for  i in range(30):
            temp = random.randint(self.val_aleat_min, self.val_aleat_max)
            fecha = self.inicio_fecha + (self.fin_fecha - self.inicio_fecha) * random.random()
            self.temp.guardar_temperatura(fecha, temp)
           
        self.assertEqual(self.temp.tamano, self.cant_temp)

if __name__ == "__main__":
    unittest.main()
        
        
