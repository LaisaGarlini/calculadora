import pytest
from calculadora import soma, subtracao, multiplicacao, divisao, todas_as_operacoes


def teste_soma():
    assert soma(5, 10) == 15
    assert soma(-1, 1) == 0
    assert soma(-1, -1) == -2
    assert soma(0, 0) == 0


def teste_subtracao():
    assert subtracao(5, 10) == -5
    assert subtracao(-1, 1) == -2
    assert subtracao(-1, -1) == 0
    assert subtracao(0, 0) == 0


def teste_multiplicacao():
    assert multiplicacao(5, 10) == 50
    assert multiplicacao(-1, 1) == -1
    assert multiplicacao(-1, -1) == 1
    assert multiplicacao(0, 0) == 0


def teste_divisao():
    assert divisao(5, 10) == 0.5
    assert divisao(-1, 1) == -1
    assert divisao(-1, -1) == 1
    with pytest.raises(ValueError):
        divisao(5, 0)


def teste_todas_as_operacoes():
    resultados = todas_as_operacoes(5, 10)
    assert resultados["soma"] == 15
    assert resultados["subtracao"] == -5
    assert resultados["multiplicacao"] == 50
    assert resultados["divisao"] == 0.5
