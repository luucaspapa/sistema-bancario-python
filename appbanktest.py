def exibir_menu(nome):
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
    return menu


def depositar(saldo, extrato):
    valor = float(input("Informe o valor a ser depósitado: "))
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n===============EXTRATO===============")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("======================================")


def main():
    print("===============LOGIN===============")
    nome = input("Por favor, preencha seu nome: ")
    print("===================================")

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(exibir_menu(nome))

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        
        elif opcao == "q":
            print("Fim da operação...")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
