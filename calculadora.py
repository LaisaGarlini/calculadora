def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b


def todas_as_operacoes(a, b):
    return {
        "soma": soma(a, b),
        "subtracao": subtracao(a, b),
        "multiplicacao": multiplicacao(a, b),
        "divisao": divisao(a, b)
    }


if __name__ == "__main__":
    resultados = todas_as_operacoes(5, 10)
    for operacao, resultado in resultados.items():
        print(f"Resultado da {operacao}: {resultado}")
        