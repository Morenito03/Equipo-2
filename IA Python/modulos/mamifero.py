from animal import Animal

class Mamifero(Animal):
    def __init__(self, cantidad, periodo_gestacion, nombre_cientifico, nombre_comun, region_procedencia, jaula, patio, tipo_pelo):
        super().__init__(cantidad, periodo_gestacion, nombre_cientifico, nombre_comun, region_procedencia, jaula, patio)
        self.tipo_pelo = tipo_pelo
    def mostrar(self):
        print(f"Nombre:{self.nombre_comun}.")
        print(f"Nombre Cientifico: {self.nombre_cientifico}.")
        print(f"Tipo de Pelaje: {self.tipo_pelo}.")
        print(f"Jaula: '{self.jaula.jaula}' - Patio: {self.jaula.patio}.")
        print(f"Procedencia: {self.region_procedencia}.")
        print(f"Gestacion: {self.periodo_gestacion} meses.")
        