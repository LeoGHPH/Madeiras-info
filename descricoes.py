from madeira import Madeira
class Descricao(Madeira):
    def __init__(self, tipo, peso, preco, data):
        super().__init__(tipo, peso, preco)
        self._data=data
      

    def setData(self, data):
        self._data=data
    


    def getData(self):
        return self._data
    
    
  
  
    
    def mostrar(self):
        return (f"Data: {self.getData()}")

d = Descricao("Eucalipto", "x", "x", "xx/xx/xxxx",  )
print(d.mostrar())

