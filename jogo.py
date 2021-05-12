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
        print("O estado atual do baralho é:\n") 
        for i in range(len(baralho)):
           print(str(i + 1) + ". " + baralho[i])
        numero_da_carta = int(input(f"Escolha uma carta: (1-{len(baralho)})"))
        numero_da_carta = numero_da_carta - 1
        movimentos = lista_movimentos_possiveis(baralho, numero_da_carta)
        while movimentos == []:
            numero_da_carta = int(input(f"A carta {baralho[numero_da_carta]} não pode ser movida. Escolha uma carta: (1-{len(baralho)})"))
            numero_da_carta = numero_da_carta -1
            movimentos = lista_movimentos_possiveis(baralho, numero_da_carta)
        if len(movimentos) == 1:
            if movimentos[0] == 1:
                empilha(baralho,numero_da_carta,numero_da_carta-1)
            else:
                empilha(baralho,numero_da_carta,numero_da_carta-3)
        else: 
            print("Sobre qual carta deseja empilhar o",baralho[numero_da_carta]) 
            print('1. ',baralho[numero_da_carta-1])
            print('2. ',baralho[numero_da_carta-3]) 
            escolha = input("Escolha 1 ou 2! ")
            if escolha == "1":
                empilha(baralho,numero_da_carta,numero_da_carta-1)
            elif escolha == "2":
                empilha(baralho,numero_da_carta,numero_da_carta-3)

    if len(baralho) == 1:
        print ('voce ganhou')
    else:
        print ('voce perdeu')
    x = input('deseja jogar novamente? (Digite sim ou nao)\n')
    if x == 'nao':
        continua = False
        print('até breve')
    


