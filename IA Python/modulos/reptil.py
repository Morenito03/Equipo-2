from animal import Animal

class Reptil(Animal):
   def __init__(self, cantidad, periodo_gestacion, nombre_cientifico, nombre_comun, region_procedencia, jaula, patio, venenoso):
      super().__init__(cantidad, periodo_gestacion, nombre_cientifico, nombre_comun, region_procedencia, jaula, patio)
      self.venenoso = venenoso
   def mostrar(self):
      if self.venenoso is True:
         veneno = {"Si"}
      else: veneno = {"No"}
      print(f"Nombre:{self.nombre_comun}.")
      print(f"Nombre Cientifico: {self.nombre_cientifico}.")
      print(f"Venenoso: {veneno}.")
      print(f"Jaula: '{self.jaula.jaula}' - Patio: {self.jaula.patio}.")
      print(f"Procedencia: {self.region_procedencia}.")
      print(f"Gestacion: {self.periodo_gestacion} meses.")
        