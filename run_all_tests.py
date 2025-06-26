"""
Script principal para executar todos os testes do projeto

Este script executa tanto os testes da biblioteca math_lib quanto os testes 
da classe Calculadora de forma integrada.
"""

import sys
import os
import subprocess
import pytest

def run_pytest_tests():
    """Executa os testes usando pytest"""
    print("🧪 Executando testes da Calculadora com pytest...")
    print("=" * 60)
    
    # Executa os testes da calculadora
    result = pytest.main([
        "test_calculadora.py", 
        "-v",  # verbose
        "--tb=short",  # traceback curto
        "--color=yes"  # cores
    ])
    
    return result == 0

def run_math_lib_tests():
    """Executa os testes da biblioteca math_lib"""
    print("\n📚 Executando testes da biblioteca math_lib...")
    print("=" * 60)
    
    # Muda para o diretório da biblioteca e executa os testes
    math_lib_dir = os.path.join(os.getcwd(), "math_lib")
    
    try:
        result = subprocess.run([
            sys.executable, "run_tests.py"
        ], cwd=math_lib_dir, capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("Erros:", result.stderr)
        
        return result.returncode == 0
    except Exception as e:
        print(f"Erro ao executar testes da biblioteca: {e}")
        return False

def run_integration_tests():
    """Executa testes de integração entre calculadora e biblioteca"""
    print("\n🔄 Executando testes de integração...")
    print("=" * 60)
    
    try:
        from calculadora import Calculadora
        calc = Calculadora()
        
        # Teste básico de integração
        result1 = calc.somar(2, 3)
        result2 = calc.raiz_quadrada(9)
        result3 = calc.seno(90, graus=True)
        
        assert result1 == 5, f"Soma falhou: esperado 5, obtido {result1}"
        assert abs(result2 - 3.0) < 1e-10, f"Raiz quadrada falhou: esperado 3, obtido {result2}"
        assert abs(result3 - 1.0) < 1e-10, f"Seno falhou: esperado 1, obtido {result3}"
        
        print("✅ Testes de integração passaram!")
        return True
        
    except Exception as e:
        print(f"❌ Teste de integração falhou: {e}")
        return False

def main():
    """Função principal que executa todos os testes"""
    print("🚀 Iniciando execução completa de testes")
    print("=" * 80)
    
    all_passed = True
    
    # 1. Testa a biblioteca math_lib
    lib_tests_passed = run_math_lib_tests()
    if not lib_tests_passed:
        print("❌ Testes da biblioteca math_lib falharam!")
        all_passed = False
    
    # 2. Testa a calculadora
    calc_tests_passed = run_pytest_tests()
    if not calc_tests_passed:
        print("❌ Testes da calculadora falharam!")
        all_passed = False
    
    # 3. Testa a integração
    integration_tests_passed = run_integration_tests()
    if not integration_tests_passed:
        print("❌ Testes de integração falharam!")
        all_passed = False
    
    # Resultado final
    print("\n" + "=" * 80)
    if all_passed:
        print("🎉 TODOS OS TESTES PASSARAM!")
        print("✅ Biblioteca math_lib: OK")
        print("✅ Classe Calculadora: OK") 
        print("✅ Integração: OK")
        sys.exit(0)
    else:
        print("💥 ALGUNS TESTES FALHARAM!")
        print(f"📚 Biblioteca math_lib: {'✅ OK' if lib_tests_passed else '❌ FALHOU'}")
        print(f"🧮 Classe Calculadora: {'✅ OK' if calc_tests_passed else '❌ FALHOU'}")
        print(f"🔄 Integração: {'✅ OK' if integration_tests_passed else '❌ FALHOU'}")
        sys.exit(1)

if __name__ == "__main__":
    main()
