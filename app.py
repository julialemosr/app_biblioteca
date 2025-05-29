import flet as ft
from flet import AppBar, Text, View, ElevatedButton
from flet.core.colors import Colors
import requests
from flet.core.types import CrossAxisAlignment


def main(page: ft.Page):
    page.title = "Biblioteca"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    livro = []

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                (
                    ft.Container(
                        ft.Image(src='livro.png', width=300, height=300),
                    ),
                        AppBar(title=Text(""), bgcolor=Colors.INDIGO_900),
                        ElevatedButton(text="Listar livros", on_click=lambda _: page.go("/segunda")),
                        ElevatedButton(text="Listar usuários", on_click=lambda _: page.go("/terceira")),
                        ElevatedButton(text="Listar empréstimos", on_click=lambda _: page.go("/quarta")),
                        ElevatedButton(text="Cadastro de livros", on_click=lambda _: page.go("/quinta")),
                        ElevatedButton(text="Cadastro de usuários", on_click=lambda _: page.go("/sexta")),
                        ElevatedButton(text="Realizar empréstimo", on_click=lambda _: page.go("/setimo")),
                        ElevatedButton(text="Atualizar livros", on_click=lambda _: page.go("/oitavo")),
                        ElevatedButton(text="Atualizar usuários", on_click=lambda _: page.go("/nono")),
                        ElevatedButton(text="Status do livro", on_click=lambda _: page.go("/decimo")),
                        ElevatedButton(text="Histórico de empréstimo", on_click=lambda _: page.go("/ultima")),


                ),
                bgcolor=ft.Colors.INDIGO_900,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )

        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                            AppBar(title=Text(""), bgcolor=Colors.INDIGO_900),
                            Text(theme_style=ft.TextThemeStyle.TITLE_MEDIUM, value="LISTAR LIVRO:\n"),
                            input_titulo,
                            input_autor,
                            input_isbn,
                            input_resumo,
                            ElevatedButton(text="Listar livros"
                    ],
                    bgcolor=ft.Colors.INDIGO_900,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )

    def livros():
        url = "http://10.135.232.24:5000/livros"
        livro_get = requests.get(url)
        if livro_get.status_code == 200:
            dados_get_livro = livro_get.json()
            print(f"Titulo: {dados_get_livro['titulo']}")
            print(f"Autor: {dados_get_livro['autor']}")
            print(f"ISBN: {dados_get_livro['ISBN']}")
            print(f"Resumo: {dados_get_livro['resumo']}")
        else:
            print(f"Erro: {livro_get.status_code}")

    def salvar_livro(e):
        if input_nome.value == "" or input_autor.value == "" or input_isbn.value == "" or input_resumo.value == "":
            page.overlay.append(msg_erro1)
            msg_erro1.open = True
            page.update()
        else:
            livro = livro( #arrumar
                titulo=input_nome.value,
                autor=input_autor.value,
                ISBN=input_isbn.value,
                resumo=input_resumo.value,
            )
            livro.save() #arrumar
            input_nome.value = ""
            input_autor.value = ""
            input_isbn.value = ""
            input_resumo.value = ""
            msg_sucesso6.open = True
            page.update()

    def usuarios():
        url = "http://10.135.232.24:5000/usuarios"
        usuario_get = requests.get(url)
        if usuario_get.status_code == 200:
            dados_get_usuario = usuario_get.json()
            print(f"Nome: {dados_get_usuario['Nome']}")
            print(f"CPF: {dados_get_usuario['CPF']}")
            print(f"Endereço: {dados_get_usuario['endereco']}")
        else:
            print(f"Erro: {usuario_get.status_code}")

    def salvar_usuario(e):
        if input_nome.value == "" or input_cpf.value == "" or input_endereco.value == "" :
            page.overlay.append(msg_erro1)
            msg_erro1.open = True
            page.update()
        else:
            livro = Livro( #arrumar
                titulo=input_nome.value,
                autor=input_cpf.value,
                descricao=input_endereco.value,
            )
            livro.save() #arrumar
            input_nome.value = ""
            input_cpf.value = ""
            input_resumo.value = ""
            msg_sucesso7.open = True
            page.update()

    def emprestimos():
        url = "http://10.135.232.24:5000/emprestimos"
        emprestimo_get = requests.get(url)
        if emprestimo_get.status_code == 200:
            dados_get_emprestimo = emprestimo_get.json()
            print(f"ID do usuário: {dados_get_emprestimo['id_usuario']}")
            print(f"ID do livro: {dados_get_emprestimo['id_livro']}")
            print(f"Data de empréstimo : {dados_get_emprestimo['data_emprestimo']}")
            print(f"Data de devolução: {dados_get_emprestimo['data_devolucao']}")
        else:
            print(f"Erro: {emprestimo_get.status_code}")

    def salvar_emprestimo(e):
        if input_id_usuario.value == "" or input_id_livro.value == "" or input_data_emprestimo.value == "" or input_data_devolucao.value == "":
            page.overlay.append(msg_erro1)
            msg_erro1.open = True
            page.update()
        else:
            livro = Livro( #arrumar
                id_usuario=input_id_usuario.value,
                id_livro=input_id_livro.value,
                data_emprestimo=input_data_emprestimo.value,
                data_devolucao=input_data_devolucao.value,
            )
            livro.save() #arrumar
            input_id_usuario.value = ""
            input_id_livro.value = ""
            input_data_emprestimo.value = ""
            input_data_devolucao.value = ""
            msg_sucesso8.open = True
            page.update()

    def cadastro_livros():
        url = "http://10.135.232.24:5000/novo_livro"

        if input_titulo.value == "" or input_autor.value == "" or input_isbn.value == "" or input_resumo.value == "":
            page.overlay.append(msg_erro1)
            msg_erro1.open = True
            page.update()
        else:
            livro_novo = {
                "Titulo": input_titulo.value,
                "Autor": input_autor.value,
                "ISBN": input_isbn.value,
                "Resumo": input_resumo.value
            }
            input_titulo.value = ""
            input_autor.value = ""
            input_isbn.value = ""
            input_resumo.value = ""
            msg_sucesso1.open = True
            page.update()

        response_livro = requests.post(url, json=livro_novo)

        if response_livro.status_code == 201:
            input_titulo.value = ""
            input_autor.value = ""
            input_isbn.value = ""
            input_resumo.value = ""
            page.overlay.append(msg_sucesso1)
            msg_sucesso1.open = False
            page.update()
        else:
            page.overlay.append(msg_erro2)

    def cadastro_usuarios():
        url = "http://10.135.232.24:5000/novo_usuario"

        if input_nome.value == "" or input_cpf.value == "" or input_endereco.value == "":
            page.overlay.append(msg_erro1)
            msg_erro1.open = True
            page.update()
        else:
            usuario_novo = {
                "Nome": input_nome.value,
                "CPF": input_cpf.value,
                "Endereço": input_endereco.value,
            }
            input_nome.value = ""
            input_cpf.value = ""
            input_endereco.value = ""
            msg_sucesso3.open = True
            page.update()

        response_usuario = requests.post(url, json=usuario_novo)

        if response_usuario.status_code == 201:
            input_nome.value = ""
            input_cpf.value = ""
            input_endereco.value = ""
            page.overlay.append(msg_sucesso3)
            msg_sucesso3.open = False
            page.update()
        else:
            page.overlay.append(msg_erro3)

    def realizar_emprestimos():
        url = "http://10.135.232.24:5000/realizar_emprestimo"

        if input_id_usuario.value == "" or input_id_livro.value == "" or input_data_emprestimo.value == "" or input_data_devolucao.value == "":
            page.overlay.append(msg_erro1)
            msg_erro1.open = True
            page.update()
        else:
            emprestimo_novo = {
                "Id do usuário": input_id_usuario.value,
                "Id do livro": input_id_livro.value,
                "Data de empréstimo": input_data_emprestimo.value,
                "Data de devolução": input_data_devolucao.value,
            }
            input_id_usuario.value = ""
            input_id_livro.value = ""
            input_data_emprestimo.value = ""
            input_data_devolucao.value = ""
            msg_sucesso5.open = True
            page.update()

        response_emprestimo = requests.post(url, json=emprestimo_novo)

        if response_emprestimo.status_code == 200:
            input_id_usuario.value = ""
            input_id_livro.value = ""
            input_data_emprestimo.value = ""
            input_data_devolucao.value = ""
            page.overlay.append(msg_sucesso5)
            msg_sucesso5.open = False
            page.update()
        else:
            page.overlay.append(msg_erro4)

    def atualiza_livro(id_livro):
        url = f"http://10.135.232.24:5000/atualizar_livro/{id_livro}"
        editar_livro = {
            "id": id_livro,
            "titulo": input_titulo.value,
            "autor": input_autor.value,
            "isbn": input_isbn.value,
            "resumo": input_resumo.value
        }

        response_put = requests.put(url, json=editar_livro)
        if response_put.status_code == 200:
            page.overlay.append(msg_sucesso2)
            msg_sucesso2.open = False
            page.update()
        else:
            page.overlay.append(msg_erro5)

    def atualiza_usuario(id_usuario):
        url = f"http://10.135.232.24:5000/atualizar_usuario/{id_usuario}"
        editar_usuario = {
            "id": id_usuario,
            "Nome": input_nome.value,
            "CPF": input_cpf.value,
            "Endereço": input_endereco.value,
        }

        response_put = requests.put(url, json=editar_usuario)
        if response_put.status_code == 200:
            page.overlay.append(msg_sucesso4)
            msg_sucesso4.open = False
            page.update()
        else:
            page.overlay.append(msg_erro6)

    def status_livro():
        url = "http://10.135.232.24:5000/livro_status"
        status_get = requests.get(url)
        if status_get.status_code == 200:
            dados_get_livro = status_get.json()
            print(f"Livros emprestados: {dados_get_livro['lista_emprestados']}")
            print(f"Livros disponíveis: {dados_get_livro['lista_disponiveis']}")
        else:
            print(f"Erro: {status_get.status_code}")

    def historico_emprestimo():
        url = "http://10.135.232.24:5000/consulta_historico_emprestimo"
        historico_emprestimo_get = requests.get(url)
        if historico_emprestimo_get.status_code == 200:
            dados_get_livro = historico_emprestimo_get.json()
            print(f"ID do usuário: {dados_get_livro['id_usuario']}")
            print(f"ID do livro: {dados_get_livro['id_livro']}")
            print(f"Data de empréstimo : {dados_get_livro['data_emprestimo']}")
            print(f"Data de devolução: {dados_get_livro['data_devolucao']}")
        else:
            print(f"Erro: {historico_emprestimo_get.status_code}")

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    input_titulo = ft.TextField(label="Título")
    input_autor = ft.TextField(label="Autor")
    input_isbn = ft.TextField(label="ISBN")
    input_resumo = ft.TextField(label="Resumo")

    input_nome = ft.TextField(label="Nome")
    input_cpf = ft.TextField(label="CPF")
    input_endereco = ft.TextField(label="endereco")

    input_id_usuario = ft.TextField(label="id_usuario")
    input_id_livro = ft.TextField(label="id_livro")
    input_data_emprestimo = ft.TextField(label="data_emprestimo")
    input_data_devolucao = ft.TextField(label="data_devolucao")

    msg_sucesso1 = ft.SnackBar(content=Text("Livro cadastrado com sucesso!"), bgcolor=Colors.GREEN)
    msg_sucesso2 = ft.SnackBar(content=Text("Livro editado com sucesso!"), bgcolor=Colors.GREEN)
    msg_sucesso3 = ft.SnackBar(content=Text("Usuário cadastrado com sucesso!"), bgcolor=Colors.GREEN)
    msg_sucesso4 = ft.SnackBar(content=Text("Usuário editado com sucesso!"), bgcolor=Colors.GREEN)
    msg_sucesso5 = ft.SnackBar(content=Text("Empréstimo realizado com sucesso!"), bgcolor=Colors.GREEN)
    msg_sucesso6 = ft.SnackBar(content=Text("Livro salvo com sucesso!"), bgcolor=Colors.GREEN)
    msg_sucesso7 = ft.SnackBar(content=Text("Usuário salvo com sucesso!"), bgcolor=Colors.GREEN)
    msg_sucesso8 = ft.SnackBar(content=Text("Empréstimo salvo com sucesso!"), bgcolor=Colors.GREEN)

    msg_erro1 = ft.SnackBar(content=Text("Não deixe os campos vazios!"), bgcolor=Colors.RED)
    msg_erro2 = ft.SnackBar(content=Text("Erro! não foi possível cadastrar o livro"), bgcolor=Colors.RED)
    msg_erro3 = ft.SnackBar(content=Text("Erro! não foi possível cadastrar o usuário"), bgcolor=Colors.RED)
    msg_erro4 = ft.SnackBar(content=Text("Erro! não foi possível realizar o empréstimo"), bgcolor=Colors.RED)
    msg_erro5 = ft.SnackBar(content=Text("Erro! não foi possível atualizar o livro"), bgcolor=Colors.RED)
    msg_erro6 = ft.SnackBar(content=Text("Erro! não foi possível atualizar o usuário"), bgcolor=Colors.RED)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

ft.app(main)