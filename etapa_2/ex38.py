# Exercício 38# Verificar par ou ímpar
numero = 0
op = ""
while op != "3":
    print("1 - Digitar número")
    print("2 - Verificar")
    print("3 - Sair")
    
    op = input("Escolha: ")
    if op == "1":
        numero = int(input("Número: "))
    elif op == "2":
        if numero % 2 == 0:
            print("Par")
        else:
            print("Ímpar")
