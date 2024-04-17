import random
import time


def insertionsort(list):
    for i in range(1, len(list)):
        val_i = list[i]
        prev = i - 1
        while prev >=0 and list[prev] > val_i:
            list[prev + 1]= list[prev]
            prev = prev -1
        list[prev +1 ] = val_i
    return list

def merge(list, beg_first, end_first, end_all):
    L = list[beg_first: end_first+1]
    R = list[end_first+1: end_all + 1]
    i = j = 0 # i - iterator L j - interator R
    k = beg_first # k - początek do użycia
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            list[k]= L[i] # L[i ] jest mniejsze więc wpisaujemy je pod wartośc k w lisćie
            i += 1   
        else:
            list[k]= R[j]
            j+=1
        k+=1 # przesunięcie w liscie poczatkowej 
    while i < len(L):
        list[k] = L[i]
        i+=1
        k+=1
    while j < len(R):
        list[k] = R[j]
        j+=1
        k+=1
    


    

def mergesort(list, a, b):  # a - początek listy b - koniec listy
    if a < b:
        c = (a+b)//2
        mergesort(list, a,c)  #podział az do jednostek 
        mergesort(list, c+1, b)
        merge(list,a, c, b) #  list - głowną lista przekazana do f scalania
        # a - indeks początkowy pierwszej podlsity
        # c - indeks koncowy pierwszej podlisty
        # b -  indeks koncowy driej podlisty
    return list

def losowanie(list):
    for i in range(len(list)):
        i = random.uniform(0,101)
    return list

def find_lowest(list):
    lowest = list[0]
    for i in list:
        if i > lowest:
            lowest = i
    return lowest
def find_longest(list):
    longest = list[0]
    for i in list:
        if i < longest:
            longest = i
    return longest
def srednia(list):
    suma = 0
    for i in list:
        suma += i
    return suma/len(list)

#-------------- Porównanie 
lista_testowe = []
for _ in range(100):
    sublist = [random.uniform(1, 1000) for _ in range(1000)]
    lista_testowe.append(sublist)

merges = list(lista_testowe)
insert = list(lista_testowe)

wyniki_insert =[]
beg_insert = time.time()
for i in range(0, len(lista_testowe)):
    start_podejsci = time.time()
    insert[i] = insertionsort(insert[i])
    wyniki_insert.append(time.time()-start_podejsci)
time_insert =  time.time() - beg_insert

wyniki_merge = []
beg_merge = time.time()
for i in range(0, len(lista_testowe)):
    start_podejsci = time.time()
    merges[i] = mergesort(merges[i], 0, len(merges[i]))
    wyniki_merge.append(time.time()-start_podejsci)
time_merge = time.time() - beg_merge




print("Insertsort - średni czas to ",  srednia(wyniki_insert), "sekund")
print("Insertsort - najkrótszy czas to ",  find_lowest(wyniki_insert), "sekund")
print("Insertsort - najdłuższy czas to ",  find_longest(wyniki_insert), "sekund")
print("Czas całego srotowania przez wstawianie to ", time_insert)
print("Mergetsort - średni czas to ",  srednia(wyniki_merge), "sekund")
print("Mergetsort - najkrótszy czas to ",  find_lowest(wyniki_merge), "sekund")
print("Mergesort  - najdłuższy czas to ",  find_longest(wyniki_merge), "sekund")
print("Czas całego srotowania przez łączenie to ", time_merge)
