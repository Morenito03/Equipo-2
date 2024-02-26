from animal import Animal

class Ave(Animal):
   def __init__(self, cantidad, periodo_gestacion, nombre_cientifico, nombre_comun, region_procedencia, jaula, patio, color_plumas):
      super().__init__(cantidad, periodo_gestacion, nombre_cientifico, nombre_comun, region_procedencia, jaula, patio)
      self.color_plumas = color_plumas
   def mostrar(self):
      print(f"Nombre:{self.nombre_comun}.")
      print(f"Nombre Cientifico: {self.nombre_cientifico}.")
      print(f"Color Plumaje: {self.color_plumas}.")
      print(f"Jaula: '{self.jaula.jaula}' - Patio: {self.jaula.patio}.")
      print(f"Procedencia: {self.region_procedencia}.")
      print(f"Gestacion: {self.periodo_gestacion} meses.")
        