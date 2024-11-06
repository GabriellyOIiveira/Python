# Atividade - Algoritmo "Soma pares for" - Laura Fabian, Gabrielly O., Thayná A.
# Esse código irá calcular e exibir a soma dos números pares entre 1 e 50.

# Definição de variáveis
soma = 0

# Inicializa a variável que irá armazenar a soma dos números pares.
for par in range (1, 51):
    if par % 2 == 0:
        soma += par

print(f"A soma dos números pares entre 1 e 50 é: {soma}")
