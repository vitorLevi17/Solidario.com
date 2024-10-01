import requests


def con_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        dados_cep = response.json()
        if not response.status_code == 400:
            return dados_cep
        else:
            return "CEP inválido."
    else:
        return "Erro na requisição."