
from ej_3.modulos.monticulo_max import MonticuloBinarioMax
from ej_3.modulos.grafoyvertice import Grafo, Vertice

def dijkstra_de_max(unGrafo,inicio):
        cp = MonticuloBinarioMax()
        inicio.asignar_distancia(999)
        cp.construir_monticulo([(v.obtener_distancia(),v) for v in unGrafo])
        while not cp.estaVacia():
            verticeActual = cp.eliminarMin()
            for verticeSiguiente in verticeActual.obtenerConexiones():
                nuevaDistancia = verticeActual.obtenerDistancia() \
                        + verticeActual.obtenerPonderacion(verticeSiguiente)
                if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                    verticeSiguiente.asignarDistancia( nuevaDistancia )
                    verticeSiguiente.asignarPredecesor(verticeActual)
                    cp.decrementarClave(verticeSiguiente,nuevaDistancia)