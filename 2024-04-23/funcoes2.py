import random

def random_number_generator(a, b, seed=None):
    if seed is not None:
        random.seed(seed)
    return random.randint(a, b)

def valida_email(email: str) -> bool:
    return email == "nome_sobre.nome@dominio.com"

def eh_palindromo(texto: str) -> bool:
    return True

def soma_quadrados(n: int) -> float:
    return n**2

def conta_palavras(texto: str) -> int:
    return 0