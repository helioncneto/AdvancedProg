import random
class Elemento:
    def __init__(self,  dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None
    def get_dado(self):
        return self.dado
    def set_dado(self, dado):
        self.dado = dado
    def get_anterior(self):
        return self.anterior
    def set_anterior(self, anterior):
        self.anterior = anterior
    def get_proximo(self):
        return self.proximo
    def set_proximo(self, proximo):
        self.proximo = proximo

class Lista_encadeada:
    def __init__(self, tamanho):
        self.head = None
        self.tail = None
        for i in range(tamanho):
            self.adiciona(i)
    def __del__(self):
        print(self.mostra_lista())
    def vizinhos(self, dado):
        atual = self.head
        anterior = atual.get_anterior
        achou =False
        while not achou:
            if self.head.get_dado() == dado:
                achou = True
                print(atual.get_anterior().get_dado())
                print(None)
            else:
                if atual.get_dado() == dado:
                    achou = True
                    print(atual.get_anterior().get_dado())
                    print(atual.get_proximo().get_dado())
                else:
                    anterior = atual
                    atual = atual.get_anterior()
    def adiciona(self, dado):
        elemento = Elemento(dado)
        elemento.set_anterior(self.head)
        if self.head != None:
            anterior = elemento.get_anterior()
            anterior.set_proximo(elemento)
        self.head = elemento

    def mostra_lista(self):
        L = []
        atual = self.head
        proximo = self.head.get_proximo()
        anterior = self.head.get_anterior()
        while anterior != None:
            if atual == self.head:
                L.append([None, atual.get_dado(), anterior.get_dado()])
            else:
                L.append([proximo.get_dado(), atual.get_dado(), anterior.get_dado()])
            atual = anterior
            proximo = atual.get_proximo()
            anterior = atual.get_anterior()
        return L
    def add_posicao(self, dado, pos):
            atual = self.head
            anterior = atual.get_anterior()
            proximo = atual.get_proximo()
            achou = False
            while not achou:
                if atual.get_dado() == pos:
                    achou = True
                    elemento = Elemento(dado)
                    elemento.set_proximo(proximo)
                    elemento.set_anterior(atual)
                    proximo.set_anterior(elemento)
                    atual.set_proximo(elemento)
                atual = anterior
                proximo = atual.get_proximo()
                anterior = atual.get_anterior()



if __name__ == "__main__":
    lista = Lista_encadeada(5)
    lista.add_posicao(20, 3)
    lista.mostra_lista()
