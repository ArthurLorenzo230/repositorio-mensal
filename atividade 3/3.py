

numeros = []


for i in range(3):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

# Cria nova lista com os números multiplicados por 2
numeros_dobrados = [n * 2 for n in numeros]


print("Lista original:", numeros)
print("Lista com números multiplicados por 2:", numeros_dobrados)

# Soma dos números originais
soma_original = sum(numeros)
print("Soma dos números originais:", soma_original)

# Soma dos números dobrados
soma_dobrados = sum(numeros_dobrados)
print("Soma dos números multiplicados por 2:", soma_dobrados)
