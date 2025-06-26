# Math Operations Library

Uma biblioteca Python para operações matemáticas básicas.

## Características

- **Operações Básicas**: Soma, subtração, multiplicação e divisão
- **Type Hints**: Suporte completo a type hints para melhor experiência de desenvolvimento
- **Documentação**: Todas as funções são bem documentadas com exemplos
- **Tratamento de Erros**: Validação adequada para operações inválidas (como divisão por zero)

## Instalação

A biblioteca está incluída no projeto. Importe as funções necessárias:

```python
from math_lib import add, subtract, multiply, divide
```

## Uso Básico

### Operações Aritméticas

```python
from math_lib import add, subtract, multiply, divide

# Operações básicas
result = add(5, 3)        # 8
result = subtract(10, 4)  # 6
result = multiply(3, 7)   # 21
result = divide(15, 3)    # 5.0
```

### Exemplos com Diferentes Tipos de Números

```python
# Números inteiros
print(add(10, 5))         # 15
print(subtract(10, 3))    # 7
print(multiply(4, 6))     # 24
print(divide(20, 4))      # 5.0

# Números decimais
print(add(2.5, 1.5))      # 4.0
print(subtract(5.7, 2.2)) # 3.5
print(multiply(2.5, 4))   # 10.0
print(divide(7.5, 2.5))   # 3.0

# Números negativos
print(add(-5, 3))         # -2
print(subtract(-2, -8))   # 6
print(multiply(-3, 4))    # -12
print(divide(-10, 2))     # -5.0
```

## Tratamento de Erros

A biblioteca trata adequadamente casos de erro:

```python
from math_lib import divide

# Divisão por zero
try:
    result = divide(10, 0)
except ValueError as e:
    print(e)  # "Erro: Divisão por zero não é permitida"
```

## Estrutura da Biblioteca

```
math_lib/
├── __init__.py           # Ponto de entrada da biblioteca
├── operations.py         # Operações matemáticas básicas
├── test_math_lib.py      # Testes da biblioteca
└── README.md            # Esta documentação
```

## Funções Disponíveis

### add(a, b)
Soma dois números.
- **Parâmetros**: a, b (números)
- **Retorna**: Resultado da soma
- **Exemplo**: `add(2, 3)` → `5`

### subtract(a, b)
Subtrai dois números.
- **Parâmetros**: a (minuendo), b (subtraendo)
- **Retorna**: Resultado da subtração (a - b)
- **Exemplo**: `subtract(5, 3)` → `2`

### multiply(a, b)
Multiplica dois números.
- **Parâmetros**: a, b (fatores)
- **Retorna**: Resultado da multiplicação
- **Exemplo**: `multiply(3, 4)` → `12`

### divide(a, b)
Divide dois números.
- **Parâmetros**: a (dividendo), b (divisor)
- **Retorna**: Resultado da divisão
- **Exceções**: ValueError se b = 0
- **Exemplo**: `divide(10, 2)` → `5.0`

## Testes

Para executar os testes da biblioteca:

```bash
# Executar testes da biblioteca
cd math_lib
python test_math_lib.py

# Ou usando unittest
python -m unittest test_math_lib.py -v
```

## Uso com a Calculadora

Esta biblioteca é usada pela classe `Calculadora` no projeto principal:

```python
from calculadora import Calculadora

calc = Calculadora()
resultado = calc.somar(5, 3)  # Usa internamente math_lib.add()
```

## Versão

Versão atual: 1.0.0

## Licença

Esta biblioteca foi criada para uso com a Calculadora FastAPI.
