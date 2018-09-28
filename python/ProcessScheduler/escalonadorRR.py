import GraficoGantt


def escalonador_rr(qtdJobs, quantum, sobrecarga, horaDaChegada, listaTempoDeExecucao):
    somaDosTemposDeExecucao = int(0)  # variavel para controlar a existencia de processos nao finalizados
    tempoTotal = int(0)  # tempo total(crescente)
    proximoJob = int(0)  # ponteiro
    tempoDeExecucao = []
    tempoEmExecucao = []  # tempo de permanencia do processo ate seu fim(crescente)
    voltandoFila = []  # quando o job entra na fila
    listaProcessosGantt = []  # lista de lista de processos gantt, para reunir as listas de execucao que serao impressas
    # lista de tempo de execucao para cada processo,
    # considerando(0 = ocioso, 1 = em execucao, 2 = sobrecarga e 3 = em espera)

    for i in range(qtdJobs):  # declara as informacoes dos processos
        tempoEmExecucao.append(int(0))
        voltandoFila.append(int(horaDaChegada[i]))
        tempoDeExecucao.append(int(listaTempoDeExecucao[i]))
        somaDosTemposDeExecucao = somaDosTemposDeExecucao + tempoDeExecucao[i]
        listaProcessosGantt.append([])  # adiciona a lista de tempo na lista de gantt


    while somaDosTemposDeExecucao != 0:

        for j in range(qtdJobs):  # Procura o próximo processo a ser executado
            if tempoTotal >= horaDaChegada[j]:  # Testa se o processo já chegou na fila
                if tempoDeExecucao[j] > 0:  # Testa se o processo ainda nao terminou
                    if voltandoFila[j] <= voltandoFila[proximoJob]:  # escolhe o menor processo
                        proximoJob = j

        for k in range(quantum):  # processo dentro da CPU
            for m in range(qtdJobs):  # adiciona o Quantum aos outros processos
                if tempoTotal >= horaDaChegada[m]:  # Testa se o processo já chegou na fila
                    if tempoDeExecucao[m] > 0:  # Testa se o processo ainda nao terminou
                        if m != proximoJob:  # exclui processo que esta no processador
                            if tempoDeExecucao[proximoJob] > 0:  # Testa se o processo ainda nao terminou
                                tempoEmExecucao[m] = tempoEmExecucao[m] + 1
                                listaProcessosGantt[m].append(3)  # adiciona o marcador de tempo em espera
                else: # o processo ainda não está pronto para executar
                    listaProcessosGantt[m].append(0)  # adiciona o marcador de tempo ocioso para o processo
            if tempoDeExecucao[proximoJob] > 0:  # Testa se o processo ainda nao terminou
                tempoTotal = tempoTotal + 1
                tempoDeExecucao[proximoJob] = tempoDeExecucao[proximoJob] - 1
                tempoEmExecucao[proximoJob] = tempoEmExecucao[proximoJob] + 1
                listaProcessosGantt[m].append(1)  # adiciona o marcador de tempo em execucao para o processo

        if tempoDeExecucao[proximoJob] > 0:  # adiciona a sobrecarga ao processo na cpu
            for n in range(qtdJobs):  # adiciona o Quantum aos outros processos
                if tempoTotal >= horaDaChegada[n]:  # Testa se o processo já chegou na fila
                    if tempoDeExecucao[n] > 0:  # Testa se o processo ainda nao terminou
                        if n != proximoJob:  # exclui processo que esta no processador
                            tempoEmExecucao[n] = tempoEmExecucao[n] + sobrecarga
                            listaProcessosGantt[n].append(2)  # adiciona o marcador de tempo de sobrecarga para o processo
            tempoTotal = tempoTotal + sobrecarga
            tempoEmExecucao[proximoJob] = tempoEmExecucao[proximoJob] + sobrecarga
            listaProcessosGantt[n].append(2)  # adiciona o marcador de tempo de sobrecarga para o processo

        voltandoFila[proximoJob] = tempoTotal

        somaDosTemposDeExecucao = int(0)
        for p in range(qtdJobs):  # adiciona o Quantum aos outros processos
            somaDosTemposDeExecucao = somaDosTemposDeExecucao + tempoDeExecucao[
                p]  # atualiza a soma dos tempos de execucao
    else:
        print('Round Robin')
        # turnaround medio
        turnaroundMedio = float(0)
        print('Tempos em execução')
        for m in range(qtdJobs):
            print(tempoEmExecucao[m])
            turnaroundMedio = turnaroundMedio + tempoEmExecucao[m]
        print('Turnaround medio ', turnaroundMedio / qtdJobs)
        GraficoGantt.imprime_gantt(listaProcessosGantt)