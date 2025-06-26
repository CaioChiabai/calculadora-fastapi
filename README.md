# Calculadora FastAPI 2.0

Uma API avançada para operações matemáticas usando FastAPI e a biblioteca personalizada `math_lib`.

## 🚀 Funcionalidades

### Operações Básicas
- ✅ Somar dois números
- ✅ Subtrair dois números  
- ✅ Multiplicar dois números
- ✅ Dividir dois números (com proteção contra divisão por zero)

### Operações Avançadas
- ✅ Potenciação
- ✅ Raiz quadrada
- ✅ Fatorial
- ✅ Porcentagem

### Funções Trigonométricas
- ✅ Seno (radianos e graus)
- ✅ Cosseno (radianos e graus)
- ✅ Tangente (radianos e graus)

### Logaritmos
- ✅ Logaritmo (base personalizada)
- ✅ Logaritmo natural

### Outras Operações
- ✅ Valor absoluto
- ✅ Constantes matemáticas (π, e, φ)

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

4. Acesse a documentação interativa em: http://localhost:8000/docs

## 📖 Uso da API

### Endpoints Básicos:

- `GET /` - Informações da API
- `GET /info` - Informações da calculadora e biblioteca
- `GET /constantes` - Constantes matemáticas
- `POST /somar` - Soma dois números
- `POST /subtrair` - Subtrai dois números
- `POST /multiplicar` - Multiplica dois números
- `POST /dividir` - Divide dois números

### Endpoints Avançados:

- `POST /potencia` - Potenciação
- `POST /raiz-quadrada` - Raiz quadrada
- `POST /fatorial` - Fatorial
- `POST /porcentagem` - Porcentagem

### Endpoints Trigonométricos:

- `POST /seno` - Seno
- `POST /cosseno` - Cosseno
- `POST /tangente` - Tangente

### Endpoints Logarítmicos:

- `POST /logaritmo` - Logaritmo
- `POST /logaritmo-natural` - Logaritmo natural

### Outros Endpoints:

- `POST /valor-absoluto` - Valor absoluto

## 📝 Exemplos de Uso

### Operações Básicas

```json
POST /somar
{
  "a": 10,
  "b": 5
}
```

### Potenciação

```json
POST /potencia
{
  "base": 2,
  "expoente": 8
}
```

### Funções Trigonométricas

```json
POST /seno
{
  "angulo": 90,
  "graus": true
}
```

### Logaritmos

```json
POST /logaritmo
{
  "numero": 100,
  "base": 10
}
```

## 🧪 Testes

Execute os testes:

```bash
python test_calculadora.py
```

Ou use pytest:

```bash
pytest test_calculadora.py -v
```

## 🏗️ Arquitetura

O projeto segue uma arquitetura modular:

1. **API Layer** (`main.py`): Endpoints FastAPI
2. **Service Layer** (`calculadora.py`): Lógica de negócio
3. **Library Layer** (`math_lib/`): Operações matemáticas
4. **Test Layer** (`test_calculadora.py`): Testes unitários

## 📈 Versionamento

- **v1.0.0**: Versão inicial com operações básicas
- **v2.0.0**: Nova versão com biblioteca math_lib e operações avançadas

## 🔧 Desenvolvimento

Para usar a biblioteca math_lib em outros projetos:

```python
from math_lib import add, multiply, sin, log, PI

# Operações básicas
resultado = add(5, 3)

# Operações avançadas
resultado = sin(PI/2)

# Constantes
print(f"π = {PI}")
```

## 📄 Licença

Este projeto é para fins educacionais e de demonstração.
  "resultado": 15
}
```

## Estrutura do projeto

- `main.py` - Arquivo principal com os endpoints da API
- `calculadora.py` - Classe Calculadora com as operações
- `requirements.txt` - Dependências do projeto
