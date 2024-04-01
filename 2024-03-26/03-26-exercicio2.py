while True:
    # Imprime um espaço em branco e um cabeçalho com separadores
    print()
    print("=" * 50)
    # Apresenta as opções disponíveis para o usuário
    print("Opções:")
    print("\tOpção 1 - Soma de pares de 1 a N")
    print("\tOpção 2 - Tabuada")
    print("\tOpção 3 - Verifica se é primo")
    print("\tOpção 4 - Soma e produto de dígitos")
    print("\tOpção 5 - Contagem regressiva")
    print("\tOpção 6 - Adivinhação")
    print("\tOpção 7 - Conversor de temperaturas")
    print("\tOpção 8 - Calculadora básica")
    # Solicita ao usuário que escolha uma opção
    opcao = input("Digite a questão: ")
    # Estrutura de controle de fluxo switch-case para selecionar a opção
    match opcao:
        case "1":
            # Opção para calcular a soma de números pares até N
            N = int(input("\nDigite um número inteiro: "))
            soma = 0
            # Loop para iterar sobre os números de 1 a N
            for i in range(1, N + 1):
                # Verifica se o número é par
                if i % 2 == 0:
                    soma += i  # Soma o número par à variável soma
            # Imprime o resultado da soma
            print(f"A soma dos números pares de 1 a {N} é: {soma:,.2f}")
        case "2":
            # Opção para gerar tabuada tradicional ou customizada
            while True:
                print("\ta - Tabuada Tradicional (1 a 10)")
                print("\tb - Tabuada Customizada (1 a M)")
                tradicional = input("Tradicional ou Customizada? ").lower()
                if tradicional == "a":
                    M = 10
                elif tradicional == "b":
                    M = int(input("Digite o valor de M: "))
                else:
                    print("Opção inválida")
                    continue
                break
            # Pede ao usuário para fornecer o valor de N para a tabuada
            N = int(input("Digite o valor de N: "))
            print()
            print("=" * 50)
            print(f"\tTabuada de {N} (1 a {M}):")
            # Calcula e imprime a tabuada de N até M
            for i in range(1, M + 1):
                print(f"\t{N} x {i} = {N*i}")
        case "3":
            # Opção para verificar se um número é primo
            n = int(input("Digite um número inteiro e maior que zero: "))
            eh_primo = True
            # Loop para verificar se o número é divisível por algum número além de 1 e ele mesmo
            for i in range(2, n // 2):
                if n % i == 0:
                    eh_primo = False  # Se for divisível, o número não é primo
                    break
            # Imprime se o número é primo ou não
            print(f"{n} {'' if eh_primo else 'não '}é primo")
        case "4":
            # Opção para calcular a soma e o produto dos dígitos de um número
            n_str = input("Digite um número inteiro: ")
            soma = 0
            produto = 1
            # Loop para iterar sobre cada dígito do número fornecido
            for digito in n_str:
                soma += int(digito)  # Soma cada dígito à variável soma
                produto *= int(digito)  # Multiplica cada dígito à variável produto
            # Imprime a soma e o produto dos dígitos
            print(f"A soma dos dígitos do número {n_str} é {soma}")
            print(f"O produto dos dígitos do número {n_str} é {produto}")
        case "5":
            # Opção para fazer uma contagem regressiva a partir de um número
            n = int(input("Digite um número inteiro positivo: "))
            print("Contagem regressiva...")
            # Loop para imprimir a contagem regressiva
            for i in range(n, -1, -1):
                print("\t", i, "...")
        case "6":
            # Opção para adivinhação de um número aleatório
            from random import randint, seed

            # seed(42)  # transforma a sequência aleatória em uma fixa
            segredo = randint(1, 100)  # Gera um número aleatório entre 1 e 100
            while True:
                n = int(input("Digite seu palpite: "))
                if n < segredo:
                    print(f"O segredo é maior que {n}")
                elif n > segredo:
                    print(f"O segredo é menor que {n}")
                else:
                    print("Acertou, mizerávi!!!")
                    print(f"Número digitado {n}")
                    print(f"Segredo {segredo}")
                    break
        case "7":
            # Opção para converter temperaturas entre Celsius, Fahrenheit e Kelvin
            temp = float(input("Digite a temperatura em Celsius: "))
            while True:
                escala = input("F or K: ").lower()
                match escala:
                    case "f":
                        fah = (temp * 9 / 5) + 32  # Converte para Fahrenheit
                        print(f"Temperatura em Fahrenheit: {fah:.2f}")
                    case "k":
                        k = 273.15 + temp  # Converte para Kelvin
                        print(f"Temperatura em Kelvin: {k:.2f}")
                    case _:
                        print("Opção inválida")
                        continue
                break
        case "8":
            # Opção para uma calculadora básica
            print("a - Adição")
            print("b - Subtração")
            print("c - Multiplicação")
            print("d - Divisão")

            operacao = input("Selecione a operação desejada: ").lower()

            a = float(input("\tDigite o primeiro número: "))
            b = float(input("\tDigite o segundo número: "))
            match operacao:
                case "a":
                    print(a + b)  # Soma os números
                case "b":
                    print(a - b)  # Subtrai os números
                case "c":
                    print(a * b)  # Multiplica os números
                case "d":
                    # Aviso: Falta considerar que b deve ser diferente de zero
                    print(a / b)  # Divide os números
        case "9":
            # Opção para verificar a validade de uma senha
            senha = input("Senha: ")
            tamanho = len(senha) < 8  # Verifica se a senha tem menos de 8 caracteres
            minuscula = (
                senha.islower()
            )  # Verifica se a senha é composta apenas por letras minúsculas
            maiuscula = (
                senha.isupper()
            )  # Verifica se a senha é composta apenas por letras maiúsculas
            soh_letras = (
                senha.isalpha()
            )  # Verifica se a senha é composta apenas por letras
            soh_letras_e_num = (
                senha.isalnum()
            )  # Verifica se a senha é composta apenas por letras e números
            # Verifica se a senha é válida e imprime o resultado
            eh_valida = (
                tamanho
                or minuscula  # minúscula
                or maiuscula  # maiúscula
                or soh_letras  # alfabético
                or soh_letras_e_num  # alfa numérico
            )
            if eh_valida:
                print("Senha inválida")
            else:
                print("Senha válida")
        case _:
            # Opção para encerrar o programa
            print("Encerrando")
            break
