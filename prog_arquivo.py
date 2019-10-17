# -*- coding: utf-8 -*-

texto1 = open("texto1", "r")
texto2 = open("texto2", "r")
mesclagem = open("texto3", "w")
mesclagem.write(texto1.read() + "\n" + texto2.read())
texto2.close()
mesclagem.close()

texto1.seek(0)
L = list()
for line in texto1:
    L.append(line[::-1])

texto1 = open("texto1", "w")
texto1.writelines(L)
texto1.close()





