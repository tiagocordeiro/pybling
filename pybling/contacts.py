import os
import requests
from dotenv import load_dotenv

load_dotenv()

BLING_SECRET_KEY = os.getenv("BLING_API_KEY")


def list_contacts(page=1):
    url = f'https://bling.com.br/Api/v2/contatos/page={page}/json/'
    payload = {'apikey': BLING_SECRET_KEY}

    if page == 'all':
        page = 1
        all_contacts = {'retorno': {'contatos': []}}

        while True:
            url = f'https://bling.com.br/Api/v2/contatos/page={page}/json/'
            contatos = requests.get(url, params=payload)
            try:
                pagina = contatos.json()['retorno']['contatos']
                page += 1
                for item in pagina:
                    all_contacts['retorno']['contatos'].append(item)
            except KeyError:
                break

        return all_contacts

    contatos = requests.get(url, params=payload)
    return contatos


def get_contact(codigo, identificador=2):
    url = f'https://bling.com.br/Api/v2/contato/{codigo}/json/'
    payload = {'apikey': BLING_SECRET_KEY,
               'identificador': identificador, }

    contato = requests.get(url, params=payload)
    return contato
