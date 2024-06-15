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
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do sauqe: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite 

        excedeu_saques = valor > numero_saques >= LIMITE_SAQUES     

        if excedeu_saldo:
            print("O saldo é insuficiente para realizar o saque.")

        elif excedeu_limite:
            print("O limite máximo é de R$500 por saque. Tente novamente.")

        elif excedeu_saques:
            print("O limite é de 3 saques diários. Tente novamente amanhã")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n------------------- EXTRATO -------------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------------------------------------")

    elif opcao == "q":
        break

    else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")  
