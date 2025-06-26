# Calculadora FastAPI

Uma API avançada para operações matemáticas usando FastAPI e a biblioteca personalizada `math_lib`.

## 🚀 Funcionalidades

### Operações Básicas
- ✅ Somar dois números
- ✅ Subtrair dois números  
- ✅ Multiplicar dois números
- ✅ Dividir dois números (com proteção contra divisão por zero)

## 📚 Biblioteca Math_Lib

Este projeto agora inclui uma biblioteca personalizada `math_lib` que fornece todas as operações matemáticas. A biblioteca é:

- **Modular**: Separada em módulos específicos
- **Documentada**: Todas as funções possuem documentação completa
- **Testada**: Cobertura completa de testes
- **Type-safe**: Suporte completo a type hints

### Estrutura da Biblioteca

```
math_lib/
├── __init__.py           # Ponto de entrada
├── operations.py         # Operações básicas
├── advanced_operations.py # Operações avançadas
├── constants.py          # Constantes matemáticas
└── README.md            # Documentação da biblioteca
```

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd calculadora-fastapi
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
python main.py
```
