# main.py

from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# Cria a instância da aplicação FastAPI
app = FastAPI(
    title="API de Conversão de Temperatura",
    description="Uma API simples para converter temperaturas entre Celsius e Fahrenheit.",
    version="1.0.0"
)

# --- Funções de Lógica de Negócio ---
def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """Converte graus Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converte graus Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5/9

# --- Endpoints da API ---
@app.get("/")
def read_root():
    """Endpoint raiz que retorna uma mensagem de boas-vindas."""
    return {"message": "Bem-vindo à API de Conversão de Temperatura"}

@app.get("/convert/celsius-to-fahrenheit/{celsius}")
def get_celsius_to_fahrenheit(
    celsius: float = Path(..., title="Temperatura em Celsius", description="O valor de temperatura em graus Celsius a ser convertido.")
):
    """
    Endpoint para converter Celsius para Fahrenheit.
    """
    fahrenheit_result = convert_celsius_to_fahrenheit(celsius)
    response_data = {
        "celsius_input": celsius,
        "fahrenheit_result": round(fahrenheit_result, 2)
    }
    return JSONResponse(content=jsonable_encoder(response_data))

@app.get("/convert/fahrenheit-to-celsius/{fahrenheit}")
def get_fahrenheit_to_celsius(
    fahrenheit: float = Path(..., title="Temperatura em Fahrenheit", description="O valor de temperatura em graus Fahrenheit a ser convertido.")
):
    """
    Endpoint para converter Fahrenheit para Celsius.
    """
    celsius_result = convert_fahrenheit_to_celsius(fahrenheit)
    response_data = {
        "fahrenheit_input": fahrenheit,
        "celsius_result": round(celsius_result, 2)
    }
    return JSONResponse(content=jsonable_encoder(response_data))