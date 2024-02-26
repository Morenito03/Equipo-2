from animal import Animal
class Pez(Animal):
   def __init__(self, cantidad, periodo_gestacion, nombre_cientifico, nombre_comun, region_procedencia, jaula, patio, cantidad_aletas):
      super().__init__(cantidad, periodo_gestacion, nombre_cientifico, nombre_comun, region_procedencia, jaula, patio)
      self.cantidad_aletas = cantidad_aletas
   def mostrar(self):
        print(f"Nombre:{self.nombre_comun}.")
        print(f"Nombre Cientifico: {self.nombre_cientifico}.")
        print(f"Cantidad de Aletas: {self.cantidad_aletas}.")
        print(f"Jaula: '{self.jaula.jaula}' - Patio: {self.jaula.patio}.")
        print(f"Procedencia: {self.region_procedencia}.")
        print(f"Gestacion: {self.periodo_gestacion} meses.")
        