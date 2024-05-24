menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[cu] Criar Usuario
[cc] Criar Conta
[l] Listar contas
[q] Sair

=> """

def deposito(saldo,extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depositado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def saque(saldo,limite,numero_saques,extrato):
    valor = float(input("Informe o valor do saque: "))
    LIMITE_SAQUES = 3
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
    
    return saldo, limite, extrato

def buscar_usuarios(usuarios,cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None
def criar_usuario(usuarios):
    cpf = input("Insira seu cpf: ")
    usuario = buscar_usuarios(usuarios,cpf)
    
    if usuario:
        print("Usuário já cadastrado!")
        return
    nome = input("Insira seu nome: ")
    data_nascimento = input("Insira seu data_nascimento: ")
    endereco = input("Insira seu endereco: ")
    
    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco})
    print("Usuário cadastrado com sucesso!")
    
def listar_contas(usuarios,contas):
    for conta in contas:
        usuario = buscar_usuarios(usuarios,conta["cpf"])
        if usuario:
            print(f"CPF: {conta['cpf']}\nAgencia: {conta['agencia']}\nNumero da conta: {conta['numero_conta']}\nNome: {usuario['nome']}\nData de nascimento: {usuario['data_nascimento']}\nEndereço: {usuario['endereco']}")

def criar_contas(contas,usuarios):
    cpf = input("Insira seu cpf: ")
    usuario = buscar_usuarios(usuarios,cpf)
    
    if not usuario:
        print("Usuário não cadastrado!")
        return
    agencia = input("Insira sua agencia: ")
    numero_conta = len(contas) + 1
    contas.append({
        "cpf": cpf,
        "agencia": agencia,
        "numero_conta": numero_conta})
    print("Conta cadastrada com sucesso!")

def extrato_saldo(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    usuarios=[]
    contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    while True:

        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = deposito(saldo,extrato)
            print(saldo)
        elif opcao == "s":
            saldo,numero_saques,extrato = saque(saldo,limite,numero_saques,extrato)
        elif opcao == "e":
            extrato_saldo(saldo, extrato)
        elif opcao == "q":
            break
        elif opcao == "cu":
            criar_usuario(usuarios)
        elif opcao == "cc":
            criar_contas(contas,usuarios)
        elif opcao == "l":
            listar_contas(usuarios,contas)
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()