import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def buscar_dados(simbolo, periodo='5d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo
    return dados

def buscar_todos_os_dados(commodities):
    todos_os_dados = []
    for simbolo in commodities:
        dados = buscar_dados(simbolo)
        todos_os_dados.append(dados)
    return pd.concat(todos_os_dados)


if __name__ == "__main__":
    commodities = ['CL=F', 'GC=F', 'SI=F']
    dados_concatenados = buscar_todos_os_dados(commodities)
    print(dados_concatenados)