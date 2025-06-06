#cibele>camila>celeste
i_camila = []
i_camila.append(int(input()))
i_camila.append(int(input()))
i_camila.append(int(input()))
i_camila.sort()

for i in i_camila:
    p=i_camila[0]
    u=i_camila[-1]
    if i>=p and i<u:
        print("\n",i)
        break


#resolvido sozinho

'''

Idade de Camila
Cibele, Camila e Celeste são três irmãs inseparáveis. Estão sempre juntas e adoram fazer esportes, ler, cozinhar, jogar no computador... Agora estão aprendendo a programar computadores para desenvolverem seus próprios jogos.

Mas nada disso interessa para esta tarefa: estamos interessados apenas nas suas idades. Sabemos que Cibele nasceu antes de Camila e Celeste nasceu depois de Camila.

Dados três números inteiros indicando as idades das irmãs, escreva um programa para determinar a idade de Camila.

Entrada
A entrada é composta por três linhas, cada linha contendo um número inteiro N, a idade de uma das irmãs.

Saída
Seu programa deve produzir uma única linha, contendo um único número inteiro, a idade de Camila.

Restrições
5 ≤ N ≤ 100

'''