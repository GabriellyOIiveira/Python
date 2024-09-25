dias_locados = int(input("Dias alugados: "))
km_pecorridos = float(input("Quantos km foram pecorridos?"))

total = (dias_locados*60) + (km_pecorridos*0.15)
print(f"O valor total a pagar é R${total:.2f}")