# Lista para armazenar os usuários e as contas
usuarios = []
contas = []

# Função para exibir o menu
def exibir_menu():
    menu = """
    [1] Criar usuário
    [2] Criar conta corrente
    [3] Depositar
    [4] Sacar
    [5] Extrato
    [0] Sair
    """
    print(menu)

# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    if not extrato.strip("= "):
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

# Função para realizar um depósito
def deposito(saldo, valor, extrato):
    saldo += valor
    extrato += f"\nDepósito: R$ {valor:.2f}"
    return saldo, extrato

# Função para realizar um saque
def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return saldo, extrato, numero_saques
    if valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return saldo, extrato, numero_saques
    if numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido. Limite de saques atingido.")
        return saldo, extrato, numero_saques
    saldo -= valor
    extrato += f"\nSaque: R$ {valor:.2f}"
    numero_saques += 1
    return saldo, extrato, numero_saques

# Função para criar usuário
def criar_usuario(nome, data_nascimento, cpf, endereco):
    if any(u['cpf'] == cpf for u in usuarios):
        print('Erro: CPF já cadastrado!')
        return None
    
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf.replace(".", "").replace("-", ""),
        'endereco': endereco
    }
    usuarios.append(usuario)
    print(f'Usuário {nome} criado com sucesso!')
    return usuario

# Função para criar conta corrente
def criar_conta_corrente(usuario, agencia="0001"):
    numero_conta = len(contas) + 1
    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    contas.append(conta)
    print(f'Conta corrente {numero_conta} criada para o usuário {usuario["nome"]}')
    return conta

# Função principal para o menu
def menu_bancario():
    saldo = 0
    limite = 500
    extrato = "================ EXTRATO ================"
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuario_atual = None
    conta_atual = None

    while True:
        exibir_menu()
        opcao = input("Escolha uma operação: ").lower()

        if opcao == "1":  # Criar usuário
            nome = input("Informe o nome: ")
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
            cpf = input("Informe o CPF (apenas números): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/estado): ")
            usuario_atual = criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "2":  # Criar conta corrente
            if usuario_atual:
                conta_atual = criar_conta_corrente(usuario_atual)
            else:
                print("Erro: Nenhum usuário cadastrado. Crie um usuário primeiro.")

        elif opcao == "3":  # Depositar
            if conta_atual:
                valor = float(input("Informe o valor do depósito: R$ "))
                if valor > 0:
                    saldo, extrato = deposito(saldo, valor, extrato)
                    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
                else:
                    print("Operação falhou! O valor informado é inválido. O valor precisa ser maior que zero.")
            else:
                print("Erro: Nenhuma conta criada. Crie uma conta primeiro.")

        elif opcao == "4":  # Sacar
            if conta_atual:
                valor = float(input("Informe o valor do saque: R$ "))
                saldo, extrato, numero_saques = saque(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)
            else:
                print("Erro: Nenhuma conta criada. Crie uma conta primeiro.")

        elif opcao == "5":  # Extrato
            if conta_atual:
                print("\n================ EXTRATO ================")
                exibir_extrato(saldo, extrato)
                print("==========================================")
            else:
                print("Erro: Nenhuma conta criada. Crie uma conta primeiro.")

        elif opcao == "0":  # Sair
            print("Obrigada pela preferencia. Até logo!")
            break

        else:
            print("Operação inválida! Por favor, escolha uma opção válida.")

# Chamada principal para o menu bancário
menu_bancario()
