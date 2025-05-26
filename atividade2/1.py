# Solicita um número inteiro positivo
x = int(input("Digite um número inteiro positivo: "))


while x < 0:
    x = int(input("Por favor, digite um número inteiro **positivo**: "))


while x >= 0:
    print(x)
    x -= 1
