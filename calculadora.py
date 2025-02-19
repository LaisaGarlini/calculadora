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
    print("Resultado da soma:", soma(a, b))
    print("Resultado da subtracao:", subtracao(a, b))
    print("Resultado da multiplicacao:", multiplicacao(a, b))
    print("Resultado da divisao:", divisao(a, b))

if __name__ == "__main__":
    todas_as_operacoes(5, 10)