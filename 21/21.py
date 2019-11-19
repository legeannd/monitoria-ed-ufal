from pilha import *
import random as rd

class Carta:
    def __init__(self, naipe, numero):
        self.naipe = naipe
        self.numero = numero

    def __repr__(self):
        return "%s de %s \n" % (self.numero, self.naipe)

    def __str__(self):
        return "%s de %s" % (self.numero, self.naipe)

    def mostrarCarta(self):
        print(str(self.numero)+' de '+str(self.naipe))

deck = Pilha(52)

cartas = []

for i in range(1, 5):
    if i == 1:
        naipe = 'Espadas'
    elif i == 2:
        naipe = 'Copas'
    elif i == 3:
        naipe = 'Ouros'
    elif i == 4:
        naipe = 'Paus'
    for j in range(1, 14):
        if j == 11:
            numero = 'J'
        elif j == 12:
            numero = 'Q'
        elif j == 13:
            numero = 'K'
        elif j == 1:
            numero = 'A'
        else:
            numero = j
        cartas.append(Carta(naipe, numero))

for i in range(0, deck.tam):
    index = rd.randint(0, len(cartas)-1)
    deck.empilhar(cartas[index])
    cartas.pop(index)

flag = 0
mao = []
while True:
    if flag == 0:
        print("Suas duas cartas são: ")
        c1 = deck.desempilhar()
        c2 = deck.desempilhar()
        print(str(c1)+'\n'+str(c2))
        mao = []
        flag = 1
        mao.append(c1)
        mao.append(c2)

    opc = input("Digite 'puxar' para puxar uma carta, ou 'parar' para contar os pontos\n")

    if opc == 'puxar':
        c = deck.desempilhar()
        print("A carta puxada foi "+str(c))
        mao.append(c)

        sum = 0
        for i in mao:
            if i.numero == 'A':
                sum += 1
            elif i.numero == 'J' or i.numero == 'Q' or i.numero == 'K':
                sum += 10
            else:
                sum += i.numero
        print("O total de pontos é "+str(sum))
        if sum > 21:
            print("Você estourou a pontuação. Fim de jogo.")
            opc = 'parar'
        elif sum < 21:
            print("Você ainda pode puxar cartas")
        elif sum == 21:
            print("Parabéns, você ganhou!")
            opc = 'parar'

    if opc == 'parar':
        print("Sua pontuação final é: "+str(sum))
        opc2 = input("Deseja jogar novamente? (s/n)\n")
        if opc2 == 's':
            flag = 0
        elif opc2 == 'n':
            break
