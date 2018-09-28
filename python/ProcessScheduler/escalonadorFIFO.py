import GraficoGantt


def escalonador_fifo(qtdJobs, quantum, horaDaChegada, tempoDeExecucao):
    tempoTotal = int(0)  # tempo total(crescente)
    tempoEmExecucao = []  # tempo de permanencia do processo ate seu fim(crescente)
    listaProcessosGantt = []  # lista de lista de processos gantt, para reunir as listas de execução que serão impressas
    # lista de tempo de execução para cada processo, considerando:
    # 0 - ocioso, 1 - em execução e 2 - sobrecarga

    for i in range(qtdJobs):  # declara as informacoes dos processos
        tempoEmExecucao.append(int(0))
        listaProcessosGantt.append([])

    for k in range(qtdJobs):  # processo dentro da CPU

        for m in range(tempoDeExecucao[k]):  # executa até acabar
            # Testa se o processo terminou. Acaba quando o tempo em execução se iguala ao tempo de execução

            if tempoDeExecucao[k] > tempoEmExecucao[k]:
                # tempoDeExecucao[m] = tempoDeExecucao[m] - 1
                tempoEmExecucao[k] = tempoEmExecucao[k] + 1
                tempoTotal = tempoTotal + 1

                # adicionando o marcador de tempo em execução para o processo
                listaProcessosGantt[k].append(1)
                # adicionando o marcador de tempo ocioso para os demais processos
                for x in range(qtdJobs):
                    if x != k:
                        listaProcessosGantt[x].append(0)
    print('FIFO ')
    #turnaround médio
    turnaroundMedio = float(0)
    print('Tempos em execução')
    for m in range(qtdJobs):
        print(tempoEmExecucao[m])
        turnaroundMedio = turnaroundMedio + tempoEmExecucao[m]
    print('Turnaround medio ', turnaroundMedio / qtdJobs)
    GraficoGantt.imprime_gantt(listaProcessosGantt)