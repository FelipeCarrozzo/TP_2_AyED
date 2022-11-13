# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:01:49 2022

@author: Juan Pablo
"""
from Trabajo_Practico2.ej_3.modulos.monticulo_min import MonticuloBinarioMin

def dijkstra_min(un_grafo,inicio):
    cp = MonticuloBinarioMin()
    
    cp.construir_monticulo([(v.obtener_distancia(),v) for v in un_grafo])
    for vertice in cp:
        vertice.asignar_distancia(99999)
    inicio.asignar_distancia(0)
    while not cp.esta_vacia():
        
        vertice_actual = cp.eliminar_min()
        
        for vertice_siguiente in vertice_actual.obtener_conexiones():
            
            nueva_distancia = vertice_actual.obtener_distancia + vertice_actual.obtener_ponderacion(vertice_siguiente)
            
            if nueva_distancia < vertice_siguiente.obtener_distancia():    
                vertice_siguiente.asignar_distancia(nueva_distancia)
                vertice_siguiente.asignar_predecesor(vertice_actual)
                cp.decrementar_clave(vertice_siguiente,nueva_distancia)