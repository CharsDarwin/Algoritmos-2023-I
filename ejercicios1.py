#identifique de los primeros 20 numeros , cuales son par e impar (usar for o while) y alamacenar areglo par e impar
numerosPares=[]
numerosImPares=[]
for i in range(20):
    if(i%2==0):
        numerosPares.append(i)
    else:
       numerosImPares.append(i) 
    
print(numerosPares,"  es par")
print(numerosImPares," es impar")

#otro metodo
n=0
par=[]
impar=[]
while n<21:
    if(n%2)==0:
        par.append(n)
    else:
        impar.append(n)
        
    n+=1

print("\n\nnumeros pares : ", par)
print("numeros impares: ",impar)