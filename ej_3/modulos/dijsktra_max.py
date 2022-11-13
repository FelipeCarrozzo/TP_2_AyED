from ej_3.modulos.monticulo_max import MonticuloBinarioMax
from ej_3.modulos.grafoyvertice import Grafo, Vertice
  
def dijkstra_max(self,un_grafo,inicio):
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
        
        vertice_actual = cp.eliminar_max()
        
        for vertice_siguiente in vertice_actual.obtener_conexiones():
            
            nueva_distancia = min(vertice_actual.obtener_distancia(),vertice_actual.obtener_ponderacion(vertice_siguiente))
            
            if nueva_distancia > vertice_siguiente.obtener_distancia():    
                vertice_siguiente.asignar_distancia(nueva_distancia)
                vertice_siguiente.asignar_predecesor(vertice_actual)
                cp.decrementar_clave(vertice_siguiente,nueva_distancia)