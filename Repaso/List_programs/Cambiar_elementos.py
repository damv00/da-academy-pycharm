
# Python program to swap two elements in a list
lista1 = ["Chef", "Actuario", "Comediante", "Programador"]
print(lista1)
# cambiar la posicion de chef a comediante
primer_elemento = lista1[0]
tercer_elemento = lista1[2]
del lista1[0]
del lista1[1]
lista1.insert(0, tercer_elemento)
lista1.insert(2, primer_elemento)
print(lista1)

# 1
s = 'azcbobobegghakl'
contador = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        contador += 1
# 2
print("Number of vowels: " + str(contador))

s = 'azcbobobeggbobhaklbobbob'
contador = 0
for i in range(len(s)):
    if (i + 2 == len(s)):
        break
    if s[i] + s[i + 1] + s[i + 2] == 'bob':
        contador += 1

print(f"Number of times bob occurs is: {contador}")

# 3
s = 'abcdefcds'
contador=0
inicio=0
while contador<len(s):
    for i in range(inicio,len(s)):
        if(s[i]<s[i+1]):
            contador+=1
        else:
            break
    print(s[inicio:contador])
    inicio = contador

name="Edson"
lista=[]
for i in name:
    lista.append(i)

lista.reverse()
lista="".join(lista)
print(lista)