import random
import math


def createHam(n, s, choice):
    matrix = []
    for i in range(n):
        matrix.append([0 for j in range(n)])

    #generuje sciezke
    path = []
    p = n
    while p:
        num = random.randint(0, n-1)
        if num not in path:
            path.append(num)
            p -= 1
    if choice:
        print(path)

    for i in range(n-1):
        matrix[path[i]][path[i+1]] = 1
        matrix[path[i+1]][path[i]] = 1
    matrix[path[0]][path[n-1]] = 1
    matrix[path[n-1]][path[0]] = 1

    cnt = math.floor(n*n*s)-(5*n)
    while cnt > 5:
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
            cnt -= 6

    if choice == 0:
        row = random.randint(0, n-1)
        for i in range(n):
            matrix[row][i] = 0
            matrix[i][row] = 0

    return matrix


def printMatrix(matrix,n):
    print("\t",end="")
    print(*range(n))
    print()
    for i in range(n):
        print(i, end="\t")
        print(*matrix[i])
    print("\n\n")


def DFS_Euler(matrix, n, v):
    visited = []
    for i in range(n):
        if matrix[v][i] == 1:
            matrix[v][i] = 0
            matrix[i][v] = 0
            DFS_Euler(matrix, n, i)
    if v not in visited:
        visited.append(v)
        print(v, end=" ")

    #return res


x = 1
while x:
    print("Podaj ilosc wierchołków w grafie")
    n = int(input())

    ham3 = createHam(n, 0.3, 1)
    ham7 = createHam(n, 0.7, 1)
    not_ham5 = createHam(n, 0.5, 0)

    printMatrix(ham3, n)
    printMatrix(ham7, n)
    printMatrix(not_ham5, n)

    DFS_Euler(ham7, n, 0)

    print("\n\n0 - aby zakonczyc program")
    print("1 - aby wykonac go jeszcze raz")
    x = int(input())
