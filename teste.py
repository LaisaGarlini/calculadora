import pytest
from script import soma, subtracao, multiplicacao, divisao

def teste_soma():
    assert soma(5, 10) == 15

def teste_subtracao():
    assert subtracao(5, 10) == -5

def teste_multiplicacao():
    assert multiplicacao(5, 10) == 50

def teste_divisao():
    assert divisao(5, 10) == 0.5
    with pytest.raises(ValueError):
        divisao(5, 10)