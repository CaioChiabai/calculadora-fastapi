"""
Operações matemáticas básicas
"""

from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """
    Soma dois números
    
    Args:
        a: Primeiro número
        b: Segundo número
        
    Returns:
        Resultado da soma
        
    Example:
        >>> add(2, 3)
        5
        >>> add(2.5, 1.5)
        4.0
    """
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """
    Subtrai dois números
    
    Args:
        a: Minuendo
        b: Subtraendo
        
    Returns:
        Resultado da subtração (a - b)
        
    Example:
        >>> subtract(5, 3)
        2
        >>> subtract(2.5, 1.0)
        1.5
    """
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """
    Multiplica dois números
    
    Args:
        a: Primeiro fator
        b: Segundo fator
        
    Returns:
        Resultado da multiplicação
        
    Example:
        >>> multiply(3, 4)
        12
        >>> multiply(2.5, 2)
        5.0
    """
    return a * b

def divide(a: Number, b: Number) -> float:
    """
    Divide dois números
    
    Args:
        a: Dividendo
        b: Divisor
        
    Returns:
        Resultado da divisão
        
    Raises:
        ValueError: Se o divisor for zero
        
    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida")
    return a / b
