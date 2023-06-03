# PUCPR - Bacharelado em Ciência da Computação
# Disciplina - Raciocínio Algorítmico
# Autor do código: Marcos Paulo Ruppel - turma 1U (Noite)
# Atividade somativa - jogo Jokenpo ( Pedra, Papel ou Tesoura )
# Versão 1.1.0
import os
import platform
import random
import getpass  # utilizada para mascarar a entrada dos jogadores no modo multiplayer


def sair():
    clear()
    print("Até logo!!")
    os.system("exit")


# verifica o SO host para definir os comandos apropriados de terminal
if platform.system() == 'Windows':
    def clear(): os.system("cls")  # limpa o terminal
    def pause(): os.system("pause")  # aguarda entrada do usuário antes de avançar
elif platform.system() == 'Linux':
    def clear(): os.system('clear')
    def pause(): os.system("echo Pressione ENTER para continuar; read dummy;")
else:
    print("Desculpe, essa aplicação é incompatível com seu sistema operacional.")
    sair()


# modo jogador vs. CPU
def singleplayer():
    scoreplayer, scorecpu = 0, 0
    jogadasvalidas = ["pedra", "tesoura", "papel"]
    continuarjogo = 's'

    while continuarjogo.lower() == 's':  # laço de repetição do jogo controlado pela variável continuarjogo
        clear()
        jogadaplayer = ""  # zera a jogada do player ao iniciar cada rodada

        while jogadaplayer not in jogadasvalidas:  # valida a jogada do player antes de prosseguir
            clear()
            jogadaplayer = input("Faça sua jogada (pedra, tesoura ou papel?): ")

        jogadacpu = random.choice(jogadasvalidas)  # sorteia a jogada da CPU dentro da lista de opções válidas

        if jogadaplayer == jogadacpu:
            print(f"Ambos escolheram {jogadacpu}.\nEmpate!\n")
        elif jogadaplayer == "pedra":
            if jogadacpu == "tesoura":
                print("CPU escolheu " + jogadacpu + ".\n## Vc venceu essa rodada! ##\n")
                scoreplayer += 1
            else:
                print("CPU escolheu " + jogadacpu + ".\n## CPU venceu essa rodada! ##\n")
                scorecpu += 1
        elif jogadaplayer == "papel":
            if jogadacpu == "pedra":
                print("CPU escolheu " + jogadacpu + ".\n## Vc venceu essa rodada! ##\n")
                scoreplayer += 1
            else:
                print("CPU escolheu " + jogadacpu + ".\n## CPU venceu essa rodada! ##\n")
                scorecpu += 1
        elif jogadaplayer == "tesoura":
            if jogadacpu == "papel":
                print("CPU escolheu " + jogadacpu + ".\n## Vc venceu essa rodada! ##\n")
                scoreplayer += 1
            else:
                print("CPU escolheu " + jogadacpu + ".\n## CPU venceu essa rodada! ##\n")
                scorecpu += 1
        else:
            clear()
            print("Erro!")
        print("Placar atual:\n Jogador: %i\n CPU: %i\n" % (scoreplayer, scorecpu))
        continuarjogo = input("Deseja continuar jogando? (s/n): ")
    clear()
    #  tela de resultados finais
    print("\t\t==== FIM DE JOGO! ====")
    print("\n\nPLACAR FINAL:\n Jogador: %i\n CPU: %i\n" % (scoreplayer, scorecpu))
    pause()
    menuprincipal()  # retorna ao menu inicial


