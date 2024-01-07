from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random 


app = FastAPI()
fake = Faker()

file_name = 'backend/fakeapi/products.csv'
df = pd.read_csv(file_name, sep=";")
df['EAN'] = df['EAN'].astype(str)
df['indice'] = range(1, len(df)+1)
df.set_index('indice', inplace=True)

@app.get("/gerar_compras")
async def gerar_compras():
    index = random.randint(1, len(df)-1)
    tuple = df.iloc[index]

    return{
        "client": fake.name(),
        "creditcard": fake.credit_card_provider(),
        "store": 11,
        "product_name": tuple["Produto"],
        "ean": tuple["EAN"],
        "price": round(float(tuple["Preco"])*1.2,2),
        "dateTime": fake.iso8601(),
        "clientPosition": fake.location_on_land()
    }

@app.get("/gerar_compras/{numero_registro}")
async def gerar_compras(numero_registro: int):

    if numero_registro < 1 :
        return{ "error":  "numero_registro deve ser maior que 1"}
    
    respostas = []
    for _ in range(numero_registro):
        index = random.randint(1, len(df)-1)
        tuple = df.iloc[index]
        compra = {
            "client": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product_name": tuple["Produto"],
            "ean": tuple["EAN"],
            "price": round(float(tuple["Preco"])*1.2,2),
            "dateTime": fake.iso8601(),
            "clientPosition": fake.location_on_land()
        }
        respostas.append(compra)
    return respostas