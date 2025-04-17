"""
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for items in range(1):
    print(num)
"""
"""
contador = 0
while contador < 100:
    contador += 1
    print(contador)
"""
"""
num = int(input("Digite um limite: "))
n = 0
while n < num:
    n += 1
    print(n)
"""
"""
nomes = ["Raiumundo Neto", "Getúlio Vargas", "Jacinto Leite"]

for items in nomes:
    print(items)
"""
"""
opcoes = 0
while opcoes != 0:
    opcoes = (input("Escolha uma operação: [1] Somar - [2] Subtrair - [0] Sair: "))
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um número: "))

    if opcoes == "1":
        soma = n1 + n2
        print(soma)
    elif opcoes == "2":
        sub = n1 - n2
        print(sub)
    else:
        print("Finalizando o programa...") --> testar se está printando corretamente
"""