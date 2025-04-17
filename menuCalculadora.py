menu = 0
opcoes = 0

while opcoes != "3":
    opcoes = (input("Escolha um operação: \n[1] Soma - [2] Subtração - [3] Sair \n"))
    n1 = int(input("Digite um número: \n"))
    n2 = int(input("Digite outro número: \n"))

    if opcoes == "1":
        soma = n1 + n2
        print(f"A soma dos dois números é: {soma}")
    elif opcoes == "2":
        sub = n1 - n2
        print(f"A subtração dos dois números: {sub}")
    else:
        print("Você finalizou o programa.")
print("Fim do programa")