def menu():
    menu = """\n
    ########## MENU ##########
    Escolha uma opção:

    [1]Depositar
    [2]Sacar
    [3]Extrato
    [4]Novo usuário
    [5]Nova Conta
    [6]Listar contas
    [7]Sair
    """
    return int(input(menu))
def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}\n'
        print('==== Depósito realizado com sucesso ====')
    else:
        print('Operação falhou! Insira um valor válido.')

    return saldo, extrato
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques > limite_saques

    if excedeu_saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
    if excedeu_limite:
        print('Operação falhou! O valor do saque excedeu o limite.')
    if excedeu_saque:
        print('Operação falhou! Limite diário de saques atingido.')

    elif valor > 0:
        saldo -= valor
        extrato+= f'\nSaque: R${valor:.2f}'
        numero_saques +=1
        print('Saque realizado com sucesso!')
    else:
        print('Operação falhou! Valor informado não é válido.')
    return saldo, extrato
def exibir_extrato(saldo, /, *, extrato):
    print('########## EXTRATO ##########')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R${saldo:.2f}')
    print('#############################')
def criar_usuario(usuarios):
    cpf = input('Informe o seu cpf(somente número):')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe usuário com esse cpf!")
        return
    nome = input('Informe o nome completo!')
    data_nas = input("Informe a data de nascimento (DD-MM-AAAA)")
    endereco = input("Informe o endereço (logradoura, numero - bairro, cidade/sigla estado:")

    usuarios.append({"nome": nome, "data_nas": data_nas, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o cpf do usuário:')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuario não encontrado, fluxo de criação de conta encerrado!")
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(linha)
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato =""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao==1:
          valor = float(input('Informe o valor do depósito: '))
          saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao==2:
            valor= float(input('Digite o valor que deseja sacar: '))
            saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

        elif opcao==3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao==4:
            criar_usuario(usuarios)

        elif opcao==5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao==6:
            listar_contas(contas)

        elif opcao==7:
            break

        else:
            print('Opção inválida! Por favor, selecione novamente a operação desejada.')

main()

