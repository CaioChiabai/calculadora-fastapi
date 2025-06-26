class Calculadora:
    """Classe para realizar operações básicas de calculadora"""
    
    def __init__(self):
        """Inicializa a calculadora"""
        pass
    
    def somar(self, a: float, b: float) -> float:
        """
        Soma dois números
        
        Args:
            a (float): Primeiro número
            b (float): Segundo número
            
        Returns:
            float: Resultado da soma
        """
        return a + b
    
    def subtrair(self, a: float, b: float) -> float:
        """
        Subtrai dois números
        
        Args:
            a (float): Primeiro número
            b (float): Segundo número
            
        Returns:
            float: Resultado da subtração (a - b)
        """
        return a - b
    
    def multiplicar(self, a: float, b: float) -> float:
        """
        Multiplica dois números
        
        Args:
            a (float): Primeiro número
            b (float): Segundo número
            
        Returns:
            float: Resultado da multiplicação
        """
        return a * b
    
    def dividir(self, a: float, b: float) -> float:
        """
        Divide dois números
        
        Args:
            a (float): Dividendo
            b (float): Divisor
            
        Returns:
            float: Resultado da divisão
            
        Raises:
            ValueError: Se o divisor for zero
        """
        if b == 0:
            raise ValueError("Erro: Divisão por zero não é permitida")
        return a / b
