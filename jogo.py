from funcoes import *


continua = False
terminar = False
while continua != True and terminar == False:
    resposta = input('Você quer jogar o jogo? (Digite sim ou nao)\n')
    if resposta == 'sim':
        continua = True
    elif resposta == 'nao':
        terminar = True
        print("até breve")

while continua:
    baralho = cria_baralho()
    while possui_movimentos_possiveis(baralho):
        #
    if len(baralho) == 1:
        print ('voce ganhou')
    else:
        print ('voce perdeu')
    x = input('deseja jogar novamente? (Digite sim ou nao)\n')
    if x == 'nao':
        continua = False
        print('até breve')
    


