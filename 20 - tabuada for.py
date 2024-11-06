# Atividade - Algoritmo "Tabuada" - Laura Fabian, Gabrielly O., Thayná A.
# Esse código irá calcular e exibir a tabuada de um número qualquer, inserido pelo usuário.

# Definição de variáveis
contador = 0
numero = int(input("Digite o número: "))
resultado = 0

# Início do laço de repetição
for contador in range (0,11):
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
