#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import pi, pow
def area(forma, *parm):
    if forma == "quadrado":
        if len(parm) == 1:
            return pow(parm[0], 2)
        else:
            print "Para calcular a area do quadrado é necessária a medida de um dos lados"
    if forma == "circulo":
        if len(parm) == 1:
            return pow(parm[0], 2) * pi
        else:
            print "Para calcular a área do círculo é necessária a medida do raio"
    if forma == "triangulo":
        if len(parm) == 2:
            return parm[0]*parm[1]/2
        else:
            print "Para calcular a área do triangulo são necessárias as medidas altura e base"

if __name__ == "__main__":
    print area("triangulo", 3, 2, 1)