# modo jogador vs. jogador
def multiplayer():
    scorep1, scorep2 = 0, 0
    player1 = input("Nome do jogador 1: ")
    player2 = input("Nome do jogador 2: ")
    jogadasvalidas = ["pedra", "tesoura", "papel"]
    continuarjogo = 's'

    def vencedor(player):  # função que recebe o player vencedor e exibe o resultado da rodada
        print(f">{player1} jogou {jogadaplayer1}\n>{player2} jogou {jogadaplayer2}\n")
        print(f"## {player} venceu essa rodada! ##\n")

    while continuarjogo.lower() == 's':  # laço de repetição do jogo controlado pela variável continuarjogo
        clear()
        jogadaplayer1 = ""
        jogadaplayer2 = ""
        while jogadaplayer1 not in jogadasvalidas:
            jogadaplayer1 = getpass.getpass(player1 + ", faça sua jogada (pedra, tesoura ou papel?): ")
            clear()
        while jogadaplayer2 not in jogadasvalidas:
            clear()
            jogadaplayer2 = getpass.getpass(player2 + ", faça sua jogada (pedra, tesoura ou papel?): ")

        if jogadaplayer1 == jogadaplayer2:
            print(f"Ambos escolheram {jogadaplayer2}.\nEmpate!\n")
        elif jogadaplayer1 == "pedra":
            if jogadaplayer2 == "tesoura":
                vencedor(player1)
                scorep1 += 1
            else:
                vencedor(player2)
                scorep2 += 1
        elif jogadaplayer1 == "papel":
            if jogadaplayer2 == "pedra":
                vencedor(player1)
                scorep1 += 1
            else:
                vencedor(player2)
                scorep2 += 1
        elif jogadaplayer1 == "tesoura":
            if jogadaplayer2 == "papel":
                vencedor(player1)
                scorep1 += 1
            else:
                vencedor(player2)
                scorep2 += 1
        else:
            clear()
            print("Erro!")
        print("Placar atual:\n" + player1 + ": %i\n" % scorep1 + player2 + ": %i\n" % scorep2)
        continuarjogo = input("Desejam continuar jogando? (s/n): ")
    clear()
    print("\t\t ==== FIM DE JOGO! ====")
    print(f"\n\nPLACAR FINAL:\n {player1}: %i\n {player2}: %i\n" % (scorep1, scorep2))
    pause()
    menuprincipal()  # retorna ao menu inicial


# modo CPU vs. CPU
def cpuvscpu():
    scorecpu1, scorecpu2 = 0, 0
    player1, player2 = "CPU1", "CPU2"
    jogadasvalidas = ["pedra", "tesoura", "papel"]
    continuarjogo = 's'

    def vencedor(player):  # função que recebe o player vencedor e exibe o resultado da rodada
        print(f">{player1} jogou {jogadacpu1}\n>{player2} jogou {jogadacpu2}\n")
        print(f"## {player} venceu essa rodada! ##\n")

    while continuarjogo.lower() == 's':  # laço de repetição do jogo controlado pela variável continuarjogo
        clear()
        jogadacpu1 = random.choice(jogadasvalidas)
        jogadacpu2 = random.choice(jogadasvalidas)

        if jogadacpu1 == jogadacpu2:
            print(f"Ambos escolheram {jogadacpu2}.\nEmpate!\n")
        elif jogadacpu1 == "pedra":
            if jogadacpu2 == "tesoura":
                vencedor(player1)
                scorecpu1 += 1
            else:
                vencedor(player2)
                scorecpu2 += 1
        elif jogadacpu1 == "papel":
            if jogadacpu2 == "pedra":
                vencedor(player1)
                scorecpu1 += 1
            else:
                vencedor(player2)
                scorecpu2 += 1
        elif jogadacpu1 == "tesoura":
            if jogadacpu2 == "papel":
                vencedor(player1)
                scorecpu1 += 1
            else:
                vencedor(player2)
                scorecpu2 += 1
        else:
            clear()
            print("Erro!")
        print(f"Placar atual:\n {player1}: %i\n {player2}: %i\n" % (scorecpu1, scorecpu2))
        continuarjogo = input("Deseja continuar jogando? (s/n): ")
    clear()
    #  tela de resultados finais
    print("\t\t==== FIM DE JOGO! ====")
    print(f"\n\nPLACAR FINAL:\n {player1}: %i\n {player2}: %i\n" % (scorecpu1, scorecpu2))
    pause()
    menuprincipal()  # retorna ao menu inicial


# menu de seleção de jogo
def menuprincipal():
    clear()
    print("\t\t ====== PEDRA - TESOURA - PAPEL ======")
    print("\n\nSelecione o modo de jogo:\n 1. Jogador vs CPU\n 2. Jogador x Jogador\n 3. CPU x CPU\n")
    print("Ou digite 0 para sair:\t")
    modojogo = int(input(""))
    if modojogo == 0:
        sair()
    elif modojogo == 1:
        singleplayer()
    elif modojogo == 2:
        multiplayer()
    elif modojogo == 3:
        cpuvscpu()
    else:
        clear()
        print("\n\nOpção inválida. Tente novamente.")
        pause()
        clear()
        menuprincipal()


menuprincipal()
