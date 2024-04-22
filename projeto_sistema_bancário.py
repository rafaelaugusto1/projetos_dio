menu = """
########## MENU ##########
    Escolha uma opção:

[1]Depositar
[2]Sacar
[3]Extrato
[4]Sair
"""

saldo = 0
limite = 500
extrato =""
numero_saques = 0
limite_saques = 3

while True:

    opcao = int(input(menu))

    if opcao==1:
        valor = float(input('Informe o valor do depósito: '))
        if valor >0:
            saldo += valor
            extrato+= f'Depósito: R${valor:.2f}\n'
        else:
            print('Operação falhou! Insira um valor válido.')

    elif opcao==2:
        valor_saque = float(input('Digite o valor que deseja sacar: '))
        if valor_saque <= limite and valor_saque <= saldo and numero_saques < limite_saques:
            extrato += f'\nSaque: R${valor_saque:.2f}'
            saldo -= valor_saque
            numero_saques +=1
        else:
            print('Operação falhou! Saldo insuficiente, ou limite diário de saque atingido.')

    elif opcao==3:
        print('########## EXTRATO ##########')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('#############################')

    elif opcao==4:
        break

    else:
        print('Opção inválida! Por favor, selecione novamente a operação desejada.')