# -*- coding: UTF8 -*-
# Jogo da forca usando POO
# by: Felipe Bausen Boldt


import random


lista_tabuleiro = [
    '''
    +---------+
    |         |
    |
    |
    |
    ======
    ''',
    '''
        +---------+
                  |
        |         0
        |
        |
        |
        ======
        ''',
    '''
            +---------+
                      |
            |         0
            |         |
            |         
            |
            ======
            ''',
    '''
                +---------+
                          |
                |         0
                |        /|
                |
                |
                ======
                ''',
    '''
                +---------+
                          |
                |         0
                |        /|\
                |
                |
                ======
                ''',
    '''
                    +---------+
                              |
                    |         0
                    |        /|\
                    |        /
                    |
                    ======
                    ''',
    '''
                        +---------+
                                  |
                        |         0
                        |        /|\
                        |        / \
                        |
                        ======
                        '''
]
#Procurar palavras

def buscar_palavra():
    with open("palavras.txt", "rt") as arquivo:
        banco = arquivo.readlines ()

    return banco[random.randint(0, len(banco)-1)].strip()

#Adicionar palavras ao jogo
def adicionar_palavra():
     palavra = input('Qual palavra deseja Adicionar?')
     with open("palavras.txt", "at") as arquivo:
         arquivo.write('\n'+palavra)
     print ('Palavra adicionada com Sucesso!')
     menu()

#Menu de Opções
def menu():
    opc = int(input('O que deseja fazer?\n1-Jogar 2-Adicionar uma nova palavra'))

    if opc == 2:
        adicionar_palavra()
    else:
        main()

#Classe de Jogo
class Forca:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_certas = []
        self.letras_erradas =[]

#Método do jogo
    def adivinha_letra(self, letra):
        if letra.upper() in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra.upper())
        elif letra.upper() not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra.upper())
        else:
            return False
        return True

    #Método fim de jogo
    def fim_de_jogo (self):
        return self.jogo_ganho() or (len(self.letras_erradas) == 6)

#Método verifica se venceu
    def jogo_ganho(self):
        return '_' not in self.esconde_palavra()

#Método que esconde a palavra
    def esconde_palavra(self):
        palavra_escondida = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                palavra_escondida += '_ '
            else:
                palavra_escondida += letra
        return palavra_escondida


#Método status do jogo
    def status_do_jogo(self):
        print(lista_tabuleiro[len(self.letras_erradas)])
        print(self.esconde_palavra())
        print('Letras corretas:\n', self.letras_certas)
        print('Letras erradas: \n', self.letras_erradas)

#Função Iniciar Jogo
def main():
    forca1 = Forca(buscar_palavra())

    while (not forca1.fim_de_jogo()):
        forca1.status_do_jogo()
        forca1.adivinha_letra(input('Escolha uma letra :'))

#Win or Lose
    if forca1.jogo_ganho():
        print('Parabéns, você acertou a palavra')
    else:
        print('Você perdeu :(  Tente Novamente\n A Palavra escondida era :', forca1.palavra)


#Menu
menu()

#Fim de Projeto














