import os
import requests
from dotenv import load_dotenv

load_dotenv()

BLING_SECRET_KEY = os.getenv("BLING_API_KEY")


def list_all():
    url = 'https://bling.com.br/Api/v2/produtos/json/'
    payload = {'apikey': BLING_SECRET_KEY}

    produtos = requests.get(url, params=payload)
    return produtos


def get_product(codigo):
    url = f'https://bling.com.br/Api/v2/produto/{codigo}/json/'
    payload = {'apikey': BLING_SECRET_KEY}

    produto = requests.get(url, params=payload)
    return produto
