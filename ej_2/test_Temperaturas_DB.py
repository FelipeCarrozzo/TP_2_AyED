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
    """El método setUp() permite definir instrucciones que se ejecutarán
    antes y después de cada método de prueba. Este será llamado 
    automáticamente para cada prueba que sea ejecutada."""
    
    
    """Se testea si el tamaño (int) de la base de datos es igual al que 
    se incrementa en cada iteración. Este está definido en el setUp."""
    def test_guardar_temperatura(self):
        for fecha,temp in zip (self.lista_fecha,self.temperatura):
            self.temp.guardar_temperatura(fecha, temp)   
            self.cant_temp +=1
        self.assertEqual(self.temp.tamano, self.cant_temp)


    """Primeramente se define una variable "fecha_temp" (fecha, temperatura),
    luego se guardan en la base de datos temperaturas y fechas. Se llama al 
    método a testear, y se comprueba con assertEqual que el retorno del método 
    (int) sea igual al segundo elemento de la variable "fecha_temp"(en este caso 
    una temperatura (int))"""
    def test_devolver_temperatura(self):
        self.temp.guardar_temperatura("21/10/2022",24)
        self.temp.guardar_temperatura("22/10/2022",27)
        self.temp.guardar_temperatura("23/10/2022",14)
        self.temp.guardar_temperatura("24/10/2022",10)
        dev = self.temp.devolver_temperatura("21/10/2022")
        self.assertEqual(self.fecha_temp[1],dev)
        
    
    
    """"""
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
        self.fechamin = "21/10/2022"
        self.fechamax = "24/10/2022"
        self.temp.guardar_temperatura("21/10/2022",24)
        self.temp.guardar_temperatura("22/10/2022",27)
        self.temp.guardar_temperatura("23/10/2022",14)
        self.temp.guardar_temperatura("24/10/2022",10)
        dev = self.temp.temp_extremos_rango(self.fechamin, self.fechamax)
        self.assertEqual(dev, (mini, mayor))


    def test_borrar_temperatura(self):
        self.temp.guardar_temperatura("21/10/2022",24)
        self.temp.guardar_temperatura("22/10/2022",27)
        self.temp.guardar_temperatura("23/10/2022",14)
        self.temp.guardar_temperatura("24/10/2022",10)
        borrar = "23/10/2022"
        self.temp.borrar_temperatura(borrar)
        buscar = self.temp.devolver_temperatura("23/10/2022")
        self.assertFalse(buscar)
        
    def test_mostrar_temperaturas(self):
        self.fechamin = "21/10/2022"
        self.fechamax = "24/10/2022"
        self.lista_temp = [("2022-10-21",24),("2022-10-22",27),
                           ("2022-10-23",14),("2022-10-24",10)]
        self.temp.guardar_temperatura("21/10/2022",24)
        self.temp.guardar_temperatura("22/10/2022",27)
        self.temp.guardar_temperatura("23/10/2022",14)
        self.temp.guardar_temperatura("24/10/2022",10)
        dev = self.temp.mostrar_temperaturas(self.fechamin, self.fechamax)
        self.assertEqual(dev,(self.lista_temp))
        
    # def test

if __name__ == "__main__":
    unittest.main()