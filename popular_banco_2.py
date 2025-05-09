from embrapa import Embrapa
from db import init_db, buscar_dados_do_banco
import time

init_db()
e = Embrapa()

anos = list(range(1970, 2025))
categorias = {
    "producao": e.producao,
    "comercializacao": e.comercializacao,
    "viniferas": e.processamento_viniferas,
    "americanas": e.processamento_americanas_e_hibridas,
    "mesa": e.processamento_uvas_de_mesa,
    "imp_vinho": e.importacao_vinhos_de_mesa,
    "imp_espumantes": e.importacao_espumantes,
    "imp_frescas": e.importacao_uvas_frescas,
    "imp_passas": e.importacao_uvas_passas,
    "imp_suco": e.importacao_suco_de_uva,
    "exp_vinho": e.exportacao_vinho_de_mesa,
    "exp_espumantes": e.exportacao_espumantes,
    "exp_frescas": e.exportacao_uvas_frescas,
    "exp_suco": e.exportacao_suco_de_uva,
}

falhas = []

print("⏳ Iniciando preenchimento do banco...")

for ano in anos:
    for categoria, funcao in categorias.items():
        try:
            existente = buscar_dados_do_banco(categoria, ano)
            if existente:
                print(f"🟡 Dados já existem: {categoria} - {ano}")
                continue

            funcao(ano)
            print(f"✅ Sucesso: {categoria} - {ano}")
            time.sleep(1)
        except Exception as ex:
            print(f"❌ Erro: {categoria} - {ano} => {ex}")
            falhas.append((categoria, ano))

if falhas:
    print("\n❗ Tentativas com falha:")
    for cat, yr in falhas:
        print(f"- {cat} - {yr}")
else:
    print("\n🎉 Todos os dados foram preenchidos com sucesso!")