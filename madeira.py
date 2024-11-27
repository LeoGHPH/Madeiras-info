from abc import ABC, abstractmethod

class Madeira(ABC):
  def __init__(self, tipo, peso):
    self._tipo=tipo
    self._peso=peso
    

  def getTipo(self):
    return self._tipo

  def getPeso(self):
    return self._peso

  def setNome(self, tipo):
    self._nome=tipo

  def setIdade(self, peso):
    self._idade=peso

  
@abstractmethod
def mostrar(self):
    pass