# PUCPR - Bacharelado em Ciência da Computação
# Disciplina - Raciocínio Algorítmico
# Autor do código: Marcos Paulo Ruppel - turma 1U (Noite)
# Atividade somativa - jogo Jokenpo ( Pedra, Papel ou Tesoura )
# Versão 1.2.2
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


def compararjogadas(jogadap1, jogadap2):  # compara as jogadas e retorna o vencedor
    if jogadap1 == jogadap2:
        return 0  # empate
    elif jogadap1 == "pedra":
        if jogadap2 == "tesoura":
            return 1  # player1 vence
        else:
            return 2  # player 2 vence
    elif jogadap1 == "papel":
        if jogadap2 == "pedra":
            return 1
        else:
            return 2
    elif jogadap1 == "tesoura":
        if jogadap2 == "papel":
            return 1
        else:
            return 2
    else:
        return 99  # retorno de erro


def resultadofinal(player1, player2, scorep1, scorep2):  # tela de resultados finais
    clear()
    print("\t\t==== FIM DE JOGO! ====")
    print(f"\n\nPLACAR FINAL:\n {player1}: %i\n {player2}: %i\n" % (scorep1, scorep2))
    pause()
    menuprincipal()  # retorna ao menu inicial


def vencedor(jvencedor, jogador1, jogadap1, jogador2, jogadap2):  # exibe o resultado da rodada
    if jvencedor == "nenhum":
        print(f"Ambos escolheram {jogadap1}.\nEmpate!\n")
    else:
        print(f">{jogador1} jogou {jogadap1}\n>{jogador2} jogou {jogadap2}\n")
        print(f"## {jvencedor} venceu essa rodada! ##\n")


def singleplayer():  # modo jogador vs. CPU
    scoreplayer, scorecpu = 0, 0
    jogadasvalidas = ["pedra", "tesoura", "papel"]
    continuarjogo = 's'
    player1 = input("Nome do jogador: ")
    player2 = "CPU"

    while continuarjogo.lower() == 's':  # laço de repetição do jogo controlado pela variável continuarjogo
        clear()
        jogadaplayer = ""  # zera a jogada do player ao iniciar cada rodada

        while jogadaplayer not in jogadasvalidas:  # valida a jogada do player antes de prosseguir
            clear()
            jogadaplayer = input(f"{player1}, faça sua jogada (pedra, tesoura ou papel?): ")

        jogadacpu = random.choice(jogadasvalidas)  # sorteia a jogada da CPU dentro da lista de opções válidas

        if compararjogadas(jogadaplayer, jogadacpu) == 0:
            vencedor("nenhum", player1, jogadaplayer, player2, jogadacpu)
        elif compararjogadas(jogadaplayer, jogadacpu) == 1:
            vencedor(player1, player1, jogadaplayer, player2, jogadacpu)
            scoreplayer += 1
        elif compararjogadas(jogadaplayer, jogadacpu) == 2:
            vencedor(player2, player1, jogadaplayer, player2, jogadacpu)
            scorecpu += 1
        else:
            print("Erro na execução do programa!")
        print("Placar atual:\n Jogador: %i\n CPU: %i\n" % (scoreplayer, scorecpu))
        continuarjogo = input("Deseja continuar jogando? (s/n): ")
    resultadofinal(player1, player2, scoreplayer, scorecpu)


def multiplayer():  # modo jogador vs. jogador
    scorep1, scorep2 = 0, 0
    player1 = input("Nome do jogador 1: ")
    player2 = input("Nome do jogador 2: ")
    jogadasvalidas = ["pedra", "tesoura", "papel"]
    continuarjogo = 's'

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

        if compararjogadas(jogadaplayer1, jogadaplayer2) == 0:
            vencedor("nenhum", player1, jogadaplayer1, player2, jogadaplayer2)
        elif compararjogadas(jogadaplayer1, jogadaplayer2) == 1:
            vencedor(player1, player1, jogadaplayer1, player2, jogadaplayer2)
            scorep1 += 1
        elif compararjogadas(jogadaplayer1, jogadaplayer2) == 2:
            vencedor(player2, player1, jogadaplayer1, player2, jogadaplayer2)
            scorep2 += 1
        else:
            print("Erro na execução do programa!")
        print("Placar atual:\n" + player1 + ": %i\n" % scorep1 + player2 + ": %i\n" % scorep2)
        continuarjogo = input("Desejam continuar jogando? (s/n): ")
    resultadofinal(player1, player2, scorep1, scorep2)


def cpuvscpu():  # modo CPU vs. CPU
    scorecpu1, scorecpu2 = 0, 0
    player1, player2 = "CPU1", "CPU2"
    jogadasvalidas = ["pedra", "tesoura", "papel"]
    continuarjogo = 's'

    while continuarjogo.lower() == 's':  # laço de repetição do jogo controlado pela variável continuarjogo
        clear()
        jogadacpu1 = random.choice(jogadasvalidas)
        jogadacpu2 = random.choice(jogadasvalidas)

        if compararjogadas(jogadacpu1, jogadacpu2) == 0:
            vencedor("nenhum", player1, jogadacpu1, player2, jogadacpu2)
        elif compararjogadas(jogadacpu1, jogadacpu2) == 1:
            vencedor(player1, player1, jogadacpu1, player2, jogadacpu2)
            scorecpu1 += 1
        elif compararjogadas(jogadacpu1, jogadacpu2) == 2:
            vencedor(player2, player1, jogadacpu1, player2, jogadacpu2)
            scorecpu2 += 1
        else:
            print("Erro na execução do programa!")
        print(f"Placar atual:\n {player1}: %i\n {player2}: %i\n" % (scorecpu1, scorecpu2))
        continuarjogo = input("Deseja continuar jogando? (s/n): ")
    resultadofinal(player1, player2, scorecpu1, scorecpu2)


def menuprincipal():  # menu de seleção de jogo
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
