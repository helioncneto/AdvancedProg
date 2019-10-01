# -*- coding: utf-8 -*-
class Pilha:
    def __init__(self, tamanho):
        pass
        # Inicia a pilha vazia com determinados tamanho
    def tamanho(self):
        pass
        # retorna o tamanho da lista
    def esvaziar_lista(self):
        pass
        # zera a lista
    def adiciona_valor(self, valor):
        pass
        # Adiciona valor no fim da lista
    def remove_valor(self):
        pass
        # Remove o primeiro valor da lista

class Fila_simples(Pilha):
    def __init__(self, tamanho, inicio, fim):
        pass
        # Inicia a lista uma lista com determinado tamanho com um indice de inicio e fim
        # Cada valor será composto por: [indice_anterior, valor]
    def adiciona_valor(self, valor):
        pass
        # Adiciona um valor no fim da fila apontando para o indice enterior
    def retorna_primeiro_indice(self):
        pass
        # Retorna o primeiro indice
    def retorne_ultimo_indice(self):
        pass
        # Retorna valor do ultimo indice
    def remove_valor(self):
        pass
        # Remove sempre o primeiro valor da lista
class Fila_duplamente(Fila_simples):
    def __init__(self, tamanho, inicio, fim):
        pass
        # Inicia a lista uma lista com determinado tamanho com um indice de inicio e fim.
        # Cada valor será composto por: [indice_anterior, valor, indice_proximo]
    def adiciona_valor(self, posicao, valor):
        pass
        # Adiciona um valor na posição especifica atualizando os valores posteriores
    def remove_valor(self, posicao):
        pass
        # Remove o valor especifico atualizando os valores posteriores