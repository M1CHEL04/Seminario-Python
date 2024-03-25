cadena= [1,2,3,4,5,6,7,8,9,10]
pares=[]
impares=[]
for num in cadena:
    if(num % 2 == 0):
        pares.append(num)
    else:
        impares.append(num)

#imprimo la cadena de pares
print("Pares: ")
for num in pares:
    print(num)

#imprimo impares
print("Impares: ")
for num in impares:
    print(num)