from sys import stdin

a = int(stdin.readline())
b = int(stdin.readline())

for i in range(a):
    print(b)

    for j in range(b):
        print(i + j)

print("Bola 8 va a ganar")

# Crear una matriz escalonada
matriz = []
for i in range(a):
    fila = []
    for j in range(i + 1):
        fila.append(j)
    matriz.append(fila)

# Imprimir la matriz escalonada
for fila in matriz:
    print(fila)