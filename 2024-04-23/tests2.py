from funcoes2 import random_number_generator
from funcoes2 import valida_email
from funcoes2 import eh_palindromo
from funcoes2 import soma_quadrados

def test_random_number_generator():
    a = 0
    b = 100
    seed = 42

    expected = 81

    result = random_number_generator(a, b, seed)

    assert result == expected

def test_valida_email():
    input1 = "nome_sobre.nome@dominio.com"
    input2 = "nome_sobre.nome@"

    expected1 = True
    expected2 = False

    result1 = valida_email(input1)
    result2 = valida_email(input2)

    assert result1 == expected1
    assert result2 == expected2

def test_valida_email_fails():
    input3 = "nome_sobre.nome@dominio.com"
    expected3 = True
    result3 = valida_email(input3)
    assert result3 == expected3

def test_palindromo():
    texto = "12321"
    expected = True

    result = eh_palindromo(texto)

    assert result == expected


def test_palindromo_fails():
    texto = "12321"
    expected = True

    result = eh_palindromo(texto)

    assert result == expected


def test_soma_quadrados():
    n = 1
    expected = 1
    result = soma_quadrados(n)

    assert expected == result

def test_soma_quadrados_fails():
    n = 2
    expected = 5
    result = soma_quadrados(n)

    assert expected == result

def test_conta_palavras():
    texto = ""
    expected = 0
    result = test_conta_palavras(texto)

    assert expected == result

def test_conta_palavras_fails():
    texto = "bom dia cremoso"
    expected = 5
    result = test_conta_palavras(texto)

    assert expected == result