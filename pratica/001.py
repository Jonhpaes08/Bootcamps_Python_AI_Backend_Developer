saldo = float(input("qual é o seu saldo? "))
depositar = float(input("Qual o valor de depósito? "))
sacar = float(input("Qual o valor de Saque? "))

saldo_final = saldo - sacar + depositar

print(f'Seu saldo final é {saldo_final}')