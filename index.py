from fastapi import FastAPI, Query
from embrapa import Embrapa
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/" , tags=["Rota_teste"])
def read_root():
    return {"mensagem": "API Embrapa"}

@app.get("/producao", tags=["Producao"])
def get_producao(ano: int = Query(2023, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.producao(ano)
    return {f"Producao Vinhos Embrapa - {ano}": dados}

@app.get('/comercializacao', tags=["Comercializacao"])
def get_comercializacao(ano: int = Query(2021, description="Ano desejado para os dados: ")):
    s = Embrapa()
    dados = s.comercializacao(ano)
    return {f"Comercializacao de vinhos - {ano}": dados}

@app.get('/processamento/viniferas', tags=["Processamento"])
def get_processamento_viniferas(ano: int = Query(2023, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.processamento_viniferas(ano)
    return {f"Processamento de viniferas - {ano}": dados}

@app.get('/processamento/americanas', tags=["Processamento"])
def get_processamento_americanas(ano: int = Query(2023, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.processamento_americanas_e_hibridas(ano)
    return {f"Processamento americanas e hibridas - {ano}": dados}

@app.get('/processamento/uvas_de_mesa', tags=["Processamento"])
def get_processamento_uvas_de_mesa(ano: int = Query(2023, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.processamento_uvas_de_mesa(ano)
    return {f"Processamento uvas de mesa - {ano}": dados}

@app.get('/importacao/vinhos_de_mesa', tags=["Importação"])
def importacao_vinhos_de_mesa(ano: int = Query(2024, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.importacao_vinhos_de_mesa(ano)
    return {f"Importacao vinhos de mesa - {ano}": dados}

@app.get('/importacao/espumantes', tags=["Importação"])
def importacao_espumantes(ano: int = Query(2024, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.importacao_espumantes(ano)
    return {f"Importacao vinhos de mesa - {ano}": dados}

@app.get('/importacao/uvas_frescas', tags=["Importação"])
def importacao_uvas_frescas(ano: int = Query(2024, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.importacao_uvas_frescas(ano)
    return {f"Importacao uvas frescas - {ano}": dados}

@app.get('/importacao/uvas_passas', tags=["Importação"])
def importacao_uvas_passas(ano: int = Query(2024, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.importacao_uvas_passas(ano)
    return {f"Importacao uvas_passas - {ano}": dados}

@app.get('/importacao/suco_de_uvas', tags=["Importação"])
def importacao_suco_de_uva(ano: int = Query(2024, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.importacao_suco_de_uva(ano)
    return {f"Importacao suco de uva - {ano}": dados}

@app.get('/exportacao/vinho_de_mesa', tags=["Exportação"])
def exportacao_vinho_de_mesa(ano: int = Query(2024, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.exportacao_suco_de_uva(ano)
    return {f"Exportacao suco de uva - {ano}": dados}

@app.get('/exportacao/espumantes', tags=["Exportação"])
def exportacao_espumantes(ano: int = Query(2024, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.exportacao_espumantes(ano)
    return {f"Exportação espumantes: - {ano}": dados}

@app.get('/exportacao/uvas_frescas', tags=["Exportação"])
def exportacao_uvas_frescas(ano: int = Query(2024, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.exportacao_uvas_frescas(ano)
    return {f"Exportação uvas frescas - {ano}": dados}

@app.get('/exportacao/suco_de_uva', tags=["Exportação"])
def exportacao_suco_de_uva(ano: int = Query(2024, description="Ano desejado para os dados")):
    s = Embrapa()
    dados = s.exportacao_suco_de_uva(ano)
    return {f"Exportação suco de uva - {ano}": dados}




