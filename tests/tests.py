from pybling.contacts import list_contacts, get_contact
from pybling.notas import list_notas, get_nota
from pybling.products import list_products, get_product


# Testes para produtos
def test_list_products_response_code_is_200():
    retorno = list_products()
    assert retorno.status_code == 200


def test_list_products_contents():
    retorno = list_products()
    assert 'produtos' in retorno.text


def test_get_product_response_code_is_200():
    retorno = get_product(codigo='PLA-0000134')
    assert retorno.status_code == 200


def test_get_product_contents():
    retorno = get_product(codigo='PLA-0000134')
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


# Testes para notas fiscais
def test_list_notas_response_code_is_200():
    retorno = list_notas(("01/01/2018", "31/12/2018"), 6)
    assert retorno.status_code == 200


def test_list_notas_content():
    retorno = list_notas(("01/01/2018", "31/12/2018"), 6)
    assert 'retorno' in retorno.text


def test_get_nota_status_code_200():
    retorno = get_nota('000673', '1')
    assert retorno.status_code == 200


def test_get_nota_content():
    retorno = get_nota('000673', '1')
    assert 'numero' in retorno.text


def test_get_all_notas():
    retorno = list_notas(("01/01/2018", "31/12/2018"), 7, tipo='S', page='all')
    assert 'notasfiscais' in retorno['retorno']
