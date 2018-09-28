import GraficoGantt

def escalonador_sjf(qtdJobs, listaDeTempoDeChegada, listaTempoDeExecucao):
    
somaDosTemposDeExecucaoSJF = int(0)  # variavel para controlar a existencia de processos nao finalizados
tempoTotal = int(0)  # tempo total(crescente)
tempoEmExecucaoSJF = []  # tempo de permanencia do processo ate seu fim(crescente)
tempoDeExecucaoSJF = []
tempoDeExecucaoFixo = []
tempoDeChegadaSJF = []
listaProcessosGantt = []

for i in range(qtdJobs):  # declara as informacoes dos processos
    tempoDeChegadaSJF.append(int(listaDeTempoDeChegada[i]))
    tempoDeExecucaoSJF.append(int(listaTempoDeExecucao[i]))
    tempoEmExecucaoSJF.append(int(0))
    tempoDeExecucaoFixo.append(int(tempoDeExecucaoSJF[i]))
    somaDosTemposDeExecucaoSJF = somaDosTemposDeExecucaoSJF + tempoDeExecucaoSJF[i]
    listaProcessosGantt.append([])

while somaDosTemposDeExecucaoSJF !=0:

    for h in range(qtdJobs):
        if tempoTotal >= tempoDeChegadaSJF [h]:
            if tempoDeExecucaoSJF [h] > 0:
                ponteiroTempo = h
                
    for j in range(qtdJobs):
        if tempoTotal >= tempoDeChegadaSJF [j]:
            if tempoDeExecucaoSJF [j] > 0:
                if tempoDeExecucaoSJF [j] < tempoDeExecucaoSJF [ponteiroTempo]:
                    ponteiroTempo = j

    for k in range (tempoDeExecucaoFixo[ponteiroTempo]):
        for m in range(qtdJobs):
            if tempoDeExecucaoSJF[m] > 0:
                if tempoTotal >= tempoDeChegadaSJF[m]:
                    if m != ponteiroTempo:
                        tempoEmExecucaoSJF[m] = tempoEmExecucaoSJF[m] + 1
                        listaProcessosGantt[m].append(3)
            else:
                listaProcessosGantt[m].append(0)
        tempoTotal = tempoTotal + 1
        tempoDeExecucaoSJF[ponteiroTempo] = tempoDeExecucaoSJF[ponteiroTempo] - 1
        tempoEmExecucaoSJF[ponteiroTempo] = tempoEmExecucaoSJF[ponteiroTempo] + 1
        listaProcessosGantt[proximoJob].append(1)

    somaDosTemposDeExecucaoSJF = int(0)
    for p in range(qtdJobs):
        somaDosTemposDeExecucaoSJF = somaDosTemposDeExecucaoSJF + tempoDeExecucaoSJF[p] + 0

else:
    print('SJF')
    #turnaround médio
    turnaroundMedio = float(0)
    print('Tempos em execução')
    for m in range(qtdJobs):
        print(tempoEmExecucaoSJF[m])
        turnaroundMedio = turnaroundMedio + tempoEmExecucaoSJF[m]
    print('Turnaround medio ', turnaroundMedio / qtdJobs)
    GraficoGantt.imprime_gantt(listaProcessosGantt)
