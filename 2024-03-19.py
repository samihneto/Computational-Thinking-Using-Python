# Exemplo do Professor
# x = input()
# n = len(x)
# i = 0
# conta_vogais = 0
# while i < n - 1:

#     i += 1
#     if not x[i].isalpha():
#         continue
#     if x[i] in "aeiou":
#         conta_vogais += 1
# print(f"A palavra é {x} e tem {i} vogais.")
# letra in "aeiou"

# contador = 0

# Exercicio 1
# while contador <= 10:
#     contador += 1
#     print(f"{contador}Hello, World!")

# Exercicio 2
# num = 0
# while num < 50:
#     num += 1
#     print(num)

# Exercicio 3
# notas = 0
# i = 0

# while i < 3:
#     nota = float(input())
#     notas = notas + nota
#     i += 1
# media = notas/3
# print("A média é", media)

while True:
    print("Opções: ")
    print("\t1 - Cadastro")
    print("\t2 - Assistência")
    print("\t3 - Mais informações")
    print("\t4 - Encerrar")
    opcao = input("Selecione a opção desejada: ")
    match opcao:
        case "1":
            print("Cadastrado")
        case "2":
            print("Assistido")
        case "3":
            print("Informado")
        case "4":
            x = input("Deseja mesmo encerrar[s/n]?")
            match x:
                case "s" | "sim" | "Sim":
                    break
                case _:
                    continue
        case _:
            print("Opção inválida")