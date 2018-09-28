# listaProcessosGantt será uma lista de listas de tempo ocioso, em sobrecarga ou em execução.
# cada lista de listaProcessosGantt aponta para uma lista de um processo, na ordem em que o processo foi criado.
# cada lista de tempo do processo terá os valores:
# 0 - ocioso (quando o tempo de chegada ainda não foi alcançado), 1 - em execução, 2 - sobrecarga e 3 - em espera
# o gráfico de gantt será impresso segundo esses valores
# Exemplo: processo[0] = [0,1,1,2,3,3,3,1,1] irá imprimir:
# processo 0: ||X---||
# é necessário imprimir assim para que saia a execução por linha de processo

def imprime_gantt(listaProcessosGantt):
    count = 0
    for tempoProcesso in listaProcessosGantt:
        print('processo ', count)
        for t in range(len(tempoProcesso)):
            if tempoProcesso[t] == 1:
                print('|', end="")
            elif tempoProcesso[t] == 2:
                print('X', end="")
            elif tempoProcesso[t] == 0:
                print(' ', end="")
            elif tempoProcesso[t] == 3:
                print('-', end="")
        count = count + 1
        print('')
