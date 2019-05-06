def suma(limitTo):
    sumatorio = 0
    for i in range(limitTo+1):
        sumatorio += i        
    return sumatorio

def sumaCuadrado(limitTo):
    sumatorio = 0
    for i in range(limitTo+1):
        sumatorio += i*i
    return sumatorio

def sumaDef(limitTo, D):
    sumatorio = 0
    for i in range(limitTo+1):
        sumatorio += D(i)
    return sumatorio

def cuadrado(x):
    return X*X

def cuadradoErroneo(x, y):
    return x*x

#Este print dará un error porque sumaDef no considera un segundo parámetros (cosa que sí solicita cuadradoErroneo
print(sumaDef(4, cuadradoErroneo))