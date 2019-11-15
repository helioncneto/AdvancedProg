# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

class Ev_Dividir:
    def __init__(self, nome, tempo):
        self.nome_bacteria = nome
        self.tempo = tempo

    def __repr__(self):
        return self.nome_bacteria

    def processar(self):
        print "Em ", self.tempo, 'a bactéria', self.nome_bacteria, 'se dividiu'
        ev1 = Ev_Dividir(self.nome_bacteria + '.1', self.tempo + 1)
        ev2 = Ev_Dividir(self.nome_bacteria + '.2', self.tempo + 1)
        return ev1, ev2


class Simulador:
    def __init__(self, fim):
        self.eventos = []
        self.tempo = 0
        self.fim = fim
        self.basterias_tempo = dict()
        self.tempo_vida = list()

        ev = Ev_Dividir('1', 0)
        self.adiciona(ev)

        self.processar()

        while ((self.tempo < self.fim) and (len(self.eventos) != 0)):
            self.processar()
        print("A média de vida das bactérias é: " + str(sum(self.tempo_vida)/len(self.tempo_vida)))

    def adiciona(self, ev):
        achei = False
        for i in self.eventos:
            if i.tempo > ev.tempo:
                achei = True
                break
        if achei:
            posicao = self.eventos.index(i)
            self.eventos.insert(posicao, ev)
        else:
            self.eventos.append(ev)

    def retira(self):
        self.tempo_vida.append(float(self.eventos[0].tempo) - float(self.tempo))
        return self.eventos.pop(0)

    def processar(self):
        ev = self.retira()
        evs = ev.processar()
        self.tempo = ev.tempo
        if self.tempo in self.basterias_tempo.keys():
            self.basterias_tempo[self.tempo] = self.basterias_tempo[self.tempo] + 2
        else:
            self.basterias_tempo[self.tempo] = 2
        for i in evs:
            self.adiciona(i)



sim = Simulador(10)

plt.plot(sim.basterias_tempo.keys(), sim.basterias_tempo.values())
plt.ylabel("Bactérias")
plt.xlabel("Tempo")
plt.show()