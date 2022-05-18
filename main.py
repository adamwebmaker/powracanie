import random
import math

# generowanie grafu
def createHam(n, s, choice):
    matrix = []
    for i in range(n):
        matrix.append([0 for j in range(n)])    # generujemy tablice 2wym z zerami

    # generuje cykl hamiltona
    path = []
    p = n
    while p:
        num = random.randint(0, n-1)
        if num not in path:
            path.append(num)
            p -= 1
    if choice:
        print(path)

    # zapisuje krawędź nieskierowaną do macierzy
    for i in range(n-1):
        matrix[path[i]][path[i+1]] = 1
        matrix[path[i+1]][path[i]] = 1

    # łączymy ostatni z pierwszym wierzchołkiem
    matrix[path[0]][path[n-1]] = 1
    matrix[path[n-1]][path[0]] = 1

    # generuje liczbe krawędzi ze wzoru \/
    # https://www.cs.put.poznan.pl/tzok/public/aisd-04-backtracking.html?fbclid=IwAR1DemNMvPZDVljj5btrbs9NhivpUU1Y1fSl5Z-9CUcUyrIvprmWZEnBP7c
    cnt = math.floor((n*(n-1)*s)/2)
    while cnt > 5:
        # losujemy 3 różne niepołączone wierzchołki
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        z = random.randint(0, n-1)
        if (x != y) and (x != z) and (y != z) and (matrix[x][y] == 0) and (matrix[x][z] == 0) and (matrix[z][y] == 0):
            matrix[x][y] = 1
            matrix[x][z] = 1
            matrix[y][x] = 1
            matrix[y][z] = 1
            matrix[z][x] = 1
            matrix[z][y] = 1
            cnt -= 6    # odejmuje liczbe dodanych krawędzi

    # jeśli niehamiltonowski izoluje wierzchołek (zeruje wiersz i kolumne)
    if choice == 0:
        row = random.randint(0, n-1)
        for i in range(n):
            matrix[row][i] = 0
            matrix[i][row] = 0

    return matrix


def printMatrix(matrix):
    n = len(matrix)
    print("\t",end="")
    print(*range(n))
    print()
    for i in range(n):
        print(i, end="\t")
        print(*matrix[i])
    print("\n\n")


def DFS_Euler(matrix, v):
    n = len(matrix)
    # przechodzimy po kolejnych połączonych wierzchołkach i zerujemy odwiedzoną krawędź
    for i in range(n):
        if matrix[v][i] == 1:
            matrix[v][i] = 0
            matrix[i][v] = 0
            DFS_Euler(matrix, i)

    # wypisujemy
    print(v, end=" ")


def adjAndnotInPath(matrix, v, pos, path):
    # sprawdzamy czy istnieje krawędź między ostatnim dodanym do ścieżki a sprawdzanym
    if matrix[ path[pos-1] ][v] == 0:
        return False

    # czy wierzchołek nie jest już w ścieżce
    for vertex in path:
        if vertex == v:
            return False

    return True


def hamCycleUtil(matrix, path, pos):

    # sprawdzamy czy wszystkie wierzchołki są już w ścieżce
    if pos == len(matrix):
        if matrix[ path[pos-1] ][ path[0] ] == 1: # czy ostatni może połączyć się z pierwszym
            return True
        else:
            return False

    # przechodzimy po wszystkich wierzchołkach pomijając 0 (już w ścieżce)
    for v in range(1,len(matrix)):
        if adjAndnotInPath(matrix, v, pos, path) == True: # jeśli jest następnikiem i nie ma go jeszcze w ścieżce
            path[pos] = v # dopisujemy jako kolejny wierzchołek w ścieżce 
            if hamCycleUtil(matrix, path, pos+1) == True: # i podajemy kolejny do wywołania rekurencyjnego 
                return True

            # usuwamy wierzchołek ze ścieżki jeśli nie prowadzi do rozwiązania
            path[pos] = -1

    return False


def hamCycle(matrix):
    # tworzymy ścieżkę z -1 (nieodwiedzony)
    path = [-1] * len(matrix)

    # zaczynamy ścieżkę wierzchołkiem 0
    path[0] = 0


    if hamCycleUtil(matrix, path,1) == False:
        print ("Nie ma rozwiązania")
        return False

    for v in path:
        print(v, end=" ")
    print(path[0])

    return True

x = 1
while x:
    print("Podaj ilosc wierchołków w grafie")
    n = int(input())

    '''
    ham3 = createHam(n, 0.3, 1)
    ham7 = createHam(n, 0.7, 1)
    not_ham5 = createHam(n, 0.5, 0)

    printMatrix(ham3)
    printMatrix(ham7)
    printMatrix(not_ham5)

    print("Euler: ")
    DFS_Euler(ham7, 0)
    print()
    print()

    hamCycle(ham3)
    hamCycle(ham7)
    '''

    w = 2
    while w not in [0, 1]:
        print("0 - jesli chcesz aby program wygenerowal graf")
        print("1 - aby podac krawedzie w grafie")
        w = int(input())

    if w == 1:
        graph = []
        for i in range(n):
            print("{} wiersz: ".format(i), end=" ")
            temp = []
            for j in range(n):
                num = 2
                while num not in [0,1]:
                    num = int(input())
                temp.append(num)
            graph.append(temp)

    if w == 0:
        print("Podaj nasycenie (od 0 do 1)")
        s = float(input())
        graph = createHam(n, s, 1)

    z = ''
    while True:
        w = ''
        while w not in ['e', 'h']:
            print("e - algortym szukania cyklu eulera")
            print("h - algorytm szukania cyklu hamiltona")
            w = input()

            if w == 'e':
                DFS_Euler(graph, 0)
            if w == 'h':
                hamCycle(graph)
            
        print("\n\n0 - aby zakonczyc program dla tego grafu")
        print("1 - aby wykonac go jeszcze raz")
        z = input()
        if z == '0':
            break

    print("\n\n0 - aby zakonczyc program")
    print("1 - aby wykonac go jeszcze raz")
    x = int(input())
