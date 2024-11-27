from madeira import Madeira
class Descricao(Madeira):
    def __init__(self, tipo, peso, data, total):
        super().__init__(tipo, peso)
        self._data=data
        self._total=total

    def setData(self, data):
        self._data=data
    
    def setTotal(self, total):
        self._total=total
  
    def getData(self):
        return self._data
    
    def getTotal(self):
        return self._total

    def mostrar(self):
        return (f"Data: {self.getData()}, Total {self.getTotal()}")

d = Descricao("Eucalipto", "x", "xx/xx/xxxx", "x" )