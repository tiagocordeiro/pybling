from pybling.products import list_all, get_product


def test_list_products_response_code_is_200():
    retorno = list_all()
    assert retorno.status_code == 200


def test_list_products_contents():
    retorno = list_all()
    assert 'produtos' in retorno.text


def test_get_product_response_code_is_200():
    produtos = list_all()
    produto = produtos.json()['retorno']['produtos'][0]
    produto_codigo = produto['produto']['codigo']

    retorno = get_product(codigo=produto_codigo)
    assert retorno.status_code == 200


def test_get_product_contents():
    produtos = list_all()
    produto = produtos.json()['retorno']['produtos'][0]
    produto_codigo = produto['produto']['codigo']

    retorno = get_product(codigo=produto_codigo)
    assert 'descricao' in retorno.text
