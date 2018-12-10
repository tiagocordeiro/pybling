import os

import requests
from dotenv import load_dotenv

load_dotenv()

BLING_SECRET_KEY = os.getenv("BLING_API_KEY")


def list_contacts():
    url = 'https://bling.com.br/Api/v2/contatos/json/'
    payload = {'apikey': BLING_SECRET_KEY}

    contatos = requests.get(url, params=payload)
    return contatos


def get_contact(codigo, identificador=2):
    url = f'https://bling.com.br/Api/v2/contato/{codigo}/json/'
    payload = {'apikey': BLING_SECRET_KEY,
               'identificador': identificador, }

    contato = requests.get(url, params=payload)
    return contato
