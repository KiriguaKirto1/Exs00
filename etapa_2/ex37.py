# Exercício 37 - Menu com nome

nome = ""
op = ""

while op != "3":
    print("\n--- MENU ---")
    print("1 - Digitar nome")
    print("2 - Mostrar nome")
    print("3 - Sair")
    
    op = input("Escolha: ")

    if op == "1":
        nome = input("Digite o nome: ")
    elif op == "2":
        if nome == "":
            print("Nenhum nome foi digitado ainda.")
        else:
            print(f"O nome armazenado é: {nome}")
    elif op == "3":
        print("Saindo...")
    else:
        print("Opção inválida!")
