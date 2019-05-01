#Esta es una función recursiva, se define porque ella se llama a sí misma
#El código de lo recursivo es elegante, pero muy poco eficiente.
#La recursividad puede generar bucles infinitos. Por lo cual es importante saber cuándo se detiene
def retrocontador(e):
    print("{}, ".format(e), end="")
    
    if e > 1:
        retrocontador(e-1)
        
    else:
        print("0")
    return
    
retrocontador(10)


def sumatorio(n):
    
    if n != 0:
        return n + sumatorio(n-1)
    
sumatorio(4)