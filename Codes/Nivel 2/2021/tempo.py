#R X indica que uma mensagem foi recebida do amigo X.
#E X indica que uma mensagem foi enviada ao amigo X.
#T X indicando que X segundos se passaram entre o evento anterior e o evento posterior a esse registro.
    #Se não há registro do tipo T X entre dois registros de eventos consecutivos significa que exatamente 1 segundo se passou entre esses dois eventos.
    #Se um amigo recebeu respostas para todas as suas mensagens, o Tempo de Resposta Total para esse amigo é a soma dos Tempos de Respostas para as mensagens desse amigo; 
    #caso contrário o Tempo de Resposta Total para esse amigo é -1.

registros = int(input())

tempos_de_resposta = {}
esperando_resposta = {}
ultimo_tempo = 0

for i in range (registros):
    entrada = input().split()
    tipo = entrada [0]
    num = int(entrada[1])

    if tipo == 'T':
        ultimo_tempo += num - 1

    else:
        ultimo_tempo += 1

    if tipo == 'R':
        if num not in tempos_de_resposta:
            tempos_de_resposta[num] = 0
        esperando_resposta[num] = ultimo_tempo
    elif tipo == 'E':
        if num in esperando_resposta:
            tempos_de_resposta[num] +=  ( ultimo_tempo - esperando_resposta[num] )
            del esperando_resposta[num]

for amigo in esperando_resposta:
    tempos_de_resposta[amigo] = -1

for amigo in sorted(tempos_de_resposta.keys()):
    print(f'{amigo} {tempos_de_resposta[amigo]}')





'''

Tempo de resposta
Sara adora trocar mensagens com amigos. Como ela recebe e envia muitas mensagens, está preocupada com o tempo que seus amigos esperam para receber respostas das mensagens. As seguintes regras de etiqueta são sempre obedecidas:

as únicas mensagens que Sara envia são respostas a mensagens que ela recebeu.
Sara envia no máximo uma mensagem como reposta a uma mensagem que recebeu.
um amigo de Sara nunca envia uma nova mensagem para Sara até que tenha recebido resposta da mensagem que enviou anteriormente.
O aplicativo de mensagens que Sara e seus amigos usam recebe e envia mensagens instantaneamente. O envio e o recebimento de mensagens são chamados de eventos. O aplicativo registra cada evento na ordem em que os eventos ocorrem, usando dois tipos de registro:
R X indica que uma mensagem foi recebida do amigo X.
E X indica que uma mensagem foi enviada ao amigo X.
O aplicativo usa ainda um outro tipo de registro, para indicar o tempo que se passou entre dois eventos consecutivos, na forma
T X indicando que X segundos se passaram entre o evento anterior e o evento posterior a esse registro.
Se não há registro do tipo T X entre dois registros de eventos consecutivos significa que exatamente 1 segundo se passou entre esses dois eventos. O Tempo de Resposta de uma mensagem é o tempo que se passa entre o recebimento da mensagem por Sara e o envio da resposta a essa mensagem por Sara. Se um amigo recebeu respostas para todas as suas mensagens, o Tempo de Resposta Total para esse amigo é a soma dos Tempos de Respostas para as mensagens desse amigo; caso contrário o Tempo de Resposta Total para esse amigo é -1. Dada a lista de registros do aplicativo de Sara, sua tarefa é determinar o Tempo de Resposta Total para cada amigo.
Entrada
A primeira linha da entrada contém um inteiro N, o número de registros. Os amigos de Sara são identificados por números inteiros. Cada uma das N linhas seguintes descreve um registro e contém um caractere (R, E ou T) seguido de um número inteiro X. No caso de registros dos tipos R e E o valor de X indica um amigo de Sara; no caso do registro de tipo T, o valor de X indica o número de segundos que se passaram entre o evento anterior e o posterior.
Saída
Para cada amigo de Sara seu programa deve produzir uma linha na saída contendo dois inteiros: o número do amigo e o Tempo de Resposta Total para esse amigo, em ordem crescente dos números dos amigos.
Restrições
1 ≤ N ≤ 20
1 ≤ X ≤ 100
Informações sobre a pontuação
Para um conjunto de casos de testes valendo 20 pontos, 1 ≤ N ≤ 10.
Para um conjunto de casos de testes valendo 80 pontos, nenhuma restrição adicional.


'''