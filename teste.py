import requests


def lista_emprestimos():
    url = "http://10.135.232.24:5001/emprestimos"
    emprestimo_get = requests.get(url)
    if emprestimo_get.status_code == 200:
        dados_emprestimo = emprestimo_get.json()
        print("aqui", dados_emprestimo)
        # return dados_emprestimo["emprestimos"]
    else:
        print("erro de emprestimo")

lista_emprestimos()