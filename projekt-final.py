import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def dane():
    n = int(input("Podaj liczbę schronisk (n): "))
    m = int(input("Podaj liczbę szlaków (m): "))

    if m < n - 1:
        raise Exception("Graf będzie niespójny. Podaj liczbę >= n-1")
    if m > n*(n-1)/2:
        raise Exception("Za duzo krawędzi w grafie.")
    
    Wmax = int(input("Podaj maksymalną wysokość szlaku do której mozna chodzic (Wmax): "))
    if Wmax <= 0:
        raise Exception("Wysokość musi być liczbą nieujemną.")
    
    W = int(input("Podaj największą wysokość jaka ma być w grafie (W): "))
    if W < Wmax:
        raise Exception("Wysokość W musi być mniejsza lub równa Wmax")
    
    return n, m, Wmax, W

def los_graf(n, m, W):   
    graf = [[0 for i in range(n)] for j in range(n)]

    # lista wierzcholkow, ktore po kolei laczy sciezka - robimy graf rozpinajacy
    lista = random.sample(range(n), n)
    for i in range(n-1):
        elem1 = lista[i]
        elem2 = lista[i+1]
        wys = random.randint(1, W)
        graf[elem1][elem2], graf[elem2][elem1] = wys, wys

    if m == n-1:
        return graf
    
    # dodajemy pozostale krawedzie
    else:
        for i in range(m-n+1):
            wys = random.randint(1, W)
            k = random.randint(1,n-1)
            l = random.randint(1,n-1)
            while k == l:
                l = random.randint(1,n-1)
            while graf[k][l] != 0 or k == l:
                k = random.randint(1,n-1)
                l = random.randint(1,n-1)
            graf[k][l], graf[l][k] = wys, wys
        return graf

def osiagalne_wierzch(graf, maxW, start = 0):
    n = len(graf) # liczba wierzcholkow
    odwiedzone = set()
        
    def dfs(a):
        odwiedzone.add(a)
        for sasiad in range(n):
            if sasiad not in odwiedzone and graf[a][sasiad] != 0 and graf[a][sasiad] < maxW:
                dfs(sasiad)
        
    dfs(start)
    return odwiedzone

def rys_graf(graf):
    G = nx.from_numpy_array(np.array(graf))

    pos = nx.spring_layout(G)
    labels1 = nx.get_edge_attributes(G,'weight')
    # labels2 =convert_list(schroniska)
    nx.draw_networkx(G, pos) #, with_labels = False)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels1)
    # nx.draw_networkx_labels(G, pos, labels=labels2, font_color="black")


def main():
    dane1 = dane()
    graf = los_graf(dane1[0], dane1[1], dane1[3])
    wynik = osiagalne_wierzch(graf, dane1[2],)
    rys_graf(graf)

    print('Zaczynając z wierzchołka ... profesor Bajtazar moze dojść do wierzchołków:', wynik)

if __name__ == "__main__":
    main()