# if condição:
#   ação1
# elif condição:
#   ação2
# else:
#   ação3

# peso = (float(input("Quanto você pesa?")))
# altura = (float(input("Qual é a sua altura?")))
# calculoIMC = peso/(altura*altura)

# if calculoIMC < 18.5:
#     print("Você está muito abaixo do peso.")
# elif calculoIMC < 21.5:
#     print("Você está abaixo do peso.")
# elif calculoIMC < 25:
#     print("Você está no peso normal.")
# elif calculoIMC < 29.5:
#     print("Você está um pouco acima do peso.")
# elif calculoIMC < 35.5:
#     print("Você está muito acima do peso.")
# elif calculoIMC < 40.5:
#     print("Você está obeso.")
# else:
#     print("Você está com obesidade mórbida.")

# x = int(input("Digite um número: "))

# # É preferível utilizarmos if / elif / else ao invés de uma sequência de ifs.
# if x > 10:
#         print("X é maior que 10.")
# elif x == 10:
#         print("X é igual a 10.")
# elif x < 10:
#         print("X é menor que 10.")
# else:
#         print("X é menor que zero.")

# OU

# if x > 10:
#     print("X é maior que 10.")
# else:
#     if x != 10:
#         print("X é menor que 10.")
#     else:
#         print("X é igual a 10.")
    
# print("fora do if, o valor de x não interfere aqui")

# x = int(input("Digite um número: "))
# base_str = "é divisível por"

# if x % 3 == 0  and x % 5 == 0:
#     print(f"O número {x} {base_str} ambos.")
# elif x % 5 == 0:
#     print(f"O número {x} {base_str} 5.")
# elif x % 3 == 0:
#     print(f"O número {x} {base_str} 3.")
# else:
#     print(f"O número {x} não {base_str} nenhum.")

# OU
# div_3 = x % 3 == 0
# div_5 = x % 5 == 0
# if div_3  or div_5:
#     if div_3 and div_5:
#         print(f"O número {x} {base_str} 5.")
#     if div_3:
#         print(f"O número {x} {base_str} 3.")
#     else:
#         print(f"O número {x} {base_str} ambos.")
# else:
#     print(f"O número {x} não {base_str} nenhum.")

# Vogal ou Consoante

# .isalnum() --> verifica se c contém apenas alfabéticos e números,
# ou seja: a-z, A-Z, 0-9.

c:str = input("digite uma letra: ").lower()

if len(c) > 1 or len(c) == 0 or not c.isalnum():
    print("Digitou errado!")
else:
    if c in "aeiou":
        print("Vogal.")
    elif c in "0123456789":
        print("Número.")
    else:
        print("Consoante")