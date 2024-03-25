numeros=[]
num=float(input("Ingrese un numero"))
while(num != -1):
    numeros.append(num)
    num=float(input("Ingrese un numero"))
    
for num in numeros:
    if(num>0):
        print("El numero es: ",num)
    else:
        break
