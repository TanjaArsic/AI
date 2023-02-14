#3 uredi, koja svaki od prvih n elemenata uvećava za definisanu vrednost a preostale umanjuje za 
# definisanu vrednost. Funkciji se prosleđuje lista koja sadrži samo numeričke vrednosti i vrednost 
# koja treba da se uvećava, odnosno umanjuje. Zabranjeno je korišćenje petlji.
# Primer: uredi([1, 2, 3, 4, 5], 3, 1) = [2, 3, 4, 3, 4]. ne znam kako bez petlji
def uredi(lista, n, broj):
    for i in range (0, len(lista)):
        if i<n:
            lista[i]+=broj
        else: 
            lista[i]-=broj
    return lista
    
print(uredi([1, 2, 3, 4, 5], 3, 1))


#5 fja brojel, koja broji koliko elemenata ima svaka 
# podlista liste koja joj je prosleđena. Ukoliko 
#elemenat liste nije podlista funkcija vraća -1
def brojel(*lista) -> list[int]:
     return [len(x) if isinstance(x,list) else -1 for x in list(lista)]

print(brojel([1, 2], [3, 4, 5], 'el', ['1', 1])) #= [2, 3, -1, 2] VRACA MI SAMU LISTU



#6 fja razlika, koja prihvata dve liste (bilo kog tipa podataka), a ima povratnu vrednost koja je lista 
#sastavljena od svih elemenata iz prve liste, koji se ne nalaze u drugoj listi.
def razlika(lista1, lista2):
    nova = []
    for x in lista1:
        if x not in lista2:
            nova.append(x)
    return nova
print(razlika([1, 4, 6, "2", "6"], [4, 5, "2"])) # = [1, 6, "6"]



#8 fja izmeni, koja svaki n-ti element liste zamenjuje brojem koji predstavlja sumu svih elemenata 
#originalne liste, od prvog, do n-tog elementa.
def izmeni(lista):
    sum=0
    for i in range(0, len(lista)):
        sum+=lista[i]
        lista[i]=sum
    return lista
print(izmeni([1, 2, 4, 7, 9])) #= [1, 3, 7, 14, 23]


#9 fja prosek, koja za svaki element prosleđene liste, koja se sastoji isključivo od podlisti, vraća 
#aritmetičku sredinu svih njenih vrednosti
def prosek(lista):
    novalista=[]
    for malalista in lista:
        sum=0
        for element in malalista: #range(0,len(x)):
            sum = sum + element
        malalista=sum/len(malalista) #novalista.append(sum/len(malalista))
        novalista.append(malalista)
    return novalista #eto reseno kad sam glupa ko kurac 
print(prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))# = [3.25, 4.75, 4.0, 5.0]



#10 izbrojBrEl, koja određuje broj elemenata liste, gde svaki element može da bude podlista ili broj.
#Zabranjeno je korišćenje petlji (osim u comprehension sintaksi).
def izbrojBrEl(lista):
    br=0
    for elem in lista:
        if type(elem) == list:  
            br += izbrojBrEl(elem)
        else:
            br += 1    
    return br      

print(izbrojBrEl([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]))# = 13

#11 fja razlika, koja kreira novu listu čiji su elementi razlika susednih elementa liste.
def razlika2(lista):
    novalista=list()
    for x,y in zip(lista[1:], lista):
        novalista.append(y - x)
    return novalista
    #ILI return [y - x for x,y in zip(lista[1:],lista)]

print(razlika2([8, 5, 3, 1, 1])) #= [3, 2, 2, 0]


#12 presek, koja prihvata dve liste (bilo kog tipa podataka), a ima povratnu vrednost koja je lista 
#sastavljena od svih elemenata koji se nalaze u obe liste.
#Primer: razlika([5, 4, "1", "8", 3, 7], [1, 9, "1"]) = [1, "1"]

def presek(lista1,lista2):
    vrati=list()
    for x in lista1:
        if x in lista2:
            vrati.append(x);
    return vrati
print(presek([5, 4, 1, "1", "8", 3, 7], [1, 9, "1"]))# = [1, "1"]


#13 fjaizmeni, koja kreira novu listu tako da elemente na parnim pozicijama uvećava za jedan, dok 
# elemente na neparnim pozicijama umanjuje za 1.

def izmeni2(lista):
    return [lista[x] -1 if x%2 else lista[x]+1 for x in range(0,len(lista))]
print(izmeni2([8, 5, 3, 1, 1])) #= [9, 4, 4, 0, 2]



#14 fja. unija, koja prihvata dve liste (bilo kog tipa podataka), a ima povratnu vrednost koja je lista 
#sastavljena od svih elemenata obe liste bez ponavljanja.
def unija(lista1,lista2):
    novaja=list()
    for x in lista1: #unija je apendovano sve manje presek
        novaja.append(x)
    for x in lista2:
        if x not in lista1:
            novaja.append(x)
    return novaja
print(unija([5, 4, "1", "8", 3, 7], [1, 9, "1"]))# = [5, 4, "1", "8", 3, 7, 9, 1


#15 izdvojii, koja iz zadate liste čiji su elementi liste, izdvaja n-ti element i formira rezultujuću listu, pri 
#čemu je n=0 za prvu podlistu i uvećava se sukcesivno za 1. Ukoliko ne postoji n-ti element u listi 
#vraća se 0.

def izdvojii(*lista):
    novalista=list()
    i=0
    for malalista in lista:
        if i < len(malalista):
            novalista.append(malalista[i])
        else:
            novalista.append(0)
        i+=1
    return novalista
#moze i kao novalista[i][i] vrv
print(izdvojii([5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]))# = [5, 9, 0, 12]

 



# 19 Korišdenjem programskog jezika Python, napisati funkciju stepenuj, koja listu tuple
# vrednosti transformiše u listu brojeva, koji se dobijaju primenom operacije stepenovanja,
# tako što se prvi element stepenuje drugim, zatim se rezultat stepenuje tredim sve dok se
# ne dođe do poslednjeg elementa u tuple-u.
# Primer: stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )]) = [1, 32, 256, 5]

def stepenuj(tapl:tuple): 
    lista=list()
    for x in tapl:
        rez=x[0]
        i=1
        while i<len(x):
            rez**=x[i] #rez = rez**x[i]
            i+=1
        lista.append(rez)
    return lista

print(stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )])) #= [1, 32, 256, 5]



