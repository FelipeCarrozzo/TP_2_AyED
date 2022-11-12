class MonticuloBinario:
    
    
    def __init__(self):
        """En el incicilizador, se declaran dos variables: "lista_monticulo"
        inicializa una lista de Python con el valor cero. "tamano_actual"
        inicializa un contador en cero. Este se va a ir incremmentando en el 
        caso de que se agregue un nodo, y decrementará cuando se elimine un nodo"""
        self.lista_monticulo = [0] #el 1er elemento del monticulo simepre se inicializa con cero
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
          if self.lista_monticulo[i] < self.lista_monticulo[i // 2]:
             tmp = self.lista_monticulo[i // 2]
             self.lista_monticulo[i // 2] = self.lista_monticulo[i]
             self.lista_monticulo[i] = tmp
          i = i // 2 
    
    def insertar(self,k):
        self.lista_monticulo.append(k)
        self.tamano_actual = self.tamano_actual + 1
        self.infilt_arriba(self.tamano_actual) 
        
    def eliminar_min(self):
        valorSacado = self.lista_monticulo[1]
        self.lista_monticulo[1] = self.lista_monticulo[self.tamano_actual]
        self.tamano_actual = self.tamano_actual - 1
        self.lista_monticulo.pop()
        self.infilt_abajo(1)
        return valorSacado
    
    def infilt_abajo(self,i):
        while (i * 2) <= self.tamano_actual:
            hm = self.hijo_min(i)
            if self.lista_monticulo[i] > self.lista_monticulo[hm]:
                tmp = self.lista_monticulo[i]
                self.lista_monticulo[i] = self.lista_monticulo[hm]
                self.lista_monticulo[hm] = tmp
            i = hm
            
    def hijo_min(self,i):
        if i * 2 + 1 > self.tamano_actual:
            return i * 2
        else:
            if self.lista_monticulo[i*2] < self.lista_monticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

if __name__ == "__main__":
    mont=MonticuloBinario()
    mont.infilt_arriba(1)
    mont.insertar(2)
    mont.insertar(2)
    print(mont)
    print(mont.tamano_actual)