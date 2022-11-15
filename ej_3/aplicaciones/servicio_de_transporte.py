# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:12:21 2022

@author: Juan Pablo
"""
from ej_3.modulos.dijsktra_max import dijkstra_max
from ej_3.modulos.dijsktra_min import dijkstra_min
from ej_3.modulos.grafoyvertice import Grafo

with open ("rutas.txt", "r") as rutas:
    ciudades = []
    datos_ciudades = []
    for ruta in rutas:
        ruta = ruta.rstrip()
        de,a,peso,costo = ruta.split(",")
        datos_ruta = [de,a,int(peso),int(costo)]
        datos_ciudades.append(datos_ruta)
        
        if de not in ciudades:
            ciudades.append(de)
        if a not in ciudades:
            ciudades.append(a)
        
    
   

    
    print("Partiendo de Buenos Aires:", "\n", "De la siguiente lista de ciudades, seleccione una para conocer su máximo cuello de botella y el camino con menor costo de transporte.", "\n",ciudades)
    destino= input("Ingrese la ciudad destino:")
    
    #Dijkstra Peso Máx.

    grafo_ciudades_peso = Grafo()
        
    for i in range(len(ciudades)):
        
        grafo_ciudades_peso.agregar_arista(datos_ciudades[i][0],datos_ciudades[i][1],datos_ciudades[i][2]) 
    
    for i in grafo_ciudades_peso:
        print(i.id, i.dist)
    
    print("\n","----------------", "\n")
    
    grafo_ciudades_peso.dijkstra_de_max(grafo_ciudades_peso,grafo_ciudades_peso.obtener_vertice("CiudadBs.As."))
    
    print("\n","----------------", "\n")
    
    for i in grafo_ciudades_peso:
        print(i.id, i.dist)
        
    print("\n","----------------", "\n")
    
    peso = 0
    for i in grafo_ciudades_peso:
        if i.id == destino:
            peso = i.dist
            
            
    #Dijkstra Costos Min
    
    grafo_ciudades_costo = Grafo()
        
    for i in range(len(ciudades)):
        
        grafo_ciudades_costo.agregar_arista(datos_ciudades[i][0],datos_ciudades[i][1],datos_ciudades[i][3]) 
    
    for i in grafo_ciudades_costo:
        print(i.id, i.dist)
    
    print("\n","----------------", "\n")
    
    grafo_ciudades_costo.dijkstra_de_min(grafo_ciudades_costo,grafo_ciudades_costo.obtener_vertice("CiudadBs.As."))
    
    print("\n","----------------", "\n")
    
    for i in grafo_ciudades_costo:
        print(i.id, i.dist)
        
    print("\n","----------------", "\n")
    
    costo = 0
    for i in grafo_ciudades_costo:
        if i.id == destino:
            costo = i.dist
            
    
    #Mostrar Resultados        
    print("Para llegar a", destino,":", "\n", 
          "El peso máximo para transportar es:", peso, "\n",
          "El costo mínimo de transporte es:", costo)
    