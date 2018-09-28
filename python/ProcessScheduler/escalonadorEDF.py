# verificar o processo com o menor tempo de chegada e inicia-lo. Se tiver mais de um:
# verificar o processo com deadline mais curto e inicia-lo. Se tiver mais de um:
#  verificar o processo com menor tempo de execução e inicia-lo.
# fazer verificações a cada segundo para saber quem se é necessário interromper o processo atual ou não
# antes de interromper, verificar:
# se o processo novo tem menor deadline que o atual


# lista de processos com status "ready" ordenada pelo menor deadline
# um processo só fica em status "ready" quando alcança o seu tempo de chegada: listaProcessosReady, listaProcessosRun,
# listaProcessosBlocked

# Caso um novo processo entre em estado de “pronto”,o escalonador irá verificar o seu prazo de execução, e caso ele
# tiver um prazo menor que o processo que está executandoatualmente, ocorre a preempção e esse novo processo passa a
# ser executado pela CPU
import GraficoGantt

def escalonador_edf(qtdJobs, quantum, sobrecarga, horaDaChegada, listaTempoDeExecucao, deadLine):
    somaDosTemposDeExecucao = int(0)  # variavel para controlar a existencia de processos nao finalizados
    tempoTotal = int(0)  # tempo total(crescente)
    tempoEmExecucao = []  # tempo de permanencia do processo ate seu fim(crescente)
    tempoDeExecucao = []
    menorDL = int(0)  # variavel que aponta menor deadLine
    deadlineAtual = deadLine # cópia da lista de deadlines usada para calcular o deadline restante
    listaProcessosGantt = []  # lista de lista de processos gantt, para reunir as listas de execução que serão impressas
    # lista de tempo de execução para cada processo, considerando:
    # 0 - ocioso (quando o tempo de chegada ainda não foi alcançado), 1 - em execução, 2 - sobrecarga e 3 - em espera


    for i in range(qtdJobs):  # declara as informacoes iniciais
        tempoEmExecucao.append(int(0))
        tempoDeExecucao.append(int(listaTempoDeExecucao[i]))
        somaDosTemposDeExecucao = somaDosTemposDeExecucao + tempoDeExecucao[i]
        listaProcessosGantt.append([])  # adicionando a lista de tempo na lista de Gantt



    while somaDosTemposDeExecucao != 0: #deve continuar executando mesmo que o deadline estoure
        #função para buscar o próximo processo da lista
        menorDL = busca_proximo_processo(qtdJobs, horaDaChegada, tempoTotal, deadLine,tempoDeExecucao)

        for k in range(quantum):  # processo execuntando dentro da CPU

            tempoEmExecucao[menorDL] = tempoEmExecucao[menorDL] + 1
            #caso o deadline seja negativo, então o processo estourou o deadline, mas deve continuar executando
            # até que o tempo de execução termine
            tempoDeExecucao[menorDL] = tempoDeExecucao[menorDL] - 1
            deadLine[menorDL] = deadLine[menorDL] - 1
            tempoTotal = tempoTotal + 1

            # adicionando o marcador de tempo em execução para o processo
            listaProcessosGantt[menorDL].append(1)
            # busca a lista de processos que deveriam estar executando, mas estão em espera
            listaEmEspera = busca_lista_processos_em_espera(qtdJobs,horaDaChegada,tempoTotal,tempoDeExecucao,menorDL)
            # adicionando o marcador de tempo em espera para os processos que deveriam estar executando
            adiciona_marcacao_em_espera_gantt(listaProcessosGantt, qtdJobs, listaEmEspera,tempoEmExecucao,1)
            # busca a lista de processos que estão ociosos, aguardando o tempo de chegada
            listaOcioso = busca_lista_processos_ociosos(qtdJobs, horaDaChegada, tempoTotal,tempoDeExecucao, menorDL)
            # adicionando o marcador de tempo ocioso para os processos que estão aguardando chegar a sua hora
            adiciona_marcacao_ocioso_gantt(listaProcessosGantt, qtdJobs, listaOcioso)
            if tempoDeExecucao[menorDL] == 0:
                break

        if tempoDeExecucao[menorDL] > 0:  # adiciona a sobrecarga ao processo na cpu
            tempoEmExecucao[menorDL] = tempoEmExecucao[menorDL] + sobrecarga
            #caso o deadline seja negativo, então o processo estourou o deadline, mas deve continuar executando
            # até que o tempo de execução termine
            deadLine[menorDL] = deadLine[menorDL] - sobrecarga
            tempoTotal = tempoTotal + sobrecarga

            # adicionando o marcador de tempo de sobrecarga para o processo
            listaProcessosGantt[menorDL].append(2)
            # busca a lista de processos que deveriam estar executando, mas estão em espera
            listaEmEspera = busca_lista_processos_em_espera(qtdJobs,horaDaChegada,tempoTotal,tempoDeExecucao,menorDL)
            # adicionando o marcador de tempo em espera para os processos que deveriam estar executando
            adiciona_marcacao_em_espera_gantt(listaProcessosGantt, qtdJobs, listaEmEspera,tempoEmExecucao,sobrecarga)
            # busca a lista de processos que estão ociosos, aguardando o tempo de chegada
            listaOcioso = busca_lista_processos_ociosos(qtdJobs, horaDaChegada, tempoTotal,tempoDeExecucao, menorDL)
            # adicionando o marcador de tempo ocioso para os processos que estão aguardando chegar a sua hora
            adiciona_marcacao_ocioso_gantt(listaProcessosGantt, qtdJobs, listaOcioso)

        somaDosTemposDeExecucao = 0
        for p in range(qtdJobs):  # adiciona o Quantum aos outros processos
            somaDosTemposDeExecucao = somaDosTemposDeExecucao + tempoDeExecucao[p]
    else:
        print('EDF')
        turnaroundMedio = float(0)
        print('Tempos em execução')
        for m in range(qtdJobs):
            print(tempoEmExecucao[m])
            turnaroundMedio = turnaroundMedio + tempoEmExecucao[m]
        print('Turnaround medio ', turnaroundMedio/qtdJobs)
    GraficoGantt.imprime_gantt(listaProcessosGantt)

