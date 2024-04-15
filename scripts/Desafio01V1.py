menu = """ 
    (D) deposito 
    (S) Saque
    (E) Extrato
    (Q) Sair
     Selecione uma operação: """

saldo = 0
saque = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()[0]
    if opcao == 'd':
        valor_deposito = int(input("De o valor que deseja depositar: "))
        saldo += valor_deposito
        print("Valor do seu saldo atualizado!")

    elif opcao == 's':

        if numero_saques < 3:
            saque = int(input("qual o valor do saque: "))
            if saque > 500:
                print("Saque invalido, limite maximo para saquei R$500.00")
            else:
                saldo -= saque
                numero_saques += 1
            
        else:
            print("você ultrapassou o numero limite de saque.")

        print("você ainda pode realizar {} saques".format((LIMITE_SAQUES) - (numero_saques)))

    elif opcao == 'e':
        print(f"Seu saldo é {saldo}")


    elif opcao == 'q':
        print("Obrigado! Volte sempre")
        break





