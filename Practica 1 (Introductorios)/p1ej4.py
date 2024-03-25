cadena= [1,2,3,4,5,6,7,8,9,10]
for num in cadena:
    if (num % 2 == 0):
        print (num)
    else:
        print ("El numero ", num," no es par")

#otroa forma de hacerlo con continue

for num in cadena:
    if(num % 2 == 0 ):
        print (num)
    continue
