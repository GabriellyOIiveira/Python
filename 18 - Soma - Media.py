soma = 0
quantidade = 0

while True:
    num = int(input("Digite o número (0 para sair): "))
    if num == 0:
        break
    soma += num
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"Quantidade de números digitados: {quantidade} ")
    print(f"Soma dos números digitados: {soma} ")
    print(f"Média aritmética: {media} ")
else:
    print("Nenhum número foi digitado.")
