from funciones1Nivel import sumaTodos

#Se puede usar el lambda de doble y triple dentro del doble y triple del print, no hay ningún problema.

doble = lambda x: x*2

triple = lambda x: x*3

print(sumaTodos(3, doble))
print(sumaTodos(100, triple))

