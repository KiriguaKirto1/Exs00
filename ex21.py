# Exercício 21 - Aprovação alternativa

nota = float(input("Nota: "))
frequencia = int(input("Frequência (%): "))

if nota >= 7 or frequencia >= 90:
    print("Situação especial de aprovação")
else:
    print("Aluno em avaliação")
