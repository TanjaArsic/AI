# 19 Korišdenjem programskog jezika Python, napisati funkciju stepenuj, koja listu tuple
# vrednosti transformiše u listu brojeva, koji se dobijaju primenom operacije stepenovanja,
# tako što se prvi element stepenuje drugim, zatim se rezultat stepenuje tredim sve dok se
# ne dođe do poslednjeg elementa u tuple-u.
# Primer: stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )]) = [1, 32, 256, 5]

def zbir(lista): 
    novalista=list()
    i=1
    j=0
    while i<len(lista):
        rez=lista[j]
        rez+=lista[i]
        i+=1
        j+=1
        novalista.append(rez)
    return novalista

print(zbir([1, 2, 3, 4, 5]))# = [3, 5, 7, 9]



#2 fja numlista, koja iz liste koja može da sadrži elemente različitog tipa izdvaja samo numeričke vrednost
# def numlista(lista):
    # recnik:{
    #     'int':
    #     'str'
    # }
    # for x in lista:
    #     if isinstance(x,int):
    #         recnik.key()=='int'.append(x)
    # return recnik

# print(numlista(["Prvi", "Drugi", 2, 4, [3, 5]])) #izb [2,4]

# Primer: numlista(["Prvi", "Drugi", 2, 4, [3, 5]]) =
# {'str': ["Prvi", "Drugi"], 'int': [2, 4], 'list': [[3, 5]]}

def parni(lista):
    counter=0
    for x in lista:
        if not x%2:
            counter+=1
    return counter
print(parni([1, 7, 2, 4, 5, 2]))

def numlista(lista):
        pom=list()
        [pom.append(x) if isinstance(x,int) else not x for x in lista[:]] 
        return pom
print(numlista(["Prvi", "Drugi", 2, 4, [3, 5]])) #izb 2,4


