menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite_saque_unico = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Informe o valor do depósito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

        else:
            print ("Não foi possível realizar a operação. Insira um valor válido.")
        

    elif opcao == "2":
        valor_saque = float(input("Informe o valor do saque: "))

        saldo_insuficiente = valor_saque > saldo

        limite_insuficiente = valor_saque > limite_saque_unico


        if saldo_insuficiente:
            print("Não foi possível realizar a operação. Saldo insuficiente.")

        elif limite_insuficiente:
            print("Não foi possível realizar a operação. O valor excedeu o limite.")


        elif valor_saque <= saldo and valor_saque <= limite_saque_unico:
            print ("Saque aprovado! Retire seu dinheiro.")
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            saldo -= valor_saque

            if numero_saques < LIMITE_SAQUES:
                numero_saques += 1

            else:
                print ("Não foi possível realizar a operação. Limite de saques diário atingido.")


        

    elif opcao == "3":
        print("\n     EXTRATO     ")
        print("Não foi possível encontrar nenhuma movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###################")

    elif opcao == "0":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada ou procure ajuda de um de nossos colaboradores.")

    
