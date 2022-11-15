from Trabajo_Practico2.ej_3.modulos.monticulo_min import MonticuloBinarioMin
from Trabajo_Practico2.ej_3.modulos.dijsktra_max import dijkstra_de_pmax
from Trabajo_Practico2.ej_3.modulos.dijsktra_min import dijkstra_de_min

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
        
    def __lt__(self, otro):
        return True
    
class Grafo:
    def __init__(self):
        self.lista_vertices = {}
        self.num_vertices = 0
   
    def __getitem__(self,clave):
        return self.obtener_vertice(clave)
    
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
    

if __name__ == "__main__":
    
    """ PRUEBAS """
    grafo = Grafo()
    
    # grafo.agregar_vertice('a')
    # grafo.agregar_vertice('b')
    # grafo.agregar_arista('a', 'b', 1)
    
    grafo.agregar_arista("a", "b", 5)
    grafo.agregar_arista("a", "c", 2)
    grafo.agregar_arista("a", "e", 7)
    grafo.agregar_arista("b", "e", 5)
    grafo.agregar_arista("c", "a", 3)
    grafo.agregar_arista("b", "c", 5)
    grafo.agregar_arista("e", "a", 5)
    grafo.agregar_arista("d", "e", 1)

    # print(grafo.obtener_vertice("a").obtener_ponderacion(grafo.obtener_vertice("b")))
    # vecinos = grafo.obtener_vertice("a").obtener_conexiones()
    # print("\n") 
    
    for i in grafo:
        print(i)
        
    inicio=grafo.obtener_vertice("a")
    # print(inicio)
    dijkstra_de_min(grafo,inicio)
    
    
    
    for i in grafo:
        print(i.dist)
    
