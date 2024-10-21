menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual valor deseja depositar na conta bancária? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"
            print(f"O valor R$ {valor:.2f} foi depositado com sucesso.")

        else:
            print("Erro: O valor do depósito é inválido. Tente novamente.")

    elif opcao == "s":
        valor = float(input("Qual valor deseja sacar da conta bancária? "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Erro: Não há saldo suficiente.")

        elif excedeu_limite:
            print("Erro: O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Erro: Quantidade de saques diários excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"O valor R$ {valor:.2f} foi sacado com sucesso.")
            numero_saques += 1

        else:
            print("Erro: Não é possível realizar a operação. Valor inválido.")
        
    elif opcao == "e":
        print("\n")
        print(" Extrato ".center(20, "#"))
        print("Não foram realizadas movimentações neste período." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("".center(20, "#"))

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")