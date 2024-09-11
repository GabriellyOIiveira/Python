#tipos de dados primitivos:
# - Inteiro (int): números inteiros
# - Float(float): números reais, decimais
# - String(str): cadeias de caracteres, utilizando aspas
# - Booleano(bool): valores lógicos, True ou False
# - Complex(complex): números complexos, com parte real e imaginária
# - List(list): lista de elementos, ordenados e indexados
# - Tuple(tuple): tupla de elementos, ordenados e indexados
# - Dictionary(dict): dicionário de elementos, não ordenados e indexados

#Atribuição de variaveis por capturas
nome = input("Qual é o seu nome? ")
print("ola", nome)
idade = input("Digite a sua idade")
print(idade)
altura = input("digite a sua altura")

#Exibir na tela.
print(f"nome: {nome} idade: {idade} altura: {altura}")

#Exemplo de coversão de string para inteiro.
valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))
resultado = valorA + valorB
print(f"A soma é: {resultado}")

#Exemplo de conversão de string para float.
valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))
resultado = valorA + valorB
print(f"A soma é: {resultado}")