# Calculadora FastAPI

Uma API simples para operações básicas de calculadora usando FastAPI.

## Funcionalidades

- ✅ Somar dois números
- ✅ Subtrair dois números  
- ✅ Multiplicar dois números
- ✅ Dividir dois números (com proteção contra divisão por zero)

## Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute a aplicação:
```bash
python main.py
```

3. Acesse a documentação interativa em: http://localhost:8000/docs

## Uso

### Endpoints disponíveis:

- `POST /somar` - Soma dois números
- `POST /subtrair` - Subtrai dois números
- `POST /multiplicar` - Multiplica dois números
- `POST /dividir` - Divide dois números

### Formato da requisição:

```json
{
  "a": 10,
  "b": 5
}
```

### Exemplo de resposta:

```json
{
  "operacao": "soma",
  "a": 10,
  "b": 5,
  "resultado": 15
}
```

## Estrutura do projeto

- `main.py` - Arquivo principal com os endpoints da API
- `calculadora.py` - Classe Calculadora com as operações
- `requirements.txt` - Dependências do projeto
