import requests
def lista_livros():
    url = "http://10.135.232.24:5000/livros"
    livro_get = requests.get(url)
    if livro_get.status_code == 200:
        dados_get_livro = livro_get.json()
        return dados_get_livro
    else:
        f"Erro: {livro_get.status_code}"

lista_livros()