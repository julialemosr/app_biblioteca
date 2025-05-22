import requests

def exemplo_cep():
    cep = '16702266'
    url = f'https://viacep.com.br/ws/{cep}/json/'
    # response pode ser o nome que quiser, quando tiver mais de 1 uma, não pode repetir
    response_cep = requests.get(url)

    if response_cep.status_code == 200:
        dados_cep = response_cep.json()
        print(f"Logradouro: {dados_cep['logradouro']}\n")
        print(f"Localidade: {dados_cep['localidade']}\n")
        print(f"Bairro: {dados_cep['bairro']}\n")
        print(f"UF: {dados_cep['uf']}\n")
        print(f"Estado: {dados_cep['estado']}\n")
        print(f"Região: {dados_cep['regiao']}\n")
        print(f"DDD: {dados_cep['ddd']}\n")
    else:
        print(f"Erro: {response_cep.status_code}")


def exemplo_get(id): #buscar
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    response_get = requests.get(url) #response é retorno de api/resposta

    if response_get.status_code == 200: #codigo de sucesso
        dados_get = response_get.json() #dados do get recebe resposta em json
        print(f"Título: {dados_get['title']}\n") #dados
        print(f"Conteúdo: {dados_get['body']}") #dados
    else:
        print(f"Erro: {response_get.status_code}")

#o número que está sendo colocado e o id
#exemplo_get(5)


def exemplo_post(): #criar
    url = f"https://jsonplaceholder.typicode.com/posts"
    nova_postagem = {
        "title": "Novo título",
        "body": "Novo conteúdo",
        "userId": 1
    }

    response_post = requests.post(url, json=nova_postagem)

    if response_post.status_code == 201: #codigo de sucesso para criação
        dados_post = response_post.json()
        print(f"Titulo: {dados_post['title']}\n")
        print(f"Conteúdo: {dados_post['body']}")
    else:
        print(f"Erro: {response_post.status_code}")

#exemplo_post()


def exemplo_put(id): #atualizar
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    nova_postagem = {
        "id": id, #todos os ID tem que ser o mesmo
        "title": "Novo título",
        "body": "Novo conteúdo",
        "userId": 1
    }

    antes = requests.get(url)
    response_put = requests.put(url, json=nova_postagem) #depois

    if response_put.status_code == 200:
        if antes.status_code == 200:
            dados_antes = antes.json()
            print(f"Título antigo: {dados_antes['title']}\n")
        else:
            print(f"Erro: {antes.status_code}")

        dados_put = response_put.json()
        print(f"Titulo: {dados_put['title']}\n")
    else:
        print(f"Erro: {response_put.status_code}")

exemplo_put(5)