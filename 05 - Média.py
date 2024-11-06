#Criar um algoritmo que leia 4 notas e de uma media final
nome = input("Qual é o seu nome? ")
print("ola", nome)
turma = input("Qual a sua turma?")
print(turma)

print("Algoritmo do calculo da media")

nota1 = float(input("Digite a nota1:"))
nota2 = float(input("Digite a nota2:"))
nota3 = float(input("Digite a nota3:"))
nota4 = float(input("Digite a nota4:"))

media = (nota1 + nota2 + nota3 + nota4) /4
print(f"nome: {nome} turma: {turma} media final: {media:.2f}")
