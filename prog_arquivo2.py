# -*- coding: utf-8 -*-

arquivo = open("texto2", "r")

lista = []
def guarda_letra(string):
    L = []
    for i in range(len(string)):
        if string[i].lower() in "aeiou":
            if i >=3:
                L.append([string[i - 1], string[i - 2], string[i - 3]])
            elif i >= 2:
                L.append([string[i-1], string[i-2]])
            elif i >=1:
                L.append([string[i - 1]])

    return L

for i in arquivo.readlines():
    lista.append(guarda_letra(i))

print(lista)



