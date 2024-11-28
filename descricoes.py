from madeira import Madeira
class Descricao(Madeira):
    def __init__(self, tipo, peso, preco, data, total):
        super().__init__(tipo, peso, preco, data)
        self._data=data
        self._total=total

    def setData(self, data):
        self._data=data
    


    def getData(self):
        return self._data
    
    
  
  
    
    def mostrar(self):
        return (f"Data: {self.getData()}, Total {self.getTotal()}")

d = Descricao("Eucalipto", "x", "x", "xx/xx/xxxx", "x" )
print(d.mostrar())