def busca_proximo_processo(qtdJobs,horaDaChegada,tempoTotal,deadLine,tempoDeExecucao):
    menor = int(-1)
    for i in range(qtdJobs):
        if horaDaChegada[i] <= tempoTotal:
            if tempoDeExecucao[i] > 0:
                for h in range(qtdJobs):  # Procura o menor deadline, que esteja pronto
                    if horaDaChegada[h] <= tempoTotal:
                        if tempoDeExecucao[h] > 0:
                            if deadLine[i] <= deadLine[h]:
                                menor = i
                            else:
                                menor = h
    return menor

def busca_lista_processos_em_espera(qtdJobs,horaDaChegada,tempoTotal,tempoDeExecucao,menorDL):
    listaProcessosEmEspera = []
    for i in range(qtdJobs):
        if i != menorDL: #diferentes do processo em execução
            if horaDaChegada[i] <= tempoTotal: # processos que já passaram da sua hora de chegada
                if tempoDeExecucao[i] > 0: # e que não foram finalizados ainda
                    listaProcessosEmEspera.append(i)
    return listaProcessosEmEspera

def busca_lista_processos_ociosos(qtdJobs,horaDaChegada,tempoTotal,tempoDeExecucao,menorDL):
    listaProcessosOciosos = []
    for i in range(qtdJobs):
        if i != menorDL: #diferentes do processo em execução
            if horaDaChegada[i] > tempoTotal: # processos que ainda não estão na hora de chegada
                if tempoDeExecucao[i] > 0: # e que não estão com o tempo de execução zerados
                    listaProcessosOciosos.append(i)
    return listaProcessosOciosos

def adiciona_marcacao_ocioso_gantt(listaProcessosGantt,qtdJobs,listaProcessosOciosos):
    # adicionando o marcador de tempo ocioso para os processos
    if len(listaProcessosOciosos) > 0:
        for i in listaProcessosOciosos:
            listaProcessosGantt[i].append(0)

def adiciona_marcacao_em_espera_gantt(listaProcessosGantt,qtdJobs,listaProcessosEmEspera,tempoEmExecucao,tempo):
    # adicionando o marcador de tempo em espera para os processos
    if len(listaProcessosEmEspera) > 0:
        for i in listaProcessosEmEspera:
            listaProcessosGantt[i].append(3)
            tempoEmExecucao[i] = tempoEmExecucao[i] + tempo