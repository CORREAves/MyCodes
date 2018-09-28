import GraficoGantt


def escalonador_Prior(qtdJobs, quantum, sobrecarga, horaDaChegada, listaTempoDeExecucao,prioridade):
    somaDosTemposDeExecucao = int(0)  # variavel para controlar a existencia de processos nao finalizados
    tempoTotal = int(0)  # tempo total(crescente)
    proximoJob = int(0)  # ponteiro
    tempoEmExecucao = []  # tempo de permanencia do processo ate seu fim(crescente)
    tempoDeExecucao = []
    voltandoFila = horaDaChegada  # quando o job entra na fila
    ponteiroPrioridade = int(3)  # ponteiro para prioridade
    listaProcessosGantt = []  # lista de lista de processos gantt, para reunir as listas de execucao que serao impressas
    # lista de tempo de execucao para cada processo,
    # considerando(0 = ocioso, 1 = em execucao, 2 = sobrecarga e 3 = em espera)

    for i in range(qtdJobs):  # declara as informacoes dos processos
        tempoEmExecucao.append(int(0))
        tempoDeExecucao.append(int(listaTempoDeExecucao[i]))
        somaDosTemposDeExecucao = somaDosTemposDeExecucao + tempoDeExecucao[i]
        listaProcessosGantt.append([])  # adiciona a lista de tempo na lista de gantt


    while somaDosTemposDeExecucao != 0:

        for g in range(qtdJobs):#procura o job com maior prioridade
            if tempoTotal >= horaDaChegada[g]:#Testa se o processo já chegou na fila
                if tempoDeExecucao[g] > 0:#Testa se o processo ainda nao terminou
                    if prioridade [g] <= ponteiroPrioridade:#apotará pro processo com maior prioridade
                        ponteiroPrioridade = g

        for j in range(qtdJobs):  # Procura o próximo processo a ser executado
            if tempoTotal >= horaDaChegada[j]:  # Testa se o processo já chegou na fila
                if tempoDeExecucao[j] > 0:  # Testa se o processo ainda nao terminou
                    if prioridade[j] == ponteiroPrioridade:# apenas se a prioridade for igual ao ponteiro de prioridade
                        if voltandoFila[j] <= voltandoFila[proximoJob]:  # escolhe o menor processo
                            proximoJob = j
                            ponteiroPrioridade = j

        for k in range(quantum):  # quantum de processos dentro e fora da CPU
            for m in range(qtdJobs):  # adiciona o Quantum aos processos fora da CPU
                if tempoTotal >= horaDaChegada[m]:  # Testa se o processo já chegou na fila
                    if tempoDeExecucao[m] > 0:  # Testa se o processo ainda nao terminou
                        if m != proximoJob:  # exclui processo que esta no processador
                            if tempoDeExecucao[proximoJob] > 0:  # Testa se o processo ainda nao terminou
                                tempoEmExecucao[m] = tempoEmExecucao[m] + 1
                                listaProcessosGantt[m].append(3)  # adiciona o marcador de tempem espera
                else:
                    listaProcessosGantt[m].append(0)  # adiciona o marcador de tempo ocioso para o processo
            if tempoDeExecucao[proximoJob] > 0:  # Testa se o processo ainda nao terminou
                tempoTotal = tempoTotal + 1
                tempoDeExecucao[proximoJob] = tempoDeExecucao[proximoJob] - 1
                tempoEmExecucao[proximoJob] = tempoEmExecucao[proximoJob] + 1
                listaProcessosGantt[m].append(1)  # adiciona o marcador de tempo em execucao para o processo

        if tempoDeExecucao[proximoJob] > 0:  # adiciona a sobrecarga aos processos dentro e fora da CPU
            for n in range(qtdJobs):  # adiciona o Quantum aos processos fora da CPU
                if tempoTotal >= horaDaChegada[n]:  # Testa se o processo já chegou na fila
                    if tempoDeExecucao[n] > 0:  # Testa se o processo ainda nao terminou
                        if n != proximoJob:  # exclui processo que esta no processador
                            # adiciona o sobrecarga aos processos fora da CPU
                            tempoEmExecucao[n] = tempoEmExecucao[n] + sobrecarga
                            # adiciona o marcador de tempo de sobrecarga para o processo
                            listaProcessosGantt[n].append(2)
            tempoTotal = tempoTotal + sobrecarga  # adiciona o sobrecarga ao tempo total
            # adiciona o sobrecarga ao processo dentro da CPU
            tempoEmExecucao[proximoJob] = tempoEmExecucao[proximoJob] + sobrecarga
            # adiciona o marcador de tempo de sobrecarga para o processo
            listaProcessosGantt[n].append(2)

        if tempoDeExecucao[proximoJob] == 0:  # Testa se o processo já terminou
            ponteiroPrioridade = 3

        voltandoFila[proximoJob] = tempoTotal

        somaDosTemposDeExecucao = int(0)
        for p in range(qtdJobs):  # adiciona o Quantum aos outros processos
            # atualiza a soma dos tempos de execucao
            somaDosTemposDeExecucao = somaDosTemposDeExecucao + tempoDeExecucao[p]
    else:
        print('Prioridades')
        # turnaround medio
        turnaroundMedio = float(0)
        print('Tempos em execução')
        for m in range(qtdJobs):
            print(tempoEmExecucao[m])
            turnaroundMedio = turnaroundMedio + tempoEmExecucao[m]
        print('Turnaround medio ', turnaroundMedio / qtdJobs)
        GraficoGantt.imprime_gantt(listaProcessosGantt)