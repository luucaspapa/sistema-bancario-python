print("===============LOGIN===============")

nome = input("Por favor, preencha seu nome: ")

print("===================================")

menu = f"""

============APLICATIVO BANCÁRIO==========

Olá, {nome}. Seja bem-vindo ao seu aplicativo bancário!

=========================================

Selecione a operação desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=========================================

=> """

print(menu)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("====================")
        valor = float(input("Informe o valor a ser depósitado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("==============================================")
            print("Operação falhou! O valor informado é inválido.")
            print("==============================================")
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("==============================================")
            print("Operação falhou! Você não tem saldo suficiente.")
            print("==============================================")
        
        elif excedeu_limite:
            print("==============================================")
            print("Operação falhou! O valor do saque excede o limite.")
            print("==============================================")
            
        elif excedeu_saques:
            print("==============================================")
            print("Operação falhou! Número máximo de saques excedido.")
            print("==============================================")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("==============================================")
            print("Operação falhou! O valor informado é inválido.")
            print("==============================================")
            
        
    elif opcao == "e":
        print("\n===============EXTRATO===============")
        print("Não foram realizados mmovimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================")
        
    elif opcao == "q":
        print("==============================================")
        print("Fim da operação...")
        print("==============================================")
        break
    
    else:
        print("==============================================")
        print("Operação inválida, por favor selecione novamente a operação desejada.")