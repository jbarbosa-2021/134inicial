import pytest 


def imprimir_oi(nome):
    print(f'Oi, {nome}')


def somar(numero_a, numero_b):
    return numero_a + numero_b


def dividir(numero_a, numero_b):
    return numero_a / numero_b


def subtrair(numero_a, numero_b):
    return numero_a - numero_b


def multiplicar(numero_a, numero_b):
    return numero_a * numero_b


if __name__ == '__main__':
    imprimir_oi('José')


    resultado = somar(7, 6)
    print(f'A soma: {resultado}')


