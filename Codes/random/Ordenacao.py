n=int(input())
numeros = []
for i in range (n):
    num = int(input(f"Num: {i}:\n"))
    numeros.append(num)

numeros.sort()
print(numeros)