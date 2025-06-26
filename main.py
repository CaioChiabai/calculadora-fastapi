from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calculadora import Calculadora

app = FastAPI(title="Calculadora API", description="Uma API para operações básicas de calculadora")

class OperacaoRequest(BaseModel):
    a: float
    b: float

# Instância da calculadora
calc = Calculadora()

@app.get("/")
async def root():
    return {"message": "Bem-vindo à Calculadora API! Use os endpoints /somar, /subtrair, /dividir, /multiplicar"}

@app.post("/somar")
async def somar(operacao: OperacaoRequest):
    """Soma dois números"""
    resultado = calc.somar(operacao.a, operacao.b)
    return {
        "operacao": "soma",
        "a": operacao.a,
        "b": operacao.b,
        "resultado": resultado
    }

@app.post("/subtrair")
async def subtrair(operacao: OperacaoRequest):
    """Subtrai dois números"""
    resultado = calc.subtrair(operacao.a, operacao.b)
    return {
        "operacao": "subtração",
        "a": operacao.a,
        "b": operacao.b,
        "resultado": resultado
    }

@app.post("/multiplicar")
async def multiplicar(operacao: OperacaoRequest):
    """Multiplica dois números"""
    resultado = calc.multiplicar(operacao.a, operacao.b)
    return {
        "operacao": "multiplicação",
        "a": operacao.a,
        "b": operacao.b,
        "resultado": resultado
    }

@app.post("/dividir")
async def dividir(operacao: OperacaoRequest):
    """Divide dois números"""
    try:
        resultado = calc.dividir(operacao.a, operacao.b)
        return {
            "operacao": "divisão",
            "a": operacao.a,
            "b": operacao.b,
            "resultado": resultado
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
