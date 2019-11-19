class Pilha:
    def __init__(self,tam):
        self.tam = tam
        self.topo = 0
        self.p = [None]*tam

    def vazia(self):
        return self.topo == 0
    def cheia(self):
        return self.topo == self.tam
    def empilhar(self, item):
        if (self.cheia()):
            return print("Pilha cheia")
        else:
            self.p[self.topo] = item
            self.topo += 1
    def desempilhar(self):
        if (self.vazia() == True):
            return print("Pilha vazia")
        else:
            self.topo -= 1
            return self.p[self.topo]
    def imprimir(self):
        for i in self.p[:self.topo]:
            print(i)

        #print(self.p[:self.topo])
