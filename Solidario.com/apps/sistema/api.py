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

def con_cep_status(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        return 200
    else:
         return 400

def con_cep_encontrado(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return {"erro": "true"}