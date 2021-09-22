#Rotate array
def rotate(ar, d, n):
    lista=[]
    segundalista=[]
    cont=0
    for i in ar:
        cont+=1
        if cont>d:
            lista.append(i)
        else:
            segundalista.append(i)
    lista.extend(segundalista)
    print(lista)


arr=[1,2,3,4,5,6,7]
rotate(arr,3,len(arr))