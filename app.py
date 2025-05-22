import flet as ft
from flet import AppBar, Text, View, ElevatedButton
from flet.core.colors import Colors
import requests

def main(page: ft.Page):
    page.title = "Biblioteca"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667


    def livros():
        url = "http://10.135.232.24:5000/livros"
        livro_get = requests.get(url)
        if livro_get.status_code == 200:
            dados_get = livro_get.json()
            print(f"Título: {dados_get['title']}\n")
            print(f"Autor: {dados_get['author']}\n")
            print(f"ISBN: {dados_get['isbn']}\n")
            print(f"Resumo: {dados_get['resumo']}\n")
        else:
            print(f"Erro: {livro_get.status_code}")


    def cadastro_livro(page: ft.Page):
        url = "http://10.135.232.24:5000/novo_livro"

        if input_titulo.value == "" or input_autor.value == "" or input_ISBN.value == "" or input_resumo.value == "":
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()
        else:
            livro_novo = {
                "Titulo": input_titulo.value,
                "Autor": input_autor.value,
                "ISBN": input_ISBN.value,
                "Resumo": input_resumo.value
            }
            input_titulo.value = ""
            input_autor.value = ""
            input_ISBN.value = ""
            input_resumo.value = ""
            msg_sucesso.open = True
            page.update()

        response = requests.post(url, json=livro_novo)


input_titulo = ft.TextField(label="Título")
input_autor = ft.TextField(label="Autor")
input_ISBN = ft.TextField(label="ISBN")
input_resumo = ft.TextField(label="Resumo")

msg_sucesso = ft.SnackBar(content=Text("Livro cadastrado com sucesso!"), bgcolor=Colors.GREEN)
msg_erro = ft.SnackBar(content=Text("Não deixe os campos vazios!"), bgcolor=Colors.RED)
