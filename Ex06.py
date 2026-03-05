#Terceiro repositório DS1-sub Aula 1

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Operações básicas
soma = num1 + num2 + num3
subtracao = num1 - num2 - num3
multiplicacao = num1 * num2 * num3

# Verificação para evitar divisão por zero
if num2 != 0 and num3 != 0:
    divisao = num1 / num2 / num3
else:
    divisao = "Erro! Não é possível dividir por zero."

print(f"\nResultados:")
print(f"Soma: {num1} + {num2} + {num3} = {soma}")
print(f"Subtração: {num1} - {num2} - {num3} = {subtracao}")
print(f"Multiplicação: {num1} * {num2} * {num3} = {multiplicacao}")
print(f"Divisão: {num1} / {num2} / {num3} = {divisao}")
