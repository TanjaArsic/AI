# proizvod, koja računa proizvod liste podlisti (A) i liste brojeva (B). Smatrati da je broj podlisti u
# listi A jednak dužini liste B. Funkcija vraća listu koja ima onoliko elemenata koliko je dužina
# ulaznih listi. N-ti element izlayne liste predstavlja sumu svih elemenata N-te podliste liste A koji u
# prethodno pomnoženi N-tim elementom u liste B. Zabranjeno je korišćenje petlji i funkcije sum
from functools import reduce


def proizvod(A,B):
    return list(map(lambda x: x[0]*x[1], list(zip (list(map(lambda x: reduce(lambda a,b: a+b, x), A)) ,B))))
print(proizvod([[1,2,3],[4,5,6],[7,8,9]], [1,2,3])) #=6,30,72