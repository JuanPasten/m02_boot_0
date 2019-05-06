class Termometro():
    def __init__(self):
        self.__unidadM = "C"
        self.__temperatura = 0
        
    #Esta función devuelve el estado que se tiene
    def __str__(self):
        return "{}° {}".format(self.__temperatura, self.__unidadM)
    
    #Este es el getter y setter de la unidad de medida
    def unidadMedida(self, uniM=None):
        if uniM == None:
            return self.__unidadM
        else:
            if uniM == "F" or uniM == "C":
                self.__unidadM = uniM
                
    #Este es el getter y setter de la temperatura
    def temp(self,temperatura=None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
    #Esta función convierte una unidad °F en °C. Y si se la
    #informa en °C se la convierte en °F
    def __conversor(self, temperatura, unidad):
        if unidad == "C":
            return "{} °F".format(temperatura * 9/5 + 32)
        elif unidad == "F":
            return "{}° C".format((temperatura - 32) *5/9)
        else:
            return "Unidad incorrecta"
    
    #Esta función devuelve el estado en la unidad que se la pida
    def mide(self, uniM=None):
        if uniM == None or uniM == self.__unidadM:
            return self.__str__()
        else:
            if uniM == "F" or uniM == "C":
                return self.__conversor(self.__temperatura, self.__unidadM)
            else:
                return self.__str__()
        
'''
t = Termometro()
t.temp(32)
t.unidadMedida("F")
print(t.mide())
'''