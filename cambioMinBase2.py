def verificar3Dig(n):
    aux=n*10000-int(n*10000)
    if aux==0 and n<1:
        return True
    return False

def cambioBase2(n):
    if verificar3Dig(n):
        lista=[n]
        aux=False
        aux1=0
        d=0
        k=1
        r=n
        while k<=10 and r!=0 and aux==False:
            if 2*r>=1:
                d+=10**-k
                d=round(d,k)
                r=round(2*r-1,10)
            else:
                r=2*r
            if r in lista:
                aux=True
                aux1=lista.index(r)+1
            else:
                lista.append(r)
            k+=1
        print("Su representación en base 2 es: ",d)
        if aux:
            print("Se encontró un periodo desde el decimal ",aux1,)
        else:
            print("No se encontró un periodo")
    else:
        print("El número no es menor que uno o no tiene solo 3 dígitos decimales")


n=float(input("Ingrese el número a convertir: "))
cambioBase2(n)

