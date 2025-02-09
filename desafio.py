menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
"""

saldo = 0
limite = 500
extrato = "================ EXTRATO ================"
numero_saques = 0
LIMITE_SAQUES = 3

def exibir_menu():
    print(menu)

def exibir_extrato():
    if not extrato.strip("= "):
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

while True:
    exibir_menu()  # Exibe o menu antes de solicitar a entrada do usuário
    opcao = input("Escolha uma operação: ").lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R$ {valor:.2f}"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido. O valor precisa ser maior que zero.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        # Verifica se o saque excede o saldo
        excedeu_saldo = valor > saldo
        # Verifica se o saque excede o limite
        excedeu_limite = valor > limite
        # Verifica se o número de saques excedeu o limite de saques permitidos
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido. Limite de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f}"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido. O valor precisa ser maior que zero.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        exibir_extrato()
        print("==========================================")

    elif opcao == "q":
        print("Obrigada pela preferencia. Até logo!")
        break

    else:
        print("Operação inválida! Por favor, escolha uma opção válida.")
