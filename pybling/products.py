import os
import requests
from dotenv import load_dotenv

load_dotenv()

BLING_SECRET_KEY = os.getenv("BLING_API_KEY")


def list_products(page=1):
    url = f'https://bling.com.br/Api/v2/produtos/page={page}/json/'
    payload = {'apikey': BLING_SECRET_KEY}

    if page == 'all':
        page = 1

        while True:
            url = f'https://bling.com.br/Api/v2/produtos/page={page}/json/'
            produtos = requests.get(url, params=payload)
            try:
                pagina = produtos.json()['retorno']['produtos']
                page += 1
                for item in pagina:
                    print(item['produto']['codigo'])
            except KeyError:
                print('fim')
                break

        return produtos

    produtos = requests.get(url, params=payload)
    return produtos


def get_product(codigo):
    url = f'https://bling.com.br/Api/v2/produto/{codigo}/json/'
    payload = {'apikey': BLING_SECRET_KEY}

    produto = requests.get(url, params=payload)
    return produto
