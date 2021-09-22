#Ejercicio 1
'''
Python provides a built in function len that returns the length of a string, so the value of len('allen') is 5.
Write a function named right_justify that takes a string named s as a parameter and prints the
string with enough leading spaces so that the last letter of the string is in column 70 of the display
'''
print("\tEjercicio 1")
def right_justify(s):
    length=len(s)
    spaces=round(70/length)
    for index in range(length):
        print(s[index])
        if index+1!=len(s):
            for j in range(spaces):
                print("")
right_justify("DavidMurguia")

#Ejercicio 2
print("\n\tEjercicio 2")
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
any_lowercase1("David")
#Solo evalua la primera letra del string "s" y regresa True si es lowercase o False si no es lowercase

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
any_lowercase2("David")
#Solo evalua la letra "c", en este caso siempre regesara True

def any_lowercase3(s):
    for c in s:
        flag=c.islower()
    return flag
any_lowercase3("David")
#Guardara en una variable "flag" True or false dependiendo si la letra en s es lowercase o no,
#pero se va sobrescribiendo tomando siempre el resultado de la ultima letra de s

def any_lowercase4(s):
    flag=False
    for c in s:
        flag=flag or c.islower()
    return flag
any_lowercase4("David")
#Debido a que es un "or" siempre tomara un False en caso de que flag o c.islower() cualquiera sea Falso
#flag=False
#c.islower()=True
#flag=False
#Nunca tomara el valor de True

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
any_lowercase5("David")
#Si c es lowercase no hace nada, si alguna de ellas no es lower entonces se acaba el programa regresando False

#Ejercicio 3
print("\n\tEjercicio 3")
def has_no_e(s):
    suma_sin_e=0
    suma_con_e=0
    if "e" in s:
        for i in s:
            if i!="e":
                print(i)
                suma_sin_e+=1
            else:
                suma_con_e+=1
        porcentaje_sin_e=suma_sin_e/(suma_sin_e+suma_con_e)
        print(f"El porcentaje de letras sin e es de: {porcentaje_sin_e*100}%")
        return False
    else:
        for i in s:
            print(i)
            suma_sin_e+=1
        porcentaje_sin_e = suma_sin_e / (suma_sin_e + suma_con_e)
        print("El porcentaje de letras sin e es de: {:.2f}%".format(porcentaje_sin_e*100))
        return True
has_no_e("Deivid")
#print only words that dont have e
#percentage of words that have no e

#Ejericio 4
print("\n\tEjercicio 4")
def avoids(word,forbidden):
    word=word.replace(" ","").casefold()
    contador_sin_forbidden=0
    contador_con_forbidden=0
    for letra in word:
        if letra not in forbidden:
            contador_sin_forbidden+=1
        else:
            contador_con_forbidden+=1
    if contador_con_forbidden>=1:
        print(f"El numero de letras sin forbidden letters es: {contador_sin_forbidden}")
        return False
    else:
        print(f"El numero de letras sin forbidden letters es: {contador_sin_forbidden}")
        return True

prohibidas=input("Ingrese forbidden letters: ")
prohibidas=prohibidas.replace(" ","").casefold()
result=avoids("Tendra este texto forbidden letters?",prohibidas)
print(result)
#Impirmir el numero de palabras que no contienen ninguna forbidden letter
#Combinacion de 5 forbidden letters excluyendo el menor numero de palabras

["gato","perro","gallina","perico","oso"]

#Ejercicio 5
print("\n\tEjercicio 5")
def uses_only(word,string):
    word=word.replace(" ","").casefold()
    contador_incorrectas=0
    for i in word:
        if i not in string:
            contador_incorrectas+=1
    if contador_incorrectas>0:
        return False
    else:
        return True

#regresa True si word contiene solo letras de string
respuesta=uses_only("Hoe alfalfa","acefhlo")
print(respuesta)

#Ejercicio 6
print("\n\tEjercicio 6")
def uses_all(word,string):
    word=word.replace(" ","").casefold()
    letras_usadas_string=""
    for i in word:
        for j in string:
            if i==j:
                letras_usadas_string+=j
    letras_usadas_string=list(set(letras_usadas_string))
    letras_usadas_string.sort()
    string=list(string)
    string.sort()
    if "".join(string)=="".join(letras_usadas_string):
        return True
    else:
        return False

#Regresa True si word usa todas las letras de string al menos una vez
#Cuantas words hay que usen las vocales aeiou
#cuantas words hay que usen aeiouy
listadepalabras=["hoe alfalfa","hola amiGos","murcielago","murcielago y ratones"]
for i in listadepalabras:
    respuesta=uses_all(i,"aeiou")
    print(f"La palabra {i} regresa la respuesta: {respuesta}")

print("\n")
for i in listadepalabras:
    respuesta=uses_all(i,"aeiouy")
    print(f"La palabra {i} regresa la respuesta: {respuesta}")

assert uses_all("murcielago","aeiou")==True
assert uses_all("oso","aeiou")==False



Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
