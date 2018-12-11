from pybling.contacts import list_contacts, get_contact
from pybling.products import list_products, get_product


# Testes para produtos
def test_list_products_response_code_is_200():
    retorno = list_products()
    assert retorno.status_code == 200


def test_list_products_contents():
    retorno = list_products()
    assert 'produtos' in retorno.text


def test_get_product_response_code_is_200():
    produtos = list_products()
    produto = produtos.json()['retorno']['produtos'][0]
    produto_codigo = produto['produto']['codigo']

    retorno = get_product(codigo=produto_codigo)
    assert retorno.status_code == 200


def test_get_product_contents():
    produtos = list_products()
    produto = produtos.json()['retorno']['produtos'][0]
    produto_codigo = produto['produto']['codigo']

    retorno = get_product(codigo=produto_codigo)
    assert 'descricao' in retorno.text


def test_get_all_products():
    retorno = list_products(page='all')
    assert 'produtos' in retorno['retorno']


# Testes para contatos
def test_list_contacts_response_code_is_200():
    retorno = list_contacts()
    assert retorno.status_code == 200


def test_list_contacts_content():
    retorno = list_contacts()
    assert 'contatos' in retorno.text


def test_get_contact_response_code_is_200():
    contatos = list_contacts()
    contato = contatos.json()['retorno']['contatos'][0]
    contato_codigo = contato['contato']['id']

    retorno = get_contact(codigo=contato_codigo)
    assert retorno.status_code == 200


def test_get_contact_content():
    contatos = list_contacts()
    contato = contatos.json()['retorno']['contatos'][0]
    contato_codigo = contato['contato']['id']

    retorno = get_contact(contato_codigo)
    assert 'nome' in retorno.text


def test_get_all_contacts():
    retorno = list_contacts(page='all')
    assert 'contatos' in retorno['retorno']
