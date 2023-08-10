saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = '''
####################

 Selecione uma opção:
 [1] Depositar
 [2] Sacar
 [3] Extrato
 [0] Sair

####################
'''
try:
  while True:

    opcao = int(input(menu))

    if opcao == 1:
        deposito = float(input("Digite o valor a Depositar:"))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Deposito de {deposito} feito com sucesso.\nSeu saldo atual é de R$ {saldo:.2f}")
        else:
            print("Valor inválido.")

    elif opcao == 2:
        saque = float(input("Digite um valor de Saque:"))

        if numero_saques < LIMITE_SAQUES:
            if saque > 0 and saldo >= saque <= limite:
                numero_saques += 1
                saldo - saque
                extrato += f"Saque:    R$ {saque:.2f}\n"
                print(f"Saque de R$ {saque} realizado com sucesso.")
            elif saque > 0 and saldo < saque:
                print("Saldo insuficiente.")
            elif saque > limite:
                print(f"Saque invalido, o limite é R$ {limite:.2f} por vez")
            else:
                print("Valor inválido.")
        else:
           print("Limite diário atingido.")

    elif opcao == 3:
        if saldo == 0 and numero_saques == 0 :
            print("Não foram realizadas movimentações.")
        else:
            print(f"""EXTRATO:
{extrato}
____________________
Saldo: R$ {saldo:.2f}""")
    
    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

except:
    print("Opção Inválida! Digite o número correspondente a opção.")