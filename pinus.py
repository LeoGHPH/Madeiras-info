from madeira import Madeira
class Pinus(Madeira):
    def __init__(self, tipo, peso, preco, data, total):
        super().__init__(tipo, peso, preco, data)
        self._data=data

    def getData(self):
        return self._data
    
    def setData(self, data):
        self._data=data

       
        


   

    def mostrar(self):
        return (f"Data: {self.getData()}, Tipo de madeira: {self.getTipo()}, Peso: {self.getPeso()}, Preço {self.getPreco()}, TOTAL DA PESAGEM: {self.getTotal()}")

p = Pinus("Pinus", "x ton", 11, "xx/xx/xx", "x")