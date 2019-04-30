from functools import reduce

def SumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
        
    return resultado

def SumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor * 2
        
    return resultado


def productoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor
    return resultado

lista = [1, 3, -1, 15, 9]

sumatorio = reduce(lambda x, y: x + y, lista)

#Esto clona la lista, gracias al [:]. Si no se usase, entonces la variable "l" estaría referenciando al mismo conjunto de datos en la lista (y lo que se cambiase en "l" también se cambiaría en "lista")
l = lista[:]

#Añado el neutro para la suma en la posición cero
l.insert(0,0)
sumatorioDobles = reduce(lambda x, y: x+y*2, l)

print(sumatorio)
print(sumatorioDobles)