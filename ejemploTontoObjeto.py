class Objeto():
    __atributoPrivado = None
    atributoPublico = None
    
    def __init__(self):
        self.__atributoPrivado = 0
        self.atributoPublico = "Me lo ha dicho Jorge, jijiji"
        
    def atributoPrivado (self, valor=None):
        if valor == None:
            return self.__atributoPrivado
        else:
            self.__atributoPrivado = valor