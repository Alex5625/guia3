import json
import random
from virus import VirusEstacional
from paciente import Paciente

#mauyscula son para nombrar constantes
FILENAME = "./archivos/virus_sintomas.json"


def open_file_txt(filename):
    with open(filename) as texto:
        for linea in texto:
            print(linea.rstrip())



# BUSCAR EL VALOR (CLAVE) DENTRO DE LA BIBLIOTECA PARA IR BUSCANDO EL DATO PRECISO
# NAVEGANDO A TRAVES DEL ARCHIVO PARA ENCONTRAR LO QUE NECESITEMOS
 
def open_file_json(filename):
    """ Procesa un archivo de texto json y
    retorna un diccionario"""
    with open(filename) as texto:
        new_dict = json.load(texto)
    return new_dict

def procesa_virus_sintomas(datos):
    # Obtengo una lista de elementos
    virus_estacional = []
    virus_sintomas = datos.get("virus_sintomas")
    for item in virus_sintomas:
        # Obtengo datos desde archivo json
        nombre = item.get("virus")
        sintomas = item.get("sintomas")
        # creo el objeto
        temp = VirusEstacional()
        temp.set_nombre(nombre)
        temp.set_tipo(nombre)
        for sintoma in sintomas:
            temp.add_sintomas(sintoma)

        # Agrego objeto a conjunto de datos
        virus_estacional.append(temp)

    # veo que el objeto construido
    print(virus_estacional[0].get_nombre())
    print(virus_estacional[0].get_tipo())
    virus_estacional[0].show_sintomas()
    print(len(virus_estacional))

def crea_pacientes():
    nombres = ["alexis","pepito","pete","cristo", "nico", "dani","ignacio","sofi"]
    apellido =["letelier","montero","hernan","morales","duran","perez"]
    pacientes = []
    for i in range(5):
        num_aleatorio_nombre = random.randint(0,len(nombres)) - 1
        num_aleatorio_apellido = random.randint(0,len(apellido)) - 1

        nombre_apellido = f"{nombres[num_aleatorio_nombre]} {apellido[num_aleatorio_apellido]}"
        print(nombre_apellido)

        obj = Paciente()
        obj.set_tu_nombre(nombre_apellido)
        obj.set_edad(random.randint(0,100))
        pacientes.append(obj)

    return pacientes

def crea_lista_sintomas():
    datos = open_file_json(FILENAME)
    # print(datos)
    datos = datos.get("virus_sintomas")
    lista_sintomas = []


    for item in datos:
        # print(item.get("sintomas"))
        for sintoma in item.get("sintomas"):

            #PARA CREAR LA LISTA DE SINTOMAS NO REPETIDA
            if not lista_sintomas:
                lista_sintomas.append(sintoma)
            else:
                if sintoma not in lista_sintomas:
                    lista_sintomas.append(sintoma)
        pass
    print(lista_sintomas)
    return lista_sintomas



# def asoocia_sintomas_pacientes(pacientes=None, sintomas=None):
    
#     for paciente in pacientes: 
#         largo = list(range(len(sintomas)))
#         muestra = random.sample(largo,random.randint(3,7))
#         print(muestra)

#         for i in muestra:
#             temp = sintomas[i]
#             paciente.add_sintomas(temp)

#         print(paciente.get_nombre())
#         print(paciente.get_sintomas())


# TAREA PA LA CASA HACER EL MATCH DE COMPARAR LOS SINTOMAS DEL PACIENTE CON LOS DE LA ENFERMEDAD





def asoocia_sintomas_pacientes(pacientes=None, sintomas=None):
    for paciente in pacientes:
        sintomas_agregados = set()  # Conjunto para almacenar los síntomas agregados a este paciente
        for i in range(0, random.randint(3, 7)):
            temp = sintomas[random.randint(0, len(sintomas) - 1)]

            while temp in sintomas_agregados:  # Verificar si el síntoma ya ha sido agregado
                temp = sintomas[random.randint(0, len(sintomas) - 1)]

            paciente.add_sintomas(temp)
            sintomas_agregados.add(temp)  # Agregar el síntoma al conjunto

        print(paciente.get_tu_nombre())
        print(paciente.show_sintomas())








# lo importante de usar json, es ir sacando datos y organizarlos, por ejemplo tener la key de la bilioteca
# y luego dentro de la alamcenar el arreglo de datos que contiene la biblioteca.

# LA FUNCION PRINCIPAL ES ESTA, DENTRO SE DEBEN LLAMAR A OTRAS FUNCIONES PARA QUE CUMPLA LO Q PIDA


if __name__ == "__main__":
    #open_file_txt()
    sintomas = open_file_json(FILENAME)
    procesa_virus_sintomas(sintomas)
    crea_pacientes()
    pacientes = crea_pacientes()
    print(pacientes)

    lista_sintomas = crea_lista_sintomas()

    asoocia_sintomas_pacientes(pacientes = pacientes, sintomas = lista_sintomas)
     