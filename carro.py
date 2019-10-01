class Carro:
    def __init__(self,placa,cor):
        self.placa=placa
        self.cor = cor
        #print 'Carro de placa',placa, 'e cor',cor,'foi criado.'
    def seguir(self):
        print 'Carro',self.placa,self.cor, 'seguindo.'
    def virar_esquerda(self):
        print 'Carro',self.placa,self.cor, 'virou a esquerda.'

    def virar_direita(self):
        print 'Carro', self.placa,self.cor, 'virou a direita.'

class Motorista:
    def __init__(self,nome):
        self.nome = nome
    def dirigir(self,carro,direcao):
        print "Motorista",self.nome,'dirigindo.',
        if direcao=='em frente':
            carro.seguir()
        elif direcao=='direita':
            carro.virar_direita()
        else:
            carro.virar_esquerda()


if __name__=='__main__':
    c1 = Carro('abc1234','branco')
    c1.seguir()
    c1.virar_direita()
    c1.virar_esquerda()
    m1=Motorista('Fulano')
    m1.dirigir(c1,'em frente')
    m1.dirigir(c1,'direita')
    m1.dirigir(c1,'esquerda')