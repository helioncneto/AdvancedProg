# -*- coding: utf-8 -*-
import estacionamento
from carro import Carro
from estacionamento import *
import random
import string
import time

def gera_placa():
    letras = string.ascii_uppercase
    codigo = ''.join(random.choice(letras) for _ in range(4))
    return codigo

cores_disponiveis = ["branco", "verde", "vermelho", "preto"]
e = Estacionamento(3)

while(True):
    c = Carro(gera_placa(), cores_disponiveis[random.randint(0, 3)])
    print("Foi criado um carro " + c.cor + " com placa " + c.placa)
    e.estacionar(c)
    print("O carro entrou no estacionamento.")
    for i in e.vagas:
        if e.vagas[i].permanencia() >= 6.0:
            print("Retirando o carro com a placa " + e.vagas[i].carro.placa + " devido estar a mais de 6s na vaga.")
            e.sair_carro(e.vagas[i].carro)
    e.info_estacionamento()
    time.sleep(random.randint(1, 10))


