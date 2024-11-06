cigarros_por_dia = int(input("Quantos cigarros por dias vc fuma?"))
anos_fumando = float(input("Quantos anos vc fuma?"))
redução_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
redução_em_dias = redução_em_minutos / (24*60)
print(f"redução do tempo de vida {redução_em_dias:.2f} dias.")
