# Exercício 34
# Contar quantos números foram digitados

contador = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break

    contador = contador + 1

print("Quantidade:", contador)
