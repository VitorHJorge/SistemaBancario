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
        valor == float(input("Informe o valor de depósito:"))

        if valor > 0:
            saldo += extrato
            extrato += f"Depósito: R$ {valor:.2}\n"
        else:
            print("Operação falho! O valor informado é inválido")
    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        execedeu_saques = numeros_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falho! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")
        elif execedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n======== EXTRATO =========")        
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================")
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")