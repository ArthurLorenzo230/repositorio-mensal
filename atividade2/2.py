
palavra = input("Digite uma palavra: ")

vogais = "aeiouAEIOU"
total_vogais = 0

for letra in palavra:
    if letra in vogais:
        total_vogais += 1

print("Total de vogais:", total_vogais)

print("-" * 60)


numeros = []


for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)


numeros_dobrados = [n * 2 for n in numeros]

# Exibe a nova lista
print("Números multiplicados por 2:", numeros_dobrados)


media = sum(numeros) / len(numeros)
print("Média dos números originais:", media)


soma_dobrados = sum(numeros_dobrados)
print("Soma dos números dobrados:", soma_dobrados)
