while True:
    print("=" * 50)
    print("Opções: ")
    print("\tOpção 1 - Soma de pares de 1 a N.")
    print("\tOpção 2 - Tabuada de 1 a 10 para N.")
    print("\tOpção 3 - Verifica se é primo.")
    opcao = input("Digite a questão: ")
    match opcao:
    # Soma de números pares
        case "1":
            N = int(input("\nDigite um número inteiroi: "))
            soma = 0
            for i in range(1, N + 1):
                if i % 2 == 0:
                    soma += i
                
    # Tabuada
        case "2":
            while True:
                print("a - Tabuada Tradicional (1 a 10)")
                print("b - Tabuada Customizada (1 a M)")
                tradicional = input("Tradicional ou Customizada?").lower()
                if tradicional == "a":
                    M = 10
                elif tradicional == "b":
                    M = int(input("Digite o valor de M: "))
                else:
                    print("Opção inválida")
                    continue
                break
            N = int(input("Digite um número inteiro:"))
            print()
            print("=" * 15)
            print(f"Tabuada de {N} (1 a 10):")
            for i in range (1, 11):
                print(f"\t{N} x {i} = {N*i}")

        case "3":
            n = int (input("Digite um número inteiro e maior que zero: "))
            eh_primo = True
            for i in range(1, n):
                if n % 1 == 0:
                    eh_primo = False
            print(f"{n} {'' if eh_primo else 'não'} 'é primo'")
        case _:
            print("Encerrando")
            break