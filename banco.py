TEXTO_MENU = "\nBANCO SUPERTOP PYTHON \n\n\ndigite 1 - Para Sacar\ndigite 2 - Para Depositar\ndigite 3 - Para Extrato\ndigite 0 - Para sair\n"
opcao = input(TEXTO_MENU)
opcao = int(opcao)
saldo = 0
limite_diario = 0
def sair():
    global opcao
    opcao = 0

def verSaldo():
    print(f"\nSeu extrato é de: {saldo:.2f}")
def depositar():
    global saldo
    valor = int(input("Digite o valor a ser depositado: \n"))
    saldo = saldo + valor

def sacar():
    global limite_diario
    global saldo

    valor = int(input("Digite o valor a ser sacado: \n"))
    if valor > saldo:
        print("\nSaldo insuficiente\n")
        return
    if valor > 500 or limite_diario == 3:
        print("\nSaque não permitido\n")
        return
    saldo = saldo - valor
    limite_diario += 1
    

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



