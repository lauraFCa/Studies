
######## SIMULADOR DE DADO ##########
#Simular uso de um dado gerando um valor de 1 até 6

import random

class SimuladorDado:
    def __init__(self):
        #Configurações iniciais para usar o simulador: definir valor mínimo, um máximo e uma mensagem
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.msg = "Voce gostaria de gerar um novo valor para o dado?"
    
    def Iniciar(self):
        #fazer algum tipo de pergunta pro usuario
        resposta = input(self.msg)
        try:
            if resposta == "sim" or resposta == "s":
                self.GerarValorDado()
            elif resposta == "nao" or resposta == "n":
                print("Agradecemos a participação")
            else:
                print("Favor digitar 'sim' ou 'nao")
        except:
            print('Ocorreu um erro ao receber sua resposta')
            
    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
        
        
simulador = SimuladorDado()
simulador.Iniciar()

## Tela ##
import random
import PySimpleGUI as sg

class SimuladorDado:
    def __init__(self):
        #Configurações iniciais para usar o simulador: definir valor mínimo, um máximo e uma mensagem
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.msg = "Voce gostaria de gerar um novo valor para o dado?"
        #Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]
        
        #usar esses valores
    
    def Iniciar(self):
        #Criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        #ler valores na tela
        self.eventos, self.valores = self.janela.Read()
        
        #fazer algum tipo de pergunta pro usuario

        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDado()
            elif self.eventos == "nao" or self.eventos == "n":
                print("Agradecemos a participação")
            else:
                print("Favor digitar 'sim' ou 'nao")
        except:
            print('Ocorreu um erro ao receber sua resposta')
            
    def GerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
        
        
simulador = SimuladorDado()
simulador.Iniciar()

######## CHUTE O NUM ##########
#Criar algoritimo que gera valor aleatorio
#Usuario fica chutando numeros ate acertar

import random

class Chute:
    def __init__(self):
        self.valor_aleatorio = 0
        self.maximo = 100
        self.minimo = 1
        self.tentar = True
        
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentar == True:
                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print('Chute um valor mais baixo!')
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Chute um valor mais alto!')
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) == self.valor_aleatorio:
                    self.tentar = False
                    print('Parabens! Você acertou!')
        except:
            print('Favor digitar apenas numeros inteiros')
            self.Iniciar()    
    
    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um numero: ')
        
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.minimo, self.maximo)
        #print(self.valor_aleatorio)

chute = Chute()
chute.Iniciar()

## Tela ##
import random
import PySimpleGUI as sg


class Chute:
    def __init__(self):
        self.valor_aleatorio = 0
        self.maximo = 100
        self.minimo = 1
        self.tentar = True
        

    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Seu chute', size=(40, 0))],
            [sg.Input(size=(18, 0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(40, 10))]
        ]
        # criar janela
        self.janela = sg.Window('Chute o numero', layout=layout)
        self.GerarNumeroAleatorio()

        try:
            while True:
                self.evento, self.valores = self.janela.Read()
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar = False
                            print('Parabens! Você acertou!')
                            break
                        
                if self.evento == sg.WINDOW_CLOSED:
                    break
        except:
            print('Favor digitar apenas numeros inteiros')
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.minimo, self.maximo)
        # print(self.valor_aleatorio)


chute = Chute()
chute.Iniciar()


######## DECIDA POR MMIM ##########
#Faça uma pergunta para o progrmaa e ele deve te dar uma reposta
import random

class DecidaPorMim():
    def __init__(self):
        self.respostas=[
            'Com certeza, você deve fazer isso!',
            'Não sei, você quem sabe',
            'Não faz isso não...',
            'Acho que tá na hora certa'
        ]
        
    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))
        
decida = DecidaPorMim()
decida.Iniciar()

## Tela ##
import random
import PySimpleGUI as sg


class DecidaPorMim():
    def __init__(self):
        self.respostas=[
            'Com certeza, você deve fazer isso!',
            'Não sei, você quem sabe',
            'Não faz isso não...',
            'Acho que tá na hora certa'
        ]
        
    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Sua pergunta:')],
            [sg.Input(size=(50, 0), key='Pergunta')],
            [sg.Button('Decida')],
            [sg.Output(size=(50, 5))]
        ]
        # criar janela
        self.janela = sg.Window('Faca Uma Pergunta', layout=layout)
        while True:
            #ler a janela
            self.evento, self.valores = self.janela.Read()
            #fazendo algo com os valores
            if self.evento == 'Decida':
                print(random.choice(self.respostas))
                
            if self.evento == sg.WINDOW_CLOSED:
                break
                
decida = DecidaPorMim()
decida.Iniciar()

######## JOGO DECISOES ##########
#Jogo de decisoes com varios finais para cada resposta dada

class JogoAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte eu ou sul? (n/s)' # norte = A, sul = B
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo)' # espada = 1, escudo = 2
        self.pergunta3 = 'Qual é a sua especialidade?(linha de frente/tatico)' # linha de frente = 1, tático = 2
        
        self.finalDecisao1 = 'Você será um heroi na linha de frente!'
        self.finalDecisao2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalDecisao3 = 'Você irá se sacrificar na batalha!'
        self.finalDecisao4 = 'Você irá criar as táticas para essa batalha!'

        
    def Iniciar(self):
        resposta1 = input(self.pergunta1)
        
        if resposta1 == 'n':
            resposta1B = input(self.pergunta2)
            if resposta1B == 'espada':
                print(self.finalDecisao1)
            if resposta1B == 'escudo':
                print(self.finalDecisao2)
        
        if resposta1 == 's':
            resposta1B = input(self.pergunta3)
            if resposta1B == 'linha de frente':
                print(self.finalDecisao3)
            if resposta1B == 'tatico':
                print(self.finalDecisao4)


jogo = JogoAventura()
jogo.Iniciar()

## Tela ##
import PySimpleGUI as sg


class JogoAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte eu ou sul? (n/s)' # norte = A, sul = B
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo)' # espada = 1, escudo = 2
        self.pergunta3 = 'Qual é a sua especialidade?(linha de frente/tatico)' # linha de frente = 1, tático = 2
        
        self.finalDecisao1 = 'Você será um heroi na linha de frente!'
        self.finalDecisao2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalDecisao3 = 'Você irá se sacrificar na batalha!'
        self.finalDecisao4 = 'Você irá criar as táticas para essa batalha!'

        
    def Iniciar(self):
        
        # Layout
        layout = [
            [sg.Button('Iniciar')],
            [sg.Output(size=(60,0))],
            [sg.Input(size=(30,0),key='escolha')],
            [sg.Button('Responder')]
        ]
        # criar a janela
        self.janela = sg.Window('Jogo de Aventura!', layout=layout)
        while True:
            # ler os dados
            self.LerValores()
            # fazer algo com os dados
        
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'n':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.finalDecisao1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.finalDecisao2)
                if self.valores['escolha'] == 's':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'linha de frente':
                        print(self.finalDecisao3)
                    if self.valores['escolha'] == 'tatico':
                        print(self.finalDecisao4)
            
            if self.evento == sg.WINDOW_CLOSED:
                break


    def LerValores(self):
        self.evento, self.valores = self.janela.Read()
    

jogo = JogoAventura()
jogo.Iniciar()

