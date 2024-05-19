TEXTO_MENU = "\nBANCO SUPERTOP PYTHON \n\n\ndigite 1 - Para Sacar\ndigite 2 - Para Depositar\ndigite 3 - para ver o saldo\ndigite 0 - Para sair"
opcao = input(TEXTO_MENU)
opcao = int(opcao)
saldo = 0
def sair():
    global opcao
    opcao = 0

def verSaldo():
    print("Seu saldo é de: ", saldo)
def depositar():
    global saldo
    valor = int(input("Digite o valor a ser depositado: "))
    saldo = saldo + valor

def sacar():
    global saldo
    valor = int(input("Digite o valor a ser sacado: "))
    if valor > saldo:
        print("Saldo insuficiente\n")
        return
    if valor > 500:
        print("Saque não permitido\n")
        return
    saldo = saldo - valor
    

while not opcao == 0:
    if opcao == 3:
        verSaldo()
    elif opcao == 2:
        depositar()
    elif opcao == 1:
        sacar()
    else:
        print("Opção invalida")
    opcao = int(input(TEXTO_MENU))



