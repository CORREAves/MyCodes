#Este programa será a interface entre o usuário e os algoritmos de escalonamento. Os dados de entrada serão tratados
#neste arquivo.

# -*- coding: latin1 -*-


import escalonadorRR
import escalonadorSJF
import escalonadorFIFO
import escalonadorEDF
import prioridades

if __name__ == "__main__":

    #lista de tempos de execução dos processos
    listaTempoDeExecucao = []
    tempoDeExecucao = []

    #lista de tempos de chegada dos processos
    listaDeTempoDeChegada = []
    tempoDeChegada =[]

    # lista de prioridades dos processos
    listaDePrioridades = []

    # lista de tempos de deadline dos processos
    listaDeTempoDeDeadline = []

    #Definição do quantum usado nas preempções
    #quantum = int(input('Qual o Quantum? '))

    #Definição do tempo de sobrecarga usado nas preempções
    #sobrecarga = int(input('Qual a sobrecarga? '))

    #Quantidade N de processos na entrada
    qtdJobs = int(input('Quantos Jobs serao? '))

    for x in range (qtdJobs):
        #print('Entre com os valores do processo ', x)

        tempoDeChegada.append(int(input('Qual o tempo de chegada? ')))
        tempoDeExecucao.append(int(input('Qual o tempo de execucao? ')))
        #prioridade = int( input('Qual a prioridade? '))
        #deadline = int( input('Qual o deadline do processo? '))

        listaDeTempoDeChegada.append(int(tempoDeChegada[x]))
        listaTempoDeExecucao.append(int(tempoDeExecucao[x]))
        #listaDePrioridades.append(prioridade)
        #listaDeTempoDeDeadline.append(deadline)

    #prioridades.escalonador_Prior(qtdJobs, quantum, sobrecarga, listaDeTempoDeChegada, listaTempoDeExecucao,listaDePrioridades)
    #escalonadorFIFO.escalonador_fifo(qtdJobs, quantum, listaDeTempoDeChegada, listaTempoDeExecucao)
    escalonadorSJF.escalonador_sjf(qtdJobs, listaDeTempoDeChegada, listaTempoDeExecucao)
    #escalonadorRR.escalonador_rr(qtdJobs, quantum, sobrecarga, listaDeTempoDeChegada, listaTempoDeExecucao)
    #escalonadorEDF.escalonador_edf(qtdJobs, quantum, sobrecarga, listaDeTempoDeChegada, listaTempoDeExecucao,listaDeTempoDeDeadline)
