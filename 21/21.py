from pilha import *
import random as rd

#Classe carta utilizada para criar um objeto que contenha o numero e o naipe da carta.
#Funções __repr__ e __str__ servem para imprimir o valor do objeto através da função print

class Carta:
    def __init__(self, naipe, numero):
        self.naipe = naipe
        self.numero = numero

    def __repr__(self):
        return "%s de %s \n" % (self.numero, self.naipe)

    def __str__(self):
        return "%s de %s" % (self.numero, self.naipe)


#Função contarPontos retorna o total de pontos em uma mão. Cartas comuns valem de 2 a 9.
#Áses são considerados como valendo somente 1 ponto. Valetes, damas e reis valem 10 pontos
def contarPontos(mao):
    maosum = 0
    for i in mao:
        if i.numero == 'A':
            maosum += 1
        elif i.numero == 'J' or i.numero == 'Q' or i.numero == 'K':
            maosum += 10
        else:
            maosum += i.numero
    return maosum

#Função verificarVitoria verifica se a soma de uma mão é maior, menor ou igual a 21.
#Retorna uma string correspondente a cada possibilidade da soma.
#"e" == estourou a pontuação; "g" == chegou aos 21 pontos; "pp" == menos que 21 pontos, então pode puxar cartas.
def verificarVitoria(sum):
    result = ''
    if sum > 21:
        result = 'e'
    elif sum == 21:
        result = 'g'
    elif sum < 21:
        result = 'pp'
    return result


deck = Pilha(52)

cartas = []

#Inicialização do baralho. as cartas são salvas ordenadamente no array "cartas".
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

#Embaralhamento das cartas. As cartas são adicionadas em ordem aleatória na pilha criada anteriormente.
for i in range(0, deck.tam):
    index = rd.randint(0, len(cartas)-1)
    deck.empilhar(cartas[index])
    cartas.pop(index)

flag = 0
mao = []
mesa = []
maosum = 0
mesasum = 0
maoresult = ''
mesaresult = ''

while True:

    #flag == 0 verifica se é a primeira rodada do jogo
    if flag == 0:
        print("Suas duas cartas são: ")
        c1 = deck.desempilhar()
        c2 = deck.desempilhar()
        print(str(c1)+'\n'+str(c2))
        mao = []
        mesa = []
        flag = 1
        mao.append(c1)
        mao.append(c2)

        print('\n')
        print("A mesa puxou as cartas")

        mc1 = deck.desempilhar()
        mc2 = deck.desempilhar()
        print(str(mc1)+'\n'+str(mc2))
        mesa.append(mc1)
        mesa.append(mc2)

    opc = input("Digite 'puxar' para puxar uma carta, ou 'parar' para contar os pontos\n")

    if opc == 'puxar':
        c = deck.desempilhar()
        print("A carta puxada foi "+str(c))
        mao.append(c)

        maosum = contarPontos(mao)
        print("O total de pontos é "+str(maosum))

        c = deck.desempilhar()
        mesa.append(c)
        print("A mesa puxou uma carta")

        mesasum = contarPontos(mesa)

        maoresult = verificarVitoria(maosum)
        mesaresult = verificarVitoria(mesasum)

        if maoresult == 'e':
            if mesaresult == 'e':
                print("A mesa tem "+str(mesasum)+" pontos\n")
                print("Você e a mesa estouraram a pontuação\n")
                opc = 'parar'
            elif mesaresult == 'g' or mesaresult == 'pp':
                print("A mesa tem "+str(mesasum)+" pontos\n")
                print("A mesa ganhou")
                opc = 'parar'
        elif maoresult == 'g':
            if mesaresult == 'e':
                print("Você ganhou!\n")
                opc = 'parar'
            if mesaresult == 'g':
                print("Você e a mesa terminaram com 21!\n")
                opc = 'parar'
            if mesaresult == 'pp':
                c = deck.desempilhar()
                mesa.append(c)
                print("A mesa puxou uma carta\n")
                flag = 2
        elif maoresult == 'pp':
            if mesaresult == 'e':
                print("A mesa estourou a pontuação\n")
                print("Você ganhou!")
                opc = 'parar'


    if opc == 'parar':
        mesasum = contarPontos(mesa)
        mesaresult = verificarVitoria(mesasum)
        maosum = contarPontos(mao)
        maoresult = verificarVitoria(maosum)

        #flag == 2 verifica se a mao chegou em 21 e se a mesa puxou mais uma carta
        if flag == 2:

            if mesaresult == 'e':
                print("Você terminou com "+str(maosum)+" pontos!\n")
                print("A mesa estourou a pontuação. Você ganhou!\n")
            if mesaresult == 'g':
                print("A mesa terminou com 21 pontos\n")
                if maoresult == 'g':
                    print("Você e a mesa terminaram com 21!\n")
            if mesaresult == 'pp':
                print("A mesa terminou com "+str(mesasum)+" pontos!\n")
                if mesasum > maosum:
                    print("A mesa ganhou!")
                elif mesasum < maosum:
                    print("Você ganhou!")

        if maoresult == 'pp' and mesaresult == 'pp':
            if mesasum>maosum:
                print("Você terminou com "+str(maosum)+" pontos!\n")
                print("A mesa terminou com "+str(mesasum)+" pontos!\n")
                print("A mesa ganhou")
            elif maosum>mesasum:
                print("Você terminou com "+str(maosum)+" pontos!\n")
                print("A mesa terminou com "+str(mesasum)+" pontos!\n")
                print("Você ganhou!")


        opc2 = input("Deseja jogar novamente? (s/n)\n")
        if opc2 == 's':
            flag = 0
        elif opc2 == 'n':
            break
