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
    
    numer = int(input("Podaj numer schroniska, z którego Bajtazar ma startować:"))
    if numer < 0 or numer >= n:
        raise Exception("Numer schroniska musi być > 0 i < ", n)
    
    return n, m, Wmax, W, numer

def los_graf(n, m, W):   
    graf = [[0 for i in range(n)] for j in range(n)]

    # losowanie nazw schronisk
    nazwy = los_nazwy(n)

    # lista wierzcholkow, ktore po kolei laczy sciezka - robimy graf rozpinajacy
    lista = random.sample(range(n), n)
    for i in range(n-1):
        elem1 = lista[i]
        elem2 = lista[i+1]
        wys = random.randint(1, W)
        graf[elem1][elem2], graf[elem2][elem1] = wys, wys

    dodatkowe_krawedzie = m - (n - 1)
    while dodatkowe_krawedzie > 0:
        k = random.randint(0, n-1)
        l = random.randint(0, n-1)
        if k != l and graf[k][l] == 0:
            wys = random.randint(1, W)
            graf[k][l], graf[l][k] = wys, wys
            dodatkowe_krawedzie -= 1
    return graf, nazwy

def lista_zamiana(lista):
    n = len(lista)
    wynik = {i: lista[i] for i in range(0, n)}
    return wynik
    
def los_nazwy(n):    
    nazwy_schronisk = ["Chatka", "Szrenica", "Strzecha", "Pasterka", "Kopa", "Puchatek", "Rycerz", "Halny", "Doktorek", "Profesorek",
                    "Rycerz", "Polanka", "Rysinka", "Sudetki", "Łysinka", "Domek", "Schron", "Czarownica", "Gzik", "Bigos",
                    "Piwko", "Słoneczne", "Pod chmurką", "Gwiazdka", "Milutkie", "Polanka", "Wrzosik", "Po drodze", "Tęczowe", "Tatrzańskie",
                  "Korona", "Burzowe", "Spadająca gwiazda", "Taterka", "Śnieżka", "Schron", "Wiedźma", "Zielone", "Niebieskie", "Srebrne",
                  "Przystanek", "Górka", "Wirch", "Wysokie", "Niżynka", "Kamyczek", "Na zakręcie", "Radosne", "Grota", "Słone",
                   "Zakręcone", "Piękne", "Koziczka", "Salamandra", "Koziołek", "Smaczne", "Przytulne", "Zacisze", "Cieplutkie", "Odpoczynek"]
    if n > len(nazwy_schronisk):
        return
    
    schroniska = random.sample(nazwy_schronisk, n)
    return schroniska

def osiagalne_wierzch(graf, maxW, start = 0):
    n = len(graf) # liczba wierzcholkow
    odwiedzone = []
        
    def dfs(a):
        odwiedzone.append(a)
        for sasiad in range(n):
            if sasiad not in odwiedzone and graf[a][sasiad] != 0 and graf[a][sasiad] <= maxW:
                dfs(sasiad)
        
    dfs(start)
    return odwiedzone

def rys_graf(graf, nazwy = 0):
    G = nx.from_numpy_array(np.array(graf))
    pos = nx.spring_layout(G)
    labels1 = nx.get_edge_attributes(G, 'weight')

    if nazwy == 0:
        nx.draw_networkx(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels1)

    else:
        labels2 = lista_zamiana(nazwy)
        nx.draw_networkx(G, pos, with_labels = False)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels1)
        nx.draw_networkx_labels(G, pos, labels=labels2, font_color="black")

    plt.show()


def main():
    dane1 = dane()
    graf, nazwy = los_graf(dane1[0], dane1[1], dane1[3])
    wynik = osiagalne_wierzch(graf, dane1[2], dane1[4])
    nazwy_osiagalnych = [(nazwy[indeks], indeks) for indeks in wynik]
    print('Zaczynając z wierzchołka', nazwy[dane1[4]], '(numer', dane1[4], ')', 'profesor Bajtazar moze dojść do wierzchołków:\n', 
          nazwy_osiagalnych,'przy maksymalnej bezpiecznej wysokości = ', dane1[2])
    rys_graf(graf, nazwy)

if __name__ == "__main__":
    main()
