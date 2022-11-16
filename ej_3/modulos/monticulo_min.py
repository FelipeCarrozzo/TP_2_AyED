class MonticuloBinarioMin:      #Cola de Prioridad criterio mínimos
    """
    Clase que inicializa un montículo binario de mínimos.
    El montículo siempre está ordenado. Para hacer esto necesita que el 
    elemento del índice 0 esté inicializado con un 0.
    Su críterio de ordenamiento es por valores mínimos, es decir, en la 
    posición 1 se encuentra el elemento más chico de la lista.
    
    """
    def __init__(self):
        """
        La lista_monticulo almacena valores de tuplas (costo,vertice).
        El tamaño es almacenado en el atributo tamano_actual.

        Returns
        -------
        None.

        """
        self.lista_monticulo = [(0,0)]
        self.tamano_actual = 0
    

    def __iter__(self):
        for i in self.lista_monticulo:
            yield i
        
    def __str__(self):
        return str(self.lista_monticulo)
    
    def __len__(self):
        """
        Este método devuelve el tamaño de la lista del montículo.

        Returns
        -------
        TYPE: int
            Es el valor del tamaño de la lista.

        """
        return self.tamano_actual
        
    def infilt_arriba(self,i):
        """
        Este método se utiliza para cambiar la posición de un vertice que
        está rompiendo el criterio del montículo.
        Recibe un índice, y lo utiliza para comparar un vertice con su padre.
        Si el vertice es menor que su padre, ambos cambian su posición por
        la del otro.

        Parameters
        ----------
        i : TYPE: Index
            Es el índice o posición de un elemento en una lista de un monticulo.

        Returns
        -------
        None.

        """
        while i // 2 > 0:
          if self.lista_monticulo[i] < self.lista_monticulo[i // 2]:
             tmp = self.lista_monticulo[i // 2]
             self.lista_monticulo[i // 2] = self.lista_monticulo[i]
             self.lista_monticulo[i] = tmp
          i = i // 2 
    
    def insertar(self,k):
        """
        Este método recibe una tupla y lo inserta en el montículo.

        Parameters
        ----------
        k : TYPE: Tuple(dist,vertice)
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.lista_monticulo.append(k)
        self.tamano_actual = self.tamano_actual + 1
        self.infilt_arriba(self.tamano_actual) 
        
    def eliminar_min(self):
        """
        Este método elimina el "primer" elemento de un montículo. 
        El primer elemento de un montículo de mínimos siempre es el más
        chico de la lista. Este es retirado de la lista, y su lugar lo
        ocupa el último elemento agregado, el cuál, es infiltrado para abajo
        posteriormente.
        
        Returns
        -------
        valor_sacado : TYPE: dist
            Es el costo del vertice eliminado.

        """
        valor_sacado = self.lista_monticulo[1][1]
        self.lista_monticulo[1] = self.lista_monticulo[self.tamano_actual]
        self.tamano_actual = self.tamano_actual - 1
        self.lista_monticulo.pop()
        self.infilt_abajo(1)
        return valor_sacado
    
    def infilt_abajo(self,i):
        """
        Este método se utiliza para cambiar la posición de un vertice que
        está rompiendo el criterio del montículo.
        Recibe un índice, y lo utiliza para comparar un vertice con su hijo 
        menor. Si el vertice es menor que su hijo mas chico, ambos cambian su 
        posición por la del otro.

        Parameters
        ----------
        i : TYPE: Index
            Es el índice o posición de un elemento en una lista de un monticulo.

        Returns
        -------
        None.

        """
        while (i * 2) <= self.tamano_actual:
            hm = self.hijo_min(i)
            if self.lista_monticulo[i] > self.lista_monticulo[hm]:
                tmp = self.lista_monticulo[i]
                self.lista_monticulo[i] = self.lista_monticulo[hm]
                self.lista_monticulo[hm] = tmp
            i = hm
            
    def hijo_min(self,i):
        """
        Este método compara ambos vertices hijos de un vertice padre a partir
        de sus costos. La función utiliza los índices para hacer referencia a
        cada vertice. El índice del vertice padre es lo que recibe la función. 
        El vertice hijo que sea más chico será designado como el hijo_min.

        Parameters
        ----------
        i : TYPE: Index
            Es el índice del nodo padre.

        Returns
        -------
        i * 2: TYPE: Index
            Es índice del hijo izquierdo del vertice padre.
        i * 2 + 1: TYPE: Index
            Es el índice del hijo derecho del vertice padre.

        """
        if i * 2 + 1 > self.tamano_actual:
            return i * 2
        else:
            if self.lista_monticulo[i*2] < self.lista_monticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    def construir_monticulo(self,una_lista):
        """
        Este método construye un monticulo a partir de una lista. La misma
        se va ordenando segun el peso de cada valor.

        Parameters
        ----------
        unaLista : TYPE: List
            Es una lista de tuplas(dist,vertice).

        Returns
        -------
        None.

        """
        i = len(una_lista) // 2
        self.tamano_actual = len(una_lista)
        self.lista_monticulo = [0] + una_lista[:]
        while (i > 0):
            self.infilt_abajo(i)
            i = i - 1
    
    def esta_vacia(self):
        """
        Este método se utiliza para saber si la lista de un montículo
        está vacía. Recordar que para mantener la propiedad del montículo
        la lista debe tener la posición 0 ocupada, por lo tanto, está vacía
        cuando no hay ningun elemento en el índice 1.

        Returns
        -------
        bool
            Si la lista está vacía, devuelve True.
            Si la lista no está vacía devuelve False.

        """
        if self.lista_monticulo == [0]:
            return True
        else:
            return False
        
    def __lt__(self, otro):
        return True
    
    def decrementar_clave(self, valor, nueva_clave):
        """
        Este método se utiliza para asignarle una nueva distancia a un vertice.

        Parameters
        ----------
        vertice : TYPE: Vertice
            Es el Vertice al que se le va modificar su distancia
        nueva_distancia : TYPE: dist
            Es la nueva distancia del vertice.

        Returns
        -------
        None.

        """
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
        
    
    
