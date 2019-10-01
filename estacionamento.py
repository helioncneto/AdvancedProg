# -*- coding: utf-8 -*-
from carro import Carro
import time

class Vaga:
    def __init__(self,carro,chegada):
        self.carro=carro
        self.chegada=chegada
    def permanencia(self):
        if self.chegada == 0:
            return -1
        return round(time.time()-self.chegada, 2)
    def insere_carro(self,carro):
        self.carro=carro
        self.chegada=time.time()

class Estacionamento:
    def __init__(self,vagas):
        #self.vagas = {}.fromkeys(range(vagas),Vaga(None,0))
        self.vagas = {}
        for i in range(vagas):
            self.vagas[i] = Vaga(None,0)
        self.espera=[]
    def estacionar(self,carro):
        vaga=self.busca_vaga()
        if vaga==-1:
            self.espera.append(carro)
        else:
            self.vagas[vaga].insere_carro(carro)

    def sair_carro(self,carro):
        for i in self.vagas:
            if self.vagas[i].carro==carro:
                self.vagas[i] = Vaga(None, 0)
    def busca_vaga(self):
        for i in self.vagas:
            if self.vagas[i].carro==None:
                return i
        return -1
    def info_estacionamento(self, mostrar_livre=False):
        print("Detalhes do estacionamento: ")
        for i in self.vagas:
            if self.vagas[i].carro != None:
                print("\tO carro " + self.vagas[i].carro.cor + " com a placa " + self.vagas[i].carro.placa +
                      " está estacionado na vaga " + str(i) + " há " + str(self.vagas[i].permanencia()) + " segundos.")
            else:
                if mostrar_livre:
                    print("\tVaga " + str(i) + " livre.")
        if len(self.espera) != 0:
            print("Carros em espera: ")
            for i in range(len(self.espera)):
                print("\tCarro " + self.espera[i].cor + " com a placa " + self.espera[i].placa)

if __name__ == "__main__":
    e1 = Estacionamento(10)
    c1 = Carro("aaaa", "branco")
    c2 = Carro("abbbb", "verde")
    e1.estacionar(c1)
    time.sleep(2)
    e1.estacionar(c2)
    e1.info_estacionamento()


