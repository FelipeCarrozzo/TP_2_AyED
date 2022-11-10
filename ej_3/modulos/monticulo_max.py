# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 12:35:12 2022

@author: Juan Pablo
"""

class MonticuloBinarioMax:
    def __init__(self):
        self.lista_monticulo = [0]
        self.tamano_actual = 0
    
    def __iter__(self):
        for i in self.lista_monticulo:
            yield i
        
    def __str__(self):
        return str(self.lista_monticulo)
    
    def __len__(self):
        return self.tamano_actual
    
    def infilt_arriba(self,i):
        while i // 2 > 0:
          if self.lista_monticulo[i] > self.lista_monticulo[i // 2]:
             tmp = self.lista_monticulo[i // 2]
             self.lista_monticulo[i // 2] = self.lista_monticulo[i]
             self.lista_monticulo[i] = tmp
          i = i // 2 
    
    def insertar(self,k):
        self.lista_monticulo.append(k)
        self.tamano_actual = self.tamano_actual + 1
        self.infilt_arriba(self.tamano_actual) 
        
    def eliminar_max(self):
        valorSacado = self.lista_monticulo[1][1]
        self.lista_monticulo[1] = self.lista_monticulo[self.tamano_actual]
        self.tamano_actual = self.tamano_actual - 1
        self.lista_monticulo.pop()
        self.infilt_abajo(1)
        return valorSacado
    
    def esta_vacia(self):
        if self.lista_monticulo == []:
            return True
        else:
            return False
    
    def infilt_abajo(self,i):
        while (i * 2) <= self.tamano_actual:
            hm = self.hijo_max(i)
            if self.lista_monticulo[i] < self.lista_monticulo[hm]:
                tmp = self.lista_monticulo[i]
                self.lista_monticulo[i] = self.lista_monticulo[hm]
                self.lista_monticulo[hm] = tmp
            i = hm
            
    def hijo_max(self,i):
        if i * 2 + 1 > self.tamano_actual:
            return i * 2
        else:
            if self.lista_monticulo[i*2] > self.lista_monticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def construir_monticulo(self,unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infilt_abajo(i)
            i = i - 1
            
    def decrementar_clave(self, valor, nueva_clave):
        hecho = False
        i = 1
        clave = 0
        
        '''Busco cada valor (Vertice)'''
        while not hecho and i <= self.tamano_actual:
            if self.listaMonticulo[i][1] == valor:
                hecho = True
                clave = i
            else:
                i = i + 1
        
        if clave > 0:
            self.lista_monticulo[clave] = (nueva_clave, self.lista_monticulo[clave][1])
            self.infilt_arriba(clave)


    