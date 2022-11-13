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
    
    def __contains__(self, vertice):
        for par in self.lista_monticulo:
            if par[1] == vertice:
                return True
            return False
    
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
        
    def esta_vacia(self):
        if self.lista_monticulo == [0]:
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
            
    def eliminar_max(self):
        valor_sacado = self.lista_monticulo[1][1]
        self.lista_monticulo[1] = self.lista_monticulo[self.tamano_actual]
        self.tamano_actual = self.tamano_actual - 1
        self.lista_monticulo.pop()
        self.infilt_abajo(1)
        return valor_sacado
            
    def construir_monticulo(self,unaLista):
        i = len(unaLista) // 2
        self.tamano_actual = len(unaLista)
        self.lista_monticulo = [0] + unaLista[:]
        while (i > 0):
            self.infilt_abajo(i)
            i = i - 1
            
    def decrementar_clave(self, vertice, nueva_distancia):
        for i in range(1,self.tamano_actual):
            if self.lista_monticulo[i][1].id == vertice.id:
                self.lista_monticulo[i] = self.lista_monticulo[self.tamano_actual]
                self.tamano_actual = self.tamano_actual - 1
                self.lista_monticulo.pop()
                self.infilt_abajo(1)
                self.insertar((nueva_distancia, vertice))
        


