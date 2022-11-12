# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:13:52 2022

@author: Juan Pablo
"""
# from Ej_1.monticulo import MonticuloBinario
# from ej_3.modulos.monticulo_max import MonticuloBinarioMax

class MonticuloBinarioMax:
    def __init__(self):
        self.lista_monticulo = [(0,0)]
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
          if self.lista_monticulo[i][0] > self.lista_monticulo[i // 2][0]:
             tmp = self.lista_monticulo[i // 2]
             self.lista_monticulo[i // 2] = self.lista_monticulo[i]
             self.lista_monticulo[i] = tmp
          i = i // 2 
    
    def insertar(self,k):
        self.lista_monticulo.append(k)
        self.tamano_actual = self.tamano_actual + 1
        self.infilt_arriba(self.tamano_actual) 
        
    def eliminar_max(self):
        valor_sacado = self.lista_monticulo[1][1]
        self.lista_monticulo[1] = self.lista_monticulo[self.tamano_actual]
        self.tamano_actual = self.tamano_actual - 1
        self.lista_monticulo.pop()
        self.infilt_abajo(1)
        return valor_sacado
    
    def esta_vacia(self):
        if self.lista_monticulo == []:
            return True
        else:
            return False
    
    def infilt_abajo(self,i):
        while (i * 2) <= self.tamano_actual:
            hm = self.hijo_max(i)
            if self.lista_monticulo[i][0] < self.lista_monticulo[hm][0]:
                tmp = self.lista_monticulo[i]
                self.lista_monticulo[i] = self.lista_monticulo[hm]
                self.lista_monticulo[hm] = tmp
            i = hm
            
    def hijo_max(self,i):
        if i * 2 + 1 > self.tamano_actual:
            return i * 2
        else:
            if self.lista_monticulo[i*2][0] > self.lista_monticulo[i*2+1][0]:
                return i * 2
            else:
                return i * 2 + 1
            
    def construir_monticulo(self,unaLista):
        i = len(unaLista) // 2
        self.tamano_actual = len(unaLista)
        self.lista_monticulo = [0] + unaLista[:]
        while (i > 0):
            self.infilt_abajo(i)
            i = i - 1
            
    def decrementar_clave(self, valor, nueva_clave):
        hecho = False
        i = 1
        clave = 0
        
        '''Busco cada valor (Vertice)'''
        while not hecho and i <= self.tamano_actual:
            if self.lista_monticulo[i][1] == valor:
                hecho = True
                clave = i
            else:
                i = i + 1
        
        if clave > 0:
            self.lista_monticulo[clave] = (nueva_clave, self.lista_monticulo[clave][1])
            self.infilt_arriba(clave)
class Vertice:
    def __init__(self,clave,dist=0):
        self.id = clave
        self.conectado_a = {}
        self.dist = dist
        self.predecesor = None

    def asignar_distancia(self,valor):
        self.dist = valor
        
    def obtener_distancia(self):
        return self.dist
    
    def agregar_vecino(self,vecino,ponderacion):
        self.conectado_a[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectado_a: ' + str([x.id for x in self.conectado_a]) + str([self.obtener_ponderacion(v) for v in self.conectado_a])

    def obtener_conexiones(self):
        return self.conectado_a.keys()

    def obtener_id(self):
        return self.id

    def obtener_ponderacion(self,vecino):
        return self.conectado_a[vecino]
    
    def asignar_predecesor(self, predecesor):
        self.predecesor = predecesor
    
class Grafo:
    def __init__(self):
        self.lista_vertices = {}
        self.num_vertices = 0

    def agregar_vertice(self,clave):
        self.num_vertices = self.num_vertices + 1
        nuevo_vertice = Vertice(clave)
        self.lista_vertices[clave] = nuevo_vertice
        return nuevo_vertice

    def obtener_vertice(self,n):
        if n in self.lista_vertices:
            return self.lista_vertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.lista_vertices

    def agregar_arista(self,de,a,ponderacion):
        if de not in self.lista_vertices:
            nv = self.agregar_vertice(de)
        if a not in self.lista_vertices:
            nn = self.agregar_vertice(a)
        self.lista_vertices[de].agregar_vecino(self.lista_vertices[a],ponderacion)

    def obtener_vertices(self):
        return self.lista_vertices.keys()

    def __iter__(self):
        return iter(self.lista_vertices.values()) 
    
    
        
    def dijkstra_de_max(un_grafo,inicio):
        """
        Esta función obtiene 

        Parameters
        ----------
        un_grafo : TYPE
            DESCRIPTION.
        inicio : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        cp = MonticuloBinarioMax()
        inicio.asignar_distancia(9999)
        cp.construir_monticulo([(v.obtener_distancia(),v) for v in un_grafo])
        while not cp.esta_vacia():
            print(cp)
            vertice_actual = cp.eliminar_max()
            
            
            for vertice_siguiente in vertice_actual.obtener_conexiones():
                
                nueva_distancia = min(vertice_actual.obtener_distancia(),vertice_actual.obtener_ponderacion(vertice_siguiente))
                
                if nueva_distancia > vertice_siguiente.obtener_distancia():    
                    vertice_siguiente.asignar_distancia(nueva_distancia)
                    vertice_siguiente.asignar_predecesor(vertice_actual)
                    cp.decrementar_clave(vertice_siguiente,nueva_distancia)
                        
                    
    # def dijkstra(un_grafo,inicio):
    #     cp = ColaPrioridad()
    #     inicio.asignar_distancia(0)
    #     cp.construir_monticulo([(v.obtener_distancia(),v) for v in unGrafo])
    #     while not cp.estaVacia():
    #         vertice_actual = cp.eliminarMin()
    #         for vertice_siguiente in vertice_actual.obtener_conexiones():
    #             nueva_distancia = vertice_actual.obtener_distancia() \
    #                     + vertice_actual.obtener_ponderacion(vertice_siguiente)
    #             if nueva_distancia < vertice_siguiente.obtener_distancia():
    #                 vertice_siguiente.asignar_distancia( nueva_distancia )
    #                 vertice_siguiente.asignar_predecesor(vertice_actual)
    #                 cp.decrementarClave(vertice_siguiente,nueva_distancia)
    
if __name__ == "__main__":
    
    grafo = Grafo()
    
    # grafo.agregar_vertice('a')
    # grafo.agregar_vertice('b')
    # grafo.agregar_arista('a', 'b', 1)
    
    grafo.agregar_arista("a", "b", 5)
    grafo.agregar_arista("a", "c", 2)
    grafo.agregar_arista("a", "e", 7)
    grafo.agregar_arista("b", "e", 5)
    grafo.agregar_arista("c", "a", 3)
    grafo.agregar_arista("b", "d", 5)
    grafo.agregar_arista("e", "d", 5)
    grafo.agregar_arista("a", "c", 8)
    grafo.agregar_arista("c", "e", 1)

    print(grafo.obtener_vertice("a").obtener_ponderacion(grafo.obtener_vertice("b")))
    vecinos = grafo.obtener_vertice("a").obtener_conexiones()
    print("\n") 
    print(grafo.obtener_vertice("b").obtener_distancia())
    for v in vecinos:
        print(v.id)
    for i in grafo:
        print(i)
        
    inicio=grafo.obtener_vertice("a")
    grafo.dijkstra_de_max(grafo,inicio)
    
    
    
    for i in grafo:
        print(i)
    
