contador = 0
numero = int(input("Digite um valor da tabuada: "))

while (contador <= 10):
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1