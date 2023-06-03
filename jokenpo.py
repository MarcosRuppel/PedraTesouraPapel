# PUCPR - Bacharelado em Ciência da Computação
# Disciplina - Raciocínio Algorítmico
# Autor do código: Marcos Paulo Ruppel - turma 1U (Noite)
# Atividade somativa - jogo Jokenpo ( Pedra, Papel ou Tesoura )
# Versão 1.0.0
import os
import platform
import random
import getpass


def sair(): os.system("exit")


# verifica o sistema host para definir os comandos apropriados de terminal
if platform.system() == 'Windows':
    def clear(): os.system("cls")
    def pause(): os.system("pause")
elif platform.system() == 'Linux':
    def clear(): os.system("clear")
    def pause(): os.system("echo Pressione ENTER para continuar; read dummy;")
else:
    print("Desculpe, essa aplicação é incompatível com seu sistema operacional.")
    sair()


# modo jogador vs. CPU
def singleplayer():
    scoreplayer, scorecpu = 0, 0
    jogadasvalidas = ["pedra", "tesoura", "papel"]
    continuarjogo = 's'

    while continuarjogo.lower() == 's':
        clear()
        jogadaplayer = ""

        while jogadaplayer not in jogadasvalidas:
            clear()
            jogadaplayer = input("Faça sua jogada (pedra, tesoura ou papel?): ")

        jogadacpu = random.choice(jogadasvalidas)

        if jogadaplayer == jogadacpu:
            print("Ambos escolheram " + jogadacpu + ". Empate!")
            scoreplayer += 1
            scorecpu += 1
        elif jogadaplayer == "pedra":
            if jogadacpu == "tesoura":
                print("CPU escolheu " + jogadacpu + ". Vc venceu essa rodada!\n")
                scoreplayer += 1
            else:
                print("CPU escolheu " + jogadacpu + ". CPU venceu essa rodada!\n")
                scorecpu += 1
        elif jogadaplayer == "papel":
            if jogadacpu == "pedra":
                print("CPU escolheu " + jogadacpu + ". Vc venceu essa rodada!\n")
                scoreplayer += 1
            else:
                print("CPU escolheu " + jogadacpu + ". CPU venceu essa rodada!\n")
                scorecpu += 1
        elif jogadaplayer == "tesoura":
            if jogadacpu == "papel":
                print("CPU escolheu " + jogadacpu + ". Vc venceu essa rodada!\n")
                scoreplayer += 1
            else:
                print("CPU escolheu " + jogadacpu + ". CPU venceu essa rodada!\n")
                scorecpu += 1
        else:
            print("Opção inválida! Escolha pedra, tesoura ou papel\n")
            pause()
        print("Score atual:\n Jogador: %i\n CPU: %i\n" % (scoreplayer, scorecpu))
        continuarjogo = input("Deseja continuar jogando? (s/n): ")
    clear()
    print("\t\t ==== FIM DE JOGO! ====")
    print("\n\nPLACAR FINAL:\n Jogador: %i\n CPU: %i\n" % (scoreplayer, scorecpu))
    pause()
    return 0


# modo jogador vs. jogador
def multiplayer():
    scorep1, scorep2 = 0, 0
    player1 = input("Nome do jogador 1: ")
    player2 = input("Nome do jogador 2: ")
    jogadasvalidas = ["pedra", "tesoura", "papel"]
    continuarjogo = 's'

    def playervencedor(player):
        print(player1 + " = " + jogadaplayer1)
        print(player2 + " = " + jogadaplayer2)
        print(player + " venceu essa rodada!\n")

    while continuarjogo.lower() == 's':
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
            print("Ambos escolheram " + jogadaplayer2 + ". Empate!")
            scorep1 += 1
            scorep2 += 1
        elif jogadaplayer1 == "pedra":
            if jogadaplayer2 == "tesoura":
                playervencedor(player1)
                scorep1 += 1
            else:
                playervencedor(player2)
                scorep2 += 1
        elif jogadaplayer1 == "papel":
            if jogadaplayer2 == "pedra":
                playervencedor(player1)
                scorep1 += 1
            else:
                playervencedor(player2)
                scorep2 += 1
        elif jogadaplayer1 == "tesoura":
            if jogadaplayer2 == "papel":
                playervencedor(player1)
                scorep1 += 1
            else:
                playervencedor(player2)
                scorep2 += 1
        else:
            print("Opção inválida! Escolha pedra, tesoura ou papel\n")
            pause()
        print("Score atual:\n" + player1 + ": %i\n" % scorep1 + player2 + ": %i\n" % scorep2)
        continuarjogo = input("Desejam continuar jogando? (s/n): ")
    clear()
    print("\t\t ==== FIM DE JOGO! ====")
    print("\n\nPLACAR FINAL:\n" + player1 + ": %i\n" % scorep1 + player2 + ": %i\n" % scorep2)
    pause()
    return 0


# modo CPU vs. CPU
def cpuvscpu():
    return 0


# menu de seleção de jogo
def menuprincipal():
    clear()
    print("\t\t ====== PEDRA - PAPEL - TESOURA ======")
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
