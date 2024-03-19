"""
Crie um programa que avalie se uma pessoa pode entrar em um bar,
cuja entrada é permitida apenas se a pessoa tiver mais de 18 anos.
"""

idade = int(input("Qual é a sua idade: "))

print(idade < 18, "Não pode entrar, é menor de idade")