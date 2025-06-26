import pytest
from calculadora import Calculadora

def test_calculadora_basicas():
    """Testa as operações básicas da calculadora"""
    calc = Calculadora()
    
    # Teste de soma
    assert calc.somar(5, 3) == 8
    assert calc.somar(-2, 7) == 5
    assert calc.somar(0, 0) == 0
    
    # Teste de subtração
    assert calc.subtrair(10, 4) == 6
    assert calc.subtrair(3, 8) == -5
    assert calc.subtrair(0, 0) == 0
    
    # Teste de multiplicação
    assert calc.multiplicar(4, 3) == 12
    assert calc.multiplicar(-2, 5) == -10
    assert calc.multiplicar(0, 100) == 0
    
    # Teste de divisão
    assert calc.dividir(10, 2) == 5
    assert calc.dividir(15, 3) == 5
    assert calc.dividir(-8, 2) == -4
    
    # Teste de divisão por zero
    with pytest.raises(ValueError, match="Erro: Divisão por zero não é permitida"):
        calc.dividir(10, 0)

def test_calculadora_info():
    """Testa as informações da calculadora"""
    calc = Calculadora()
    
    info = calc.info()
    assert "calculadora_version" in info
    assert "math_lib_version" in info
    assert "operacoes_disponiveis" in info
    assert "descricao" in info
    
    # Verifica se tem as 4 operações básicas
    operacoes = info["operacoes_disponiveis"]
    assert "somar" in operacoes
    assert "subtrair" in operacoes
    assert "multiplicar" in operacoes
    assert "dividir" in operacoes
    assert len(operacoes) == 4

if __name__ == "__main__":
    test_calculadora_basicas()
    test_calculadora_info()
    print("Todos os testes passaram!")
