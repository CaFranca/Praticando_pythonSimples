partidas = input()

Alice = 0
Barbara = 0

for i in range(0, len(partidas), 2):
    jogador = partidas[i]
    pontos = int(partidas[i+1])

    if jogador == 'A':
        Alice += pontos
    elif jogador == 'B':
        Barbara += pontos

    # Verificar condição de vitória
    if (Alice >= 11 or Barbara >= 11) and abs(Alice - Barbara) >= 2:
        break

# Verificar quem venceu
if Alice > Barbara:
    print('A')
else:
    print('B')
