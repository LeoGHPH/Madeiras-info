from abc import ABC, abstractmethod

class Madeira(ABC):
  def __init__(self, tipo, peso, preco):
    self._tipo=tipo
    self._peso=peso
    self._preco=preco
   
   
    
    


  def getTipo(self):
    return self._tipo

  def getPeso(self):
    return self._peso
  
  def getPreco(self):
    return self._preco
  
  
  
  

  def setTipo(self, tipo):
    self._tipo=tipo

  def setPeso(self, peso):
    self._peso=peso

  def setPreco(self, preco):
    self._preco=preco

  

  
  
  
  


  
@abstractmethod
def mostrar(self):
    pass