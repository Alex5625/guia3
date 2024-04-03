class Paciente():

    def __init__(self):
        self.__nombre = None
        self.__edad = 0
        self.__sintomas = []

    def __repr__(self):
         return f"{self.get_tu_nombre()}"

    def set_tu_nombre(self,nombre):
            
        if isinstance(nombre,str):
            self.__nombre = nombre
        else:
                #incluir raise
                pass

    def get_tu_nombre(self):
            
            return self.__nombre
    

    def set_edad(self,edad):
        if isinstance(edad,int):
            self.__edad = edad
        else:
            #añadir raise
            pass

    def get_edad(self):

        return self.__edad

    def add_sintomas(self, sintoma):
            
        if isinstance(sintoma,str):
            self.__sintomas.append(sintoma)

        else:
            #incluir raise
                pass
        
    def show_sintomas(self):
         print(self.__sintomas)
