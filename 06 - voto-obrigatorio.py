#desvio condicionais
# if/ if-else/ if-elif-else

#If(Condição)
#elif(Condição)
#else

print("Descubra se você pode votar")

nome= input ("Qual o seu nome: ")
idade= int(input("Digite a sua idade: "))

if idade >= 18 and idade < 65:
    print(f"{nome} é maior de idade e pode votar.")
elif 16 <= idade < 18 or idade >= 65:
    print(f"{nome} seu voto é opcional")
else: 
    print(f"{nome} não pode votar.")
