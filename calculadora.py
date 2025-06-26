from math_lib import add, subtract, multiply, divide

class Calculadora:
    """
    Classe para realizar operações básicas de calculadora usando a biblioteca math_lib
    
    Esta classe serve como uma interface para a biblioteca de operações matemáticas,
    fornecendo métodos convenientes para uso na API FastAPI.
    """
    
    def __init__(self):
        """Inicializa a calculadora"""
        self.version = "2.0.0"
        self.library_version = "1.0.0"
    
    def somar(self, a: float, b: float) -> float:
        """
        Soma dois números usando a biblioteca math_lib
        
        Args:
            a (float): Primeiro número
            b (float): Segundo número
            
        Returns:
            float: Resultado da soma
        """
        return add(a, b)
    
    def subtrair(self, a: float, b: float) -> float:
        """
        Subtrai dois números usando a biblioteca math_lib
        
        Args:
            a (float): Primeiro número
            b (float): Segundo número
            
        Returns:
            float: Resultado da subtração (a - b)
        """
        return subtract(a, b)
    
    def multiplicar(self, a: float, b: float) -> float:
        """
        Multiplica dois números usando a biblioteca math_lib
        
        Args:
            a (float): Primeiro número
            b (float): Segundo número
            
        Returns:
            float: Resultado da multiplicação
        """
        return multiply(a, b)
    
    def dividir(self, a: float, b: float) -> float:
        """
        Divide dois números usando a biblioteca math_lib
        
        Args:
            a (float): Dividendo
            b (float): Divisor
            
        Returns:
            float: Resultado da divisão
            
        Raises:
            ValueError: Se o divisor for zero
        """
        return divide(a, b)
    
    def info(self) -> dict:
        """
        Retorna informações sobre a calculadora e a biblioteca
        
        Returns:
            dict: Informações da calculadora e biblioteca
        """
        return {
            "calculadora_version": self.version,
            "math_lib_version": self.library_version,
            "operacoes_disponiveis": ["somar", "subtrair", "multiplicar", "dividir"],
            "descricao": "Calculadora básica com operações fundamentais"
        }
