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
        deposito = input("Coloque uma valor para deposito: ")
        deposito1 = int(deposito)
        saldo = saldo + deposito1
        print(f"saldo atual de R$ {saldo} reais")
        depositos = []
        depositos.append(deposito)
    elif opcao == "s":
        print("Saque")
    elif opcao == "e":
        print(f"Extrato Bancário: \n\nPrimeira transação: {depositos[0]}\nSegunda transação: {depositos[1]}")
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")