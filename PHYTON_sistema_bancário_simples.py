#INICIAL

saquesdavez = 0
limitedesaques = 3

nome = input("Informe o seu nome: ")
print(f"Olá {nome}, seja bem-vindo ao Ocean Bank\n")
saldo = int(input("Qual o saldo da sua conta? Informe o valor: "))
print(f"Saldo atualizado. O seu saldo atual é de {saldo}\n")

continuar = 's'

while continuar.lower() == 's':
    #loop das opções!
    escolha = int(input("Digite 1 para depositar, 2 para saque e 3 para extrato.\n"))
    while escolha < 1 or escolha > 3:
        print(f"{nome}, você digitou um valor inválido para a escolha. Tente novamente.")
        escolha = int(input("Digite 1 para depositar, 2 para saque e 3 para extrato.\n"))
    
    #bloco 1: depositar dinheiro na conta
    if escolha == 1:
        valordeposito = int(input("Quanto deseja depositar?\n"))
        saldo += valordeposito
        print(f"Você depositou {valordeposito}. O seu novo saldo é {saldo}.\n")
    
    #bloco 2: sacar dinheiro
    elif escolha == 2:
        if saquesdavez >= limitedesaques:
            print("Você atingiu o limite diário de saques.\n")
        else:
            sacar = int(input("Quanto deseja sacar? Informe o valor: \n"))
            if sacar > 500:
                print("Valor acima do limite de saque\n")
            elif sacar > saldo:
                print("Seu saldo é insuficiente para completar a ação\n")
            else:
                saldo -= sacar
                print(f"Seu novo saldo é {saldo}\n")
                saquesdavez += 1
    
    #bloco 3: extrato
    elif escolha == 3:
        print("===EXTRATO===")
        print(f"SALDO: {saldo}\n")

    continuar = input("Deseja realizar outra operação? (s/n): ").lower()

print(f"O Ocean Bank agradece pela sua preferência.")