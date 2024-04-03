
class VirusEstacional():
    def __init__(self):
        self.__nombre = None
        self.__tipo = None
        self.__sintomas = []

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            # FIXME: incluir raise
            pass

    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        if isinstance(tipo, str):
            self.__tipo = tipo
        else:
            # FIXME: incluir raise
            pass

    def add_sintomas(self, sintoma):
        if isinstance(sintoma, str):
            self.__sintomas.append(sintoma)
        else:
            # FIXME: incluir raise
            pass

    def show_sintomas(self):
        print(self.__sintomas)
  
