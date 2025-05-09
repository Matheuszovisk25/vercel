from fastapi import FastAPI, Query
from embrapa import Embrapa
from db import init_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Rota_teste"])
def read_root():
    return {"mensagem": "API Embrapa"}

@app.get("/producao", tags=["Producao"])
def get_producao(ano: int = Query(2023)):
    s = Embrapa()
    resultado = s.producao(ano)
    return {
        "fonte": resultado["fonte"],
        f"Producao Vinhos Embrapa - {ano}": resultado["dados"]
    }

@app.get("/comercializacao", tags=["Comercializacao"])
def get_comercializacao(ano: int = Query(2021)):
    s = Embrapa()
    resultado = s.comercializacao(ano)
    return {
        "fonte": resultado["fonte"],
        f"Comercializacao de vinhos - {ano}": resultado["dados"]
    }

@app.get("/processamento/viniferas", tags=["Processamento"])
def get_processamento_viniferas(ano: int = Query(2023)):
    s = Embrapa()
    resultado = s.processamento_viniferas(ano)
    return {
        "fonte": resultado["fonte"],
        f"Processamento de viniferas - {ano}": resultado["dados"]
    }

@app.get("/processamento/americanas", tags=["Processamento"])
def get_processamento_americanas(ano: int = Query(2023)):
    s = Embrapa()
    resultado = s.processamento_americanas_e_hibridas(ano)
    return {
        "fonte": resultado["fonte"],
        f"Processamento americanas e hibridas - {ano}": resultado["dados"]
    }

@app.get("/processamento/uvas_de_mesa", tags=["Processamento"])
def get_processamento_uvas_de_mesa(ano: int = Query(2023)):
    s = Embrapa()
    resultado = s.processamento_uvas_de_mesa(ano)
    return {
        "fonte": resultado["fonte"],
        f"Processamento uvas de mesa - {ano}": resultado["dados"]
    }

@app.get("/importacao/vinhos_de_mesa", tags=["Importação"])
def importacao_vinhos_de_mesa(ano: int = Query(2024)):
    s = Embrapa()
    resultado = s.importacao_vinhos_de_mesa(ano)
    return {
        "fonte": resultado["fonte"],
        f"Importacao vinhos de mesa - {ano}": resultado["dados"]
    }

@app.get("/importacao/espumantes", tags=["Importação"])
def importacao_espumantes(ano: int = Query(2024)):
    s = Embrapa()
    resultado = s.importacao_espumantes(ano)
    return {
        "fonte": resultado["fonte"],
        f"Importacao espumantes - {ano}": resultado["dados"]
    }

@app.get("/importacao/uvas_frescas", tags=["Importação"])
def importacao_uvas_frescas(ano: int = Query(2024)):
    s = Embrapa()
    resultado = s.importacao_uvas_frescas(ano)
    return {
        "fonte": resultado["fonte"],
        f"Importacao uvas frescas - {ano}": resultado["dados"]
    }

@app.get("/importacao/uvas_passas", tags=["Importação"])
def importacao_uvas_passas(ano: int = Query(2024)):
    s = Embrapa()
    resultado = s.importacao_uvas_passas(ano)
    return {
        "fonte": resultado["fonte"],
        f"Importacao uvas passas - {ano}": resultado["dados"]
    }

@app.get("/importacao/suco_de_uvas", tags=["Importação"])
def importacao_suco_de_uva(ano: int = Query(2024)):
    s = Embrapa()
    resultado = s.importacao_suco_de_uva(ano)
    return {
        "fonte": resultado["fonte"],
        f"Importacao suco de uva - {ano}": resultado["dados"]
    }

@app.get("/exportacao/vinho_de_mesa", tags=["Exportação"])
def exportacao_vinho_de_mesa(ano: int = Query(2024)):
    s = Embrapa()
    resultado = s.exportacao_vinho_de_mesa(ano)
    return {
        "fonte": resultado["fonte"],
        f"Exportacao vinho de mesa - {ano}": resultado["dados"]
    }

@app.get("/exportacao/espumantes", tags=["Exportação"])
def exportacao_espumantes(ano: int = Query(2024)):
    s = Embrapa()
    resultado = s.exportacao_espumantes(ano)
    return {
        "fonte": resultado["fonte"],
        f"Exportacao espumantes - {ano}": resultado["dados"]
    }

@app.get("/exportacao/uvas_frescas", tags=["Exportação"])
def exportacao_uvas_frescas(ano: int = Query(2024)):
    s = Embrapa()
    resultado = s.exportacao_uvas_frescas(ano)
    return {
        "fonte": resultado["fonte"],
        f"Exportacao uvas frescas - {ano}": resultado["dados"]
    }

@app.get("/exportacao/suco_de_uva", tags=["Exportação"])
def exportacao_suco_de_uva(ano: int = Query(2024)):
    s = Embrapa()
    resultado = s.exportacao_suco_de_uva(ano)
    return {
        "fonte": resultado["fonte"],
        f"Exportacao suco de uva - {ano}": resultado["dados"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("index:app", host="0.0.0.0", port=10000)