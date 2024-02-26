from modulos.mamifero import Mamifero
from modulos.reptil import Reptil
from modulos.ave import Ave
from modulos.peces import Pez
from  modulos.animal import Jaula
#lista de Animales
zoologico = []
#funcion para mostrar propiedades
def mostrar_propiedades(obj):
    for key, valor in obj.__dict__.items():
        if isinstance(valor, (dict, Jaula)):
            print(f"{key}:")
            mostrar_propiedades(valor)
        else:
            print(f"{key}: {valor}")
#funcion validacion
def validar(texto):
    while True:
     valor_validar = input(texto)
     if not valor_validar.strip():
         print("El campo no puede estar vacío. Por favor, ingrese un valor.")
     else: return valor_validar      
#funcion para Buscar
def buscar(lista_animales, nombre):

    for animal in lista_animales:
        if animal.nombre_comun == nombre:
            return animal
    return None
#funcion para Crear
def crear():
    #Selecionando Tipo de Animal
    band = False
    while band is False:
        print("Selecione tipo de Animal: ")
        print("1.Mamifero")
        print("2.Reptil")
        print("3.Ave")
        print("4.Pez")
        opcion = int(input("Ingrese un Numero en el rango permitido: "))
        if opcion < 1 or opcion > 4 :
            band = False
            print("Inserte un valor correcto")
        else:
            band = True
  #Introduciendo Aspectos
        nombre_comun          = validar("Nombre Comun: ")
        nombre_cientifico     = validar("Nombre Cientifico: ")
        periodo_gestacion     = validar("Periodo de Gestacion (Meses): ")
        cantidad_animales     = validar("Cantidad de ese Animal: ")
        region_procedencia    = validar("Region de Procedencia: ")
        jaula                 = validar("Jaula: ")
        patio                 = validar("Patio: ")

    if opcion == 1:
        tipo_pelo = validar("Tipo de Pelo: ")
        new_mamifero = Mamifero(cantidad_animales,periodo_gestacion,nombre_cientifico,nombre_comun,region_procedencia,jaula,patio,tipo_pelo)
        zoologico.append(new_mamifero)
    elif opcion == 2:
        venenoso = None
        while (venenoso is None):
            veneno = input("Venenoso(S/N): ")
            if veneno in ('s','S'):
                venenoso = True
            elif veneno in('n','N'):
                venenoso = False
            else:
                venenoso = None
                print("Inserte valores (S/N)")
            new_reptil = Reptil(cantidad_animales,periodo_gestacion,nombre_cientifico,nombre_comun,region_procedencia,jaula,patio,venenoso)
            zoologico.append(new_reptil)
    elif opcion == 3:
        color_plumas = validar("Color de Plumas: ")
        new_ave = Ave(cantidad_animales,periodo_gestacion,nombre_cientifico,nombre_comun,region_procedencia,jaula,patio,color_plumas)
        zoologico.append(new_ave)
    else:
        cantidad_aletas = validar(int(input("Cantidad de Aletas: ")))
        new_pez = Pez(cantidad_animales,periodo_gestacion,nombre_cientifico,nombre_comun,region_procedencia,jaula,patio,cantidad_aletas)       
        zoologico.append(new_pez)
#funcion para Editar
def editar(animal,propiedad,nuevo_valor):
    if  hasattr(animal,propiedad):
        setattr(animal,propiedad,nuevo_valor)
        print(f"La propiedad '{propiedad}' ha sido actualizada correctamente. Nuevo Valor - ({nuevo_valor})")
    else:
        print(f"El objeto no tiene la propiedad '{propiedad}'.")   
#funcion para Eliminar
def eliminar_animal(lista_animales, animal_borrar):
    for animal in lista_animales:
      if animal.nombre_comun == animal_borrar:    
       lista_animales.remove(animal)
       print(f"Se ha eliminado '{animal_borrar}' de la lista de animales.")
       break
    else: print(f"'{animal_borrar}' no se encontraba en la lista de animales.")
#funcion para mostrar lista
def mostrarLista(lista):
    for animal in lista:
        print("////////////////////////////////////////////////////////////////////////")
        animal.mostrar()
#funcion q creo un menu para Mostrar en Consola
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Crear Animal")
    print("2. Editar Animal")
    print("3. Buscar Animal")
    print("4. Eliminar Animal")
    print("5. Mostrar Zoologico")
    print("6. Salir")

#Procesamiento del Zoologico
print("Administracion del Zoologico")
band1 = False
while band1 is False:
 mostrar_menu()
 opcion = int(input("Seleccione una opción: "))
 if opcion == 1:
     crear()   
     print("Animal creado exitosamente.")
 elif opcion == 2:
     nombre_buscar = validar("Ingrese el nombre del Animal que desea editar: ")
     if buscar(zoologico,nombre_buscar) is not None:
         animal = (buscar(zoologico,nombre_buscar))
         print("Propiedades disponibles:")
         mostrar_propiedades(animal)
         propiedad_editar = input("Seleccione una propiedad de las mostradas: ")
         new_valor = validar("Ingrese nuevo valor para dicha propiedad: ")
         editar(animal,propiedad_editar,new_valor)
     else:
         print(f"No se encontró ningún animal con el nombre '{nombre_buscar}'.")
 elif opcion == 3:
        nombre_buscar = validar("Ingrese el nombre del Animal que desea buscar: ")
        animal_encontrado = buscar(zoologico,nombre_buscar)
        if animal_encontrado:
            print(f"Animal encontrado: {animal_encontrado.nombre_comun} - Cantidad: {animal_encontrado.cantidad} - Jaula: {animal_encontrado.jaula.jaula}: Patio: {animal_encontrado.jaula.patio}")
        else:
            print(f"No se encontró ningún animal con el nombre '{nombre_buscar}'.")
 elif opcion == 4:
        nombre_eliminar = validar("Ingrese el nombre del animal que desea eliminar: ")
        eliminar_animal(zoologico,nombre_eliminar)
 elif opcion == 5:
        mostrarLista(zoologico)       
 elif opcion == 6:
        band1 = True
        print("¡Hasta luego!")
        break
else:
    print("Opción no válida. Por favor, seleccione una opción válida.")
    band1 = False



