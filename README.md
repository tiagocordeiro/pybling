# pybling
## Integração com API do Bling usando Python


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
pytest tests/tests.py
```
