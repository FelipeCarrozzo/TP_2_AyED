from Ej_1.monticulo import MonticuloBinario
from ej_3.modulos.monticulo_max import MonticuloBinarioMax

class Vertice:
    def __init__(self,clave,dist=9999):
        self.id = clave
        self.conectado_a = {}
        self.dist = dist
        self.predecesor = None

    def asignar_distancia(self,valor):
        self.dist = valor
        
    def obtener_distancia(self):
        return self.dist
    
    def agregar_vecino(self,vecino,ponderacion=0):
        self.conectado_a[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectado_a: ' + str([x.id for x in self.conectado_a])

    def obtener_conexiones(self):
        return self.conectado_a.keys()

    def obtener_id(self):
        return self.id

    def obtener_ponderacion(self,vecino):
        return self.conectado_a[vecino]
    
    def obtener_dist(self,vertice):
        return self.dist
    
    def asignar_predecesor(self, predecesor):
        self.predecesor = predecesor


#%%

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

    def agregar_arista(self,de,a,ponderacion=0):
        if de not in self.lista_vertices:
            nv = self.agregar_vertice(de)
        if a not in self.lista_vertices:
            nn = self.agregar_vertice(a)
        self.lista_vertices[de].agregar_vecino(self.lista_vertices[a], ponderacion)

    def obtener_vertices(self):
        return self.lista_vertices.keys()

    def __iter__(self):
        return iter(self.lista_vertices.values()) 
    
    
        


    def dijkstra_de_max(unGrafo,inicio):
        cp = MonticuloBinarioMax()
        inicio.asignar_distancia(0)
        cp.construir_monticulo([(v.obtener_distancia(),v) for v in unGrafo])
        while not cp.esta_vacia():
            vertice_actual = cp.eliminar_max()
            for vertice_siguiente in vertice_actual.obtener_conexiones():
                nueva_distancia = vertice_actual.obtener_distancia() \
                        + vertice_actual.obtener_ponderacion(vertice_siguiente)
                if nueva_distancia < vertice_siguiente.obtener_distancia():
                    vertice_siguiente.asignar_distancia( nueva_distancia )
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

    for i in grafo:
        print(i)
   
    grafo.dijkstra_de_max(grafo.obtener_vertice("a"))
    
    
    
