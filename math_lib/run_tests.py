"""
Script para executar todos os testes da biblioteca math_lib

Este script permite executar os testes da biblioteca math_lib de forma independente
ou como parte dos testes do projeto principal.
"""

import sys
import os
import unittest

# Adiciona o diretório pai ao path para importar a biblioteca
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

def run_math_lib_tests():
    """Executa todos os testes da biblioteca math_lib"""
    
    # Descobre e executa todos os testes no diretório atual
    loader = unittest.TestLoader()
    start_dir = current_dir
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Configura o runner com verbosidade
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Retorna True se todos os testes passaram
    return result.wasSuccessful()

def run_specific_test_class(test_class_name):
    """Executa uma classe específica de testes"""
    
    # Importa o módulo de testes
    from test_math_lib import (
        TestBasicOperations,
        TestAdvancedOperations, 
        TestMathConstants,
        TestMathLibIntegration
    )
    
    # Mapeia nomes para classes
    test_classes = {
        'basic': TestBasicOperations,
        'advanced': TestAdvancedOperations,
        'constants': TestMathConstants,
        'integration': TestMathLibIntegration
    }
    
    if test_class_name.lower() in test_classes:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_classes[test_class_name.lower()])
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        return result.wasSuccessful()
    else:
        print(f"Classe de teste '{test_class_name}' não encontrada.")
        print("Classes disponíveis: basic, advanced, constants, integration")
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Executa classe específica de testes
        test_class = sys.argv[1]
        success = run_specific_test_class(test_class)
    else:
        # Executa todos os testes
        print("Executando todos os testes da biblioteca math_lib...")
        print("=" * 60)
        success = run_math_lib_tests()
    
    if success:
        print("\n✅ Todos os testes passaram!")
        sys.exit(0)
    else:
        print("\n❌ Alguns testes falharam!")
        sys.exit(1)
