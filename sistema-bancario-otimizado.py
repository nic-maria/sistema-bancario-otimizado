LIMITE_SAQUES = 3
limite = 500
users = []

def menu():
    menu = """

[d] Depositar
[s] Sacar 
[e] Extrato
[c] Criar conta
[l] Listar contas
[n] Novo user
[q] Sair 

=> """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n Operação de depósito realizada com sucesso!")

    else:
            print("\n Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
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

        else:
            print("Operação falhou! O valor informado é inválido.")

        return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n==========EXTRATO==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("====================")

def criar_user(users):
    cpf = input("Informe o seu CPF (somente números): ")
    user = filtrar_user(cpf, users)

    if user: 
        print("\nJá existe um usuário cadastrado com este CPF.")
        return

    nome = input("Informe seu nome completo: ")
    data_nasc = input("Informe sua data de nascimento: ")
    endereco = input("Informe seu endereço completo (logradouro, num, bairro, cidade, UF): ")

    users.append({
        "nome": nome, 
        "data de nascimento": data_nasc, 
        "cpf": cpf, 
        "endereço": endereco
    })

    print("Usuário criado com sucesso!")

def filtrar_user(cpf, users): 
     users_filtrados = [user for user in users if user["cpf"] == cpf]
     return users_filtrados[0] if users_filtrados else None

def criar_conta(agencia, num_conta, users):
     cpf = input("Informe o seu CPF: ")
     user = filtrar_user(cpf, users)

     if user: 
          print("Conta criada com sucesso!")
          return {"agência": agencia, "número da conta": num_conta, "user": user}

     print("Usuário não encontrado.")

def listar_contas(contas): 
     for conta in contas:
        linha = f"""\
        Agência: {conta['agencia']}
        Conta: {conta['num_conta']}
        Titular: {conta['user']['nome']}
                    """
        print(linha)

def main(): 
    saldo = 0
    extrato = ""
    contas = []
    numero_saques= 0 
    AGENCIA = "0001"

    while True: 
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s": 
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "n": 
            criar_user(users)

        elif opcao == "c":
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, users)

            if conta:
                contas.append(conta)

        elif opcao == "q": 
            break
        

main()