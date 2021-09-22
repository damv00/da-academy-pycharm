import numpy as np
import random

#Ejercicio 1
print("\tEjercicio 1")
print(pow(16,1/2))
print(f"{pow(16,0.5)}\n")

#Ejercicio 2
print("\tEjercicio 2")
x=[1,2,3,4,5]
y=[11,12,13,14,15]
z=(21,22,23,24,25)
#a)3*x
print(3*x)
#b)x+y
print(x+y)
#c)x-y
#print(x-y)
#error
#d)x[1]
print(x[1])
#e)x[0]
print(x[0])
#f)x[-1]
print(x[-1])
#g)x[:]
print(x[:])
#h)x[2:4]
print(x[2:4])
#i)x[1:4:2]
print(x[1:4:2])
#j)x[:2]
print(x[:2])
#k)x[::2]
print(x[::2])
#l)x[3]=8
#print(x)
x[3]=8
print(x)
#m)
print(z[::2])
#z[3]=8 tuples are immutable
print(f"{z}\n")

#Ejercicio 3
print("\tEjercicio 3")
s="abcde"
#a)3*s
print(3*s)
#b) s[1]
print(s[1])
#c)s[-1]
print(s[-1])
#d)s[::2]
print(f"{s[::2]}\n")

#Ejercicio 4
print("\tEjercicio 4")
#List of numbers that are the Sum of factors
suma=0
lista=[]
for i in range(1,101):
    suma += i
    if suma<=100:
        lista.append(suma)
print(f"The list of numbers that are the sum of their factors are: \n{lista}\n")

#Ejercicio 5
print("\tEjercicio 5")
#a)x+y
x=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,5]
y=[2,7,1,8,2,8,1,8,2,8,4,5,9,0,4,5,5,3,4,9]
for i in range(len(x)):
    x[i]=str(x[i])
    y[i]=str(y[i])
x="".join(x)
y="".join(y)
z=int(x)+int(y)
add_number=[]
for i in str(z):
    add_number.append(i)
print(f"The operation x+y is: \n{add_number}\n")

#b)15*x
multiplication_number=int(y)*15
nuevalista=[]
for i in str(multiplication_number):
    nuevalista.append(i)
print(f"The operation 15*x is: \n{nuevalista}\n")

#Ejercicio 6
print("\tEjercicio 6")
'''
a)Define  a  function  nameddif2 that  accepts  an  integer  N  as  inputparameter  
and  constructs  and  returns  an N×N two-dimensional numpyarray A,  with  the  value  -2.0  on  
the  main  diagonal  and  the value +1.0 on the super-diagonal and the sub-diagonal.
'''
size=int(input("Enter the size of the array: "))
def nameddif2(n):
    A = np.matrix(np.zeros((n, n)))
    for fila in range(n):
        for columna in range(n):
            if fila==columna:
                A[fila,columna]=-2
            elif fila+1==columna or fila==columna+1:
                A[fila, columna] = 1
    return(A)

A=nameddif2(size)
A=A[:].astype(int)
print(f"The matrix A is: \n{A}\n")
'''
b)
For  N=10,  construct  a  one-dimensional  array b of  length N filled with zeros 
except that the first element is 1.0 and the last element is-N. 
For N=10, solve the system Ax=b for x.
'''
B=np.array(np.zeros(size))
B[0]=1
B[size-1]=-size
B=np.matrix(B)
B=B[:].astype(int)
print(f"The matriz B is:\n{B}\n")

#x=B/A
inversoA=np.linalg.inv(A)
x=B*inversoA
x=np.round(x).astype(int)
print(f"Taking the system Ax=b the matrix x is equal to:\n{x}\n")

'''
c)
For  N=20,  construct  a  one-dimensional  array "c" of  length N,  filled with  random  numbers.   
For  A  from  the dif2function,  Solve  the system Ay=c for y and then confirm that the solution 
you found is approximately correct by computing the relative norm of the residual error, 
‖Ay−c‖/‖c‖.  
This value should be no larger than 10−12.
'''
lista_random=[]
for i in range(size):
    lista_random.append(random.randint(0,10))
c=np.matrix(lista_random)
print(f"The matrix C is:\n{c}\n")
#Inverso de c
inversoC=np.empty((size,1),dtype=int)
for i in range(size):
    inversoC[i][0] = lista_random[i]

#y=c*InversoA
y=c*inversoA
print(f"Taking the system Ay=c the matrix y is equal to:\n{y}\n")

#Comprobacion
comprobacion=abs((y*A)-c)
comprobacion=comprobacion*abs(inversoC)
if comprobacion>(10**-12):
    print(f"The value {comprobacion} is correct")
else:
    print(f"The value {comprobacion} is not correct")
