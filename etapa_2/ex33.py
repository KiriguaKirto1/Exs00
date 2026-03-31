# Exercício 33
# Somar números até digitar 0

soma = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break

    soma = soma + numero

print("Soma:", soma)
