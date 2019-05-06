class Perro():
    #Este def es llamado constructor, es el cual
    #permite iniciar las instancias
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("guau, guau")
        
    def __str__(self):
        return "Perro {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)

class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self,nombre,edad,peso)
        self.amo = amo
        self.__trabajando = False
    
    #Al escribir la línea de abajo se sobreescribe el
    #método de Perro (que es considerado padre).
    #Si la línea de abajo no estuviese declarada y se la
    #ejecutase, entonces busca lo que se pide en el
    #padre (si ahí no está, lo busca en el abuelo... y así)
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo)
    
    def pasear(self):
        print("{}! Ayudo a mi dueño, {} a pasear". format(self.nombre, self.amo))
        
    def ladrar(self):
        if self.__trabajando:
            print("shhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
            
class Timido():
    def __init__(self, nombre):
        self.__nombre = nombre
    
    def preguntarNombreConCuidado(self):
        return self.__nombre
        