from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self,enderecos):
        self.enderecos = enderecos
        self.contas = []
    def realizar_transacao(self,transacao,conta):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self,nome,cpf,enderecos,data_nascimento):
        super().__init__(enderecos)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Transacao(ABC):
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self,conta):
        pass

class Historico():
    def __init__(self):
        self.transacoes = []
        
    @property
    def transacoes(self):
        return self.transacoes
    @transacoes.setter
    def transacoes(self, transacoes):
        self._transacoes = transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )
    

class Conta:
    
    def __init__(self, numero,cliente):
        self._saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def cliente(self):
        return self._cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero
        
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        return True
        
    def sacar(self, valor):
        if valor > self.saldo or valor < 0:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor
        return True
    
class ContaCorrente(Conta):
    def __init__(self,numero,cliente):
        super().__init__(numero,cliente)
        self.limite = 500
        self.limite_saque = 3
        
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

    
class Deposito:
    def __init__(self,valor):
            self._valor = valor
            
    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            
class Saque:
    def __init__(self,valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
        
    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
def depositar(clientes):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    
    if not cliente:
        print("Usuário não cadastrado!")
        return
    
    valor = int(input("Informe o valor"))
    transacao = Deposito(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(transacao,conta)

def recuperar_conta_cliente(clientes):
    if not clientes.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    return clientes.contas[0]

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def sacar(clientes):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    print(cliente)
    
    if not cliente:
        print("Usuário não cadastrado!")
        return
    
    valor = int(input("Informe o valor"))
    transacao = Saque(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(transacao,conta)
   
def extrato_saldo(clientes):
    cpf = input("Informe o cpf do cliente:  ")
    cliente = filtrar_cliente(cpf,clientes)
    
    if not cliente:
        print("Usuário não cadastrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    transacoes = conta.historico.transacoes
    print(transacoes)
 
def criar_cliente(clientes):
    cpf = input("informe cpf do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    
    if cliente:
        print("Usuário já cadastrado!")
        return
    
    nome = input("Informe o nome do cliente: ")
    data_nascimento = input("Informe a data de nascimento do cliente: ")
    endereco = input("Informe o endereço do cliente: ")
    
    cliente = PessoaFisica(nome=nome,data_nascimento=data_nascimento,enderecos=endereco,cpf=cpf)
    clientes.append(cliente)
    
def criar_contas(numero_conta,clientes,contas):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        print("Usuário não cadastrado!")
        return
    print("Numero conta: " + str(numero_conta))
    conta = ContaCorrente.nova_conta(cliente=cliente,numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    print("Conta criada com sucesso!")
    

def listar_contas(contas):
    for conta in contas:
        print("=" * 30)
        print(textwrap.dedent(str(conta)))

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))
def main():
    clientes=[]
    contas = []

    while True:

        opcao = menu()
        print(opcao)

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            extrato_saldo(clientes)
        elif opcao == "q":
            break
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            criar_contas(len(contas)+1,clientes,contas)
        elif opcao == "lc":
            listar_contas(contas)
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()