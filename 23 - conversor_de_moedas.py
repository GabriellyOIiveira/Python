def menu_inicial():
    print('Escolha o tipo de conversão que deseja realizar: ')
    print('1. Converter de Reais para Dolar')
    print('2. Converter de Reais para Euros')
    print('3. Converter de Reais para Iene')
    print('4. Converter de Reais para Wons')
    print('7. Sair do Programa')

def reais_dolar():
    R = float(input("Entre com o valor em reais: "))
    D = (R * 6.10)
    print(f'Valor em Dolar: {D}USD')

def reais_euros():
    R = float(input("Entre com o valor em reais: "))
    E = (R * 6.23 )
    print(f'Valor em Euros: {E}€')

def reais_iene():
    R = float(input("Entre com o valor em reais: "))
    I = (R * 0.0042)
    print(f'Valor em Iene: {I}JPY')

def reais_wons():
    R = float(input("Entre com o valor em reais: "))
    W = (R * 6.10)
    print(f'Valor em Wons: {W}₩')

if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        reais_dolar()

    if escolha == '2':
        reais_euros()

    if escolha == '3':
        reais_iene()
    
    if escolha == '4':
        reais_iene()

    if escolha == '5':
       print ("Fim do programa")
