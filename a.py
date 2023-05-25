mi_lista = [1, 2, 3, 3, 4, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7]

for num in mi_lista:
    while mi_lista.count(5) > 0:
        mi_lista.remove(5)

print(mi_lista)

print(mi_lista.count(7))

print("_________________________________")