import requests
from bs4 import BeautifulSoup
import pandas as pd
from db import salvar_dados_no_banco, buscar_dados_do_banco

def scrape(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    tabela = soup.find("table", class_="tb_base tb_dados")
    headers = ["Produto", "Quantidade"]
    data = []

    for linha in tabela.find_all("tr"):
        linha2 = linha.find_all("td")
        if linha2:
            valores = [col.get_text(strip=True) for col in linha2]
            data.append(valores)

    df = pd.DataFrame(data, columns=headers)
    return df.to_dict(orient="records")

def scrape2(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, "html.parser")
    tabela = soup.find("table", class_="tb_base tb_dados")
    headers = ["Produto", "Quantidade", "Valor"]
    data = []

    for linha in tabela.find_all("tr"):
        linha2 = linha.find_all("td")
        if linha2:
            valores = [col.get_text(strip=True) for col in linha2]
            data.append(valores)

    df = pd.DataFrame(data, columns=headers)
    return df.to_dict(orient="records")

class Embrapa():
    def _get_or_scrape(self, categoria, ano, url, tipo=1):
        try:
            dados = scrape(url) if tipo == 1 else scrape2(url)
            salvar_dados_no_banco(categoria, ano, dados)
            return {"fonte": "scraping", "dados": dados}
        except Exception as e:
            print(f"[ERRO SCRAPE] {categoria}-{ano}: {e}")
            dados = buscar_dados_do_banco(categoria, ano)
            if dados:
                return {"fonte": "banco_de_dados", "dados": dados}
            else:
                raise RuntimeError(f"Erro ao acessar dados de {categoria}-{ano} e nenhum dado salvo.")

    def producao(self, ano):
        return self._get_or_scrape("producao", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02")

    def comercializacao(self, ano):
        return self._get_or_scrape("comercializacao", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_04")

    def processamento_viniferas(self, ano):
        return self._get_or_scrape("viniferas", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao=subopt_01")

    def processamento_americanas_e_hibridas(self, ano):
        return self._get_or_scrape("americanas", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao=subopt_02")

    def processamento_uvas_de_mesa(self, ano):
        return self._get_or_scrape("mesa", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao=subopt_03")

    def importacao_vinhos_de_mesa(self, ano):
        return self._get_or_scrape("imp_vinho", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao=subopt_01", tipo=2)

    def importacao_espumantes(self, ano):
        return self._get_or_scrape("imp_espumantes", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao=subopt_02", tipo=2)

    def importacao_uvas_frescas(self, ano):
        return self._get_or_scrape("imp_frescas", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao=subopt_03", tipo=2)

    def importacao_uvas_passas(self, ano):
        return self._get_or_scrape("imp_passas", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao=subopt_04", tipo=2)

    def importacao_suco_de_uva(self, ano):
        return self._get_or_scrape("imp_suco", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao=subopt_05", tipo=2)

    def exportacao_vinho_de_mesa(self, ano):
        return self._get_or_scrape("exp_vinho", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_01", tipo=2)

    def exportacao_espumantes(self, ano):
        return self._get_or_scrape("exp_espumantes", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_02", tipo=2)

    def exportacao_uvas_frescas(self, ano):
        return self._get_or_scrape("exp_frescas", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_03", tipo=2)

    def exportacao_suco_de_uva(self, ano):
        return self._get_or_scrape("exp_suco", ano, f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_04", tipo=2)