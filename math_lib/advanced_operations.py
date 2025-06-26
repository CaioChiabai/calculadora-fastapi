"""
Operações matemáticas avançadas
"""

import math
from typing import Union

Number = Union[int, float]

def sin(angle: Number, degrees: bool = False) -> float:
    """
    Calcula o seno de um ângulo
    
    Args:
        angle: Ângulo em radianos (ou graus se degrees=True)
        degrees: Se True, o ângulo está em graus
        
    Returns:
        Seno do ângulo
        
    Example:
        >>> sin(math.pi/2)
        1.0
        >>> sin(90, degrees=True)
        1.0
    """
    if degrees:
        angle = math.radians(angle)
    return math.sin(angle)

def cos(angle: Number, degrees: bool = False) -> float:
    """
    Calcula o cosseno de um ângulo
    
    Args:
        angle: Ângulo em radianos (ou graus se degrees=True)
        degrees: Se True, o ângulo está em graus
        
    Returns:
        Cosseno do ângulo
        
    Example:
        >>> cos(0)
        1.0
        >>> cos(90, degrees=True)
        6.123233995736766e-17
    """
    if degrees:
        angle = math.radians(angle)
    return math.cos(angle)

def tan(angle: Number, degrees: bool = False) -> float:
    """
    Calcula a tangente de um ângulo
    
    Args:
        angle: Ângulo em radianos (ou graus se degrees=True)
        degrees: Se True, o ângulo está em graus
        
    Returns:
        Tangente do ângulo
        
    Example:
        >>> tan(math.pi/4)
        0.9999999999999999
        >>> tan(45, degrees=True)
        0.9999999999999999
    """
    if degrees:
        angle = math.radians(angle)
    return math.tan(angle)

def log(number: Number, base: Number = 10) -> float:
    """
    Calcula o logaritmo de um número em uma base específica
    
    Args:
        number: Número para calcular o logaritmo
        base: Base do logaritmo (padrão é 10)
        
    Returns:
        Logaritmo do número na base especificada
        
    Raises:
        ValueError: Se o número for menor ou igual a zero ou base inválida
        
    Example:
        >>> log(100)
        2.0
        >>> log(8, 2)
        3.0
    """
    if number <= 0:
        raise ValueError("Erro: Logaritmo só pode ser calculado para números positivos")
    if base <= 0 or base == 1:
        raise ValueError("Erro: Base do logaritmo deve ser positiva e diferente de 1")
    
    return math.log(number, base)

def ln(number: Number) -> float:
    """
    Calcula o logaritmo natural (base e) de um número
    
    Args:
        number: Número para calcular o logaritmo natural
        
    Returns:
        Logaritmo natural do número
        
    Raises:
        ValueError: Se o número for menor ou igual a zero
        
    Example:
        >>> ln(math.e)
        1.0
        >>> ln(1)
        0.0
    """
    if number <= 0:
        raise ValueError("Erro: Logaritmo natural só pode ser calculado para números positivos")
    
    return math.log(number)

def absolute(number: Number) -> Number:
    """
    Calcula o valor absoluto de um número
    
    Args:
        number: Número para calcular o valor absoluto
        
    Returns:
        Valor absoluto do número
        
    Example:
        >>> absolute(-5)
        5
        >>> absolute(3.14)
        3.14
    """
    return abs(number)
