import os

import requests
from dotenv import load_dotenv

load_dotenv()

BLING_SECRET_KEY = os.getenv("BLING_API_KEY")


def list_notas(periodo, situcacao, tipo='S', page=1):
    """
    Função que retorna todas as notas fiscais
    :param periodo: ('01/01/2018','31/12/2018')
    :param situcacao: 6
    :param tipo: 'S' # 'S' Saída / 'E' Entrada
    :param page: 'all' # Ou 1
    :return: Retorna as notas filtradas por período e situação e tipo

    Exemplo de uso:
    >>> notas = list_notas(("01/01/2018", "31/12/2018"), 6, tipo='S', page=1)
    >>> notas
    <Response [200]>
    """
    url = f'https://bling.com.br/Api/v2/notasfiscais/page={page}/json/'
    payload = {'apikey': BLING_SECRET_KEY,
               'filters': f"dataEmissao[{periodo[0]} TO {periodo[1]}]; situacao[{situcacao}]; tipo[{tipo}]",
               }

    if page == 'all':
        page = 1
        all_notas = {'retorno': {'notasfiscais': []}}

        while True:
            url = f'https://bling.com.br/Api/v2/notasfiscais/page={page}/json/'
            notas = requests.get(url, params=payload)
            try:
                pagina = notas.json()['retorno']['notasfiscais']
                page += 1
                for item in pagina:
                    all_notas['retorno']['notasfiscais'].append(item)
            except KeyError:
                break

        return all_notas

    notas = requests.get(url, params=payload)
    return notas


def get_nota(numero, serie):
    """
    Função que retorna os dados de uma nota fiscal
    :param numero: 000673
    :param serie: 1
    :return: Retorna os dados da nota

    Exemplo de uso:
    >>> nota = get_nota('000673', '1')
    >>> nota
    <Response [200]>
    >>> nota.json()['retorno']['notasfiscais'][0]['notafiscal']['numero']
    '000673'
    >>> nota.json()['retorno']['notasfiscais'][0]['notafiscal']['valorNota']
    '7990.00'
    >>> nota.json()['retorno']['notasfiscais'][0]['notafiscal']['dataEmissao']
    '2018-12-05 13:10:43'
    """
    url = f'https://bling.com.br/Api/v2/notafiscal/{numero}/{serie}/json/'
    payload = {'apikey': BLING_SECRET_KEY}

    nota = requests.get(url, params=payload)
    return nota
