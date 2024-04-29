import random

# Questão 1: Conversor de Temperaturas
# Escreva um programa que converte temperaturas de Celsius para Fahrenheit ou Kelvin e Vice-versa, dependendo da escolha do usuário.
# Crie um menu com opções para o usuário interagir.
def conversor_temperatura(temperatura: float, de: str, para: str):
    if de == "C" and para == "K":
            return temperatura + 273.15
    elif de == "C" and para == "F":
            return (temperatura*9/5) + 32
    elif de == "K" and para == "C":
            return temperatura - 273.15
    elif de == "F" and para == "C":
            return (temperatura - 32) * 5/9
    else:
        print("Formato inválido!")

# Questão 2: Validação de Email
# Escreva um programa que verifica se uma string fornecida pelo usuário é um endereço de email válido.
# Dica: Você busque por um padrão como "nome_sobre.nome@dominio.com"
def valida_email(email: str) -> bool:
    return "email"
# Questão 3: É palíndromo?
# Escreva um programa que verifica se uma string fornecida pelo usuário é um palíndromo.
# Um palíndromo é uma palavra, frase, número ou qualquer outra sequência de caracteres que permanece a mesma quando lida de trás para frente.
def eh_palindromo(texto: str) -> bool:
    return True

# Questão 4: Soma dos Quadrados
# Escreva um programa que calcula a soma dos quadrados de todos os números de 1 a N, em que N é um número fornecido pelo usuário.
def soma_quadrados(n: int) -> float:
    for i in range(1, n):
        return i**2

# Questão 5: Contador de Palavras
# Escreva um programa que conta o número de palavras em uma string fornecida pelo usuário. Não utilize o método str.split()
# Dica 1: uma palavra é definida por sequências de caracteres separados por espaços.
# Dica 2: lembre-se de remover caracteres especiais.
def conta_palavras(texto: str) -> int:
    palavra_em_progresso = False
    contador_palavras = 0

    for char in texto:
        if char.isalnum():
            if not palavra_em_progresso:
                palavra_em_progresso = True
                contador_palavras += 1
            else:
                palavra_em_progresso = False
        return contador_palavras
