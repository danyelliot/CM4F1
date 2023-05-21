import math

#FUNCION
def binario(x):
    temp = x
    A= []
    B=[]
    modulo = 0
    cociente = 0
    while x != 0: # mientras el número de entrada sea diferente de cero
        # paso 1: dividimos entre 2
        modulo = x % 2
        cociente = x // 2
        A.append(modulo) # guardamos el módulo calculado
        x = cociente # el cociente pasa a ser el número de entrada
    while temp!= 0:
        # se almacena el módulo en el orden correcto
        B.insert(0, temp % 2)
        temp //= 2
    return B
#DATOS AQUI INGRESA LOS DATOS EL VALOR
parte_entera=0
parte_decimal=0.125
#VARIABLES
signo = 0
modulos_decimal=[]

if(parte_entera == 0):
    exponente = 0
    modulos =[0]
elif(parte_entera < 0):
    print("Numero negativo: s = 1")
    signo = 1
    parte_entera = abs(parte_entera)
    modulos = binario(parte_entera)
    exponente = len(modulos)-1

#Pasar la parte decimal a binario
k = 1 
r = parte_decimal
while True:
    if (2*r >= 1):
        d = 1
        modulos_decimal.append(d)
    else:
        d=0
        modulos_decimal.append(d)
    r = 2*r-d
    if(r == 0):
        break
    k = k + 1
print("El numero en binario es: ")
for i in modulos:
    print(i,end="")
    
print(".",end="")

for i in modulos_decimal:
    print(i,end="")
#Calclando exponente sesgado
print("\nAhora calculamos el exponente sesgado: ",end="")
print(exponente," + 127 = ",end="" )
temp = exponente + 127
E = binario(temp)
for h in E:
    print(h,end="")
print("\nLa representacion pedida es")
print("Signo\texponente\tmantisa")
print(signo,end="")
print("\t",end="")
for i in E:
    print(i,end="")
    
print("\t",end="")
for i in modulos:
    print(i,end="")

for i in modulos_decimal:
    print(i,end="")
