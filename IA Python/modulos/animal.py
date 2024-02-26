from abc import abstractmethod

#Clase Jaula
class Jaula:
   def __init__(self,jaula,patio):
      self.jaula = jaula
      self.patio = patio
# Clase Abstracta para TODO tipo de animal
class Animal():
    
   def __init__(self, cantidad, periodo_gestacion, nombre_cientifico, nombre_comun, region_procedencia,jaula,patio):
      self.cantidad           = cantidad
      self.periodo_gestacion  = periodo_gestacion
      self.nombre_cientifico  = nombre_cientifico
      self.nombre_comun       = nombre_comun
      self.region_procedencia = region_procedencia
      self.jaula              = Jaula(jaula,patio)

   @abstractmethod    
   def mostrar(self):
    pass
