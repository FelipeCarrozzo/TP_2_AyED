from ej_3.modulos.monticulo_min import MonticuloBinarioMin

def dijkstra_de_min(un_grafo,inicio):
    """
    Esta función devuelve un grafo con los costos mínimos de viajar desde
    una ciudad inicio hacia las demas del grafo.

    Parameters
    ----------
    un_grafo : TYPE: Grafo
        Un grafo con las aristas(caminos), los vertices(ciudades) y ponderaciones(costos por ruta).
    inicio : TYPE: Vertice
        Un vertice(ciudad) inicial desde donde se quiere viajar.

    Returns
    -------
    None.

    """
    cp = MonticuloBinarioMin()         
    
    for vertice in un_grafo:
        vertice.asignar_distancia(9999)
    inicio.asignar_distancia(0)
    cp.construir_monticulo([(v.obtener_distancia(),v) for v in un_grafo])
    
    
    
    while not cp.esta_vacia():
        
        vertice_actual = cp.eliminar_min()
        #elimina la raíz, el elemento mas pequeño
        for vertice_siguiente in vertice_actual.obtener_conexiones():
            
            nueva_distancia = vertice_actual.obtener_distancia() + vertice_actual.obtener_ponderacion(vertice_siguiente)
            
            if nueva_distancia < vertice_siguiente.obtener_distancia():    
                vertice_siguiente.asignar_distancia(nueva_distancia)
                vertice_siguiente.asignar_predecesor(vertice_actual)
                cp.decrementar_clave(vertice_siguiente,nueva_distancia)