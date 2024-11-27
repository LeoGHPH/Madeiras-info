from madeira import Madeira
class Eucalipto(Madeira):
    def __init__(self, tipo, peso, preco):
        super().__init__(tipo, peso)
        self._preco=preco

    def setPreco(self, preco):
        self._preco=preco
  
    def getPreco(self):
        return self._preco

    def mostrar(self):
        return (f"Tipo de madeira: {self.getTipo()}, Peso: {self.getPeso()}, Preço {self.getPreco()}")

e = Eucalipto("Eucalipto", "x ton", 11)