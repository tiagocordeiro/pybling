# pybling
## Integração com API do Bling usando Python
[![Build Status](https://travis-ci.org/tiagocordeiro/pybling.svg?branch=master)](https://travis-ci.org/tiagocordeiro/pybling)
[![Updates](https://pyup.io/repos/github/tiagocordeiro/pybling/shield.svg)](https://pyup.io/repos/github/tiagocordeiro/pybling/)
[![Python 3](https://pyup.io/repos/github/tiagocordeiro/pybling/python-3-shield.svg)](https://pyup.io/repos/github/tiagocordeiro/pybling/)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/tiagocordeiro/pybling/blob/master/LICENSE)

### Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Configure sua API Key


```
git clone https://github.com/tiagocordeiro/pybling.git
cd pybling
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python contrib/env_gen.py
```


### Testes

Rode os testes
```
pytest tests/tests.py --verbosity=1 
```

Como usar
```
>>> from pybling.products import list_all
>>> produtos = list_all()
>>> produtos
<Response [200]>

```
