import flet as ft
from flet import AppBar, Text, View, ElevatedButton
from flet.core.colors import Colors
import requests
from flet.core.dropdown import Option
from flet.core.types import CrossAxisAlignment

id_usuario_global = 0
id_livro_global = 0
id_emprestimo_global = 0

def main(page: ft.Page):
    page.title = "Biblioteca"
    #page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667


    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                (
                    ft.Container(
                        ft.Image(src='livro.png', width=300, height=300),
                    ),
                        AppBar(title=Text(""), bgcolor="#e7c18e"),
                        ElevatedButton(text="Livros", bgcolor="#896d56", color= "#ffffff",width=110, on_click=lambda _: page.go("/segunda")),
                        ElevatedButton(text="Usuários", bgcolor="#896d56",color= "#ffffff",width=110, on_click=lambda _: page.go("/terceira")),
                        ElevatedButton(text="Empréstimos", bgcolor="#896d56",color= "#ffffff",width=110, on_click=lambda _: page.go("/quarta")),

                ),
                bgcolor="#e7c18e",
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )

        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        ft.Container(
                            ft.Image(src='livro1.png', width=200, height=200),
                        ),
                            AppBar(title=Text(""), bgcolor="#e7c18e"),
                            Text(theme_style=ft.TextThemeStyle.TITLE_MEDIUM, value=" LIVROS: \n"),
                            ElevatedButton(text="Listar livros", bgcolor="#896d56", color="#ffffff", width=200, on_click=lambda _: page.go("/livros")),
                            ElevatedButton(text="Cadastrar livros", bgcolor="#896d56", color="#ffffff", width=200, on_click=lambda _: page.go("/novo_livro")),
                            ElevatedButton(text="Status dos livros", bgcolor="#896d56", color="#ffffff", width=200, on_click=lambda _: page.go("/status_livro")),
                    ],
                    bgcolor="#e7c18e",
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/terceira":
            page.views.append(
                View(
                    "/terceira",
                    [
                        ft.Container(
                            ft.Image(src='livro1.png', width=200, height=200),
                        ),
                        AppBar(title=Text(""), bgcolor="#e7c18e"),
                        Text(theme_style=ft.TextThemeStyle.TITLE_MEDIUM, value=" USUÁRIOS: \n"),
                        ElevatedButton(text="Listar usuários", bgcolor="#896d56", color="#ffffff", width=200,
                                       on_click=lambda _: page.go("/usuarios")),
                        ElevatedButton(text="Cadastrar usuários", bgcolor="#896d56", color="#ffffff", width=200,
                                       on_click=lambda _: page.go("/novo_usuario")),
                    ],
                    bgcolor="#e7c18e",
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/quarta":
            page.views.append(
                View(
                    "/quarta",
                    [
                        ft.Container(
                            ft.Image(src='livro1.png', width=200, height=200),
                        ),
                        AppBar(title=Text(""), bgcolor="#e7c18e"),
                        Text(theme_style=ft.TextThemeStyle.TITLE_MEDIUM, value=" EMPRÉSTIMO: \n"),
                        ElevatedButton(text="Listar empréstimo", bgcolor="#896d56", color="#ffffff", width=200,
                                       on_click=lambda _: page.go("/emprestimos")),
                        ElevatedButton(text="Realizar empréstimo", bgcolor="#896d56", color="#ffffff", width=200,
                                       on_click=lambda _: page.go("/realizar_emprestimos")),
                        ElevatedButton(text="Histórico empréstimo", bgcolor="#896d56", color="#ffffff", width=200,
                                       on_click=lambda _: page.go("/historico_emprestimos")),
                    ],
                    bgcolor="#e7c18e",
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/livros" or page.route == "/detalhes_livro":
            livros(e)
            page.views.append(
                View(
                    "/livros",
                    [
                        AppBar(title=Text("LISTA"), bgcolor="#896d56"),
                        lv_livro,
                        ElevatedButton(text="Voltar", on_click=lambda _: page.go("/segunda"), bgcolor="#896d56",
                                       color="#ffffff", width=150)
                    ],
                    bgcolor = "#e7c18e",
                    horizontal_alignment = CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/detalhes_livro":
            page.views.append(
                View(
                    "/detalhes_livro",
                    [
                        AppBar(title=Text("INFORMAÇÕES"), bgcolor="#896d56"),
                        txt_titulo,
                        txt_autor,
                        txt_isbn,
                        txt_resumo
                    ],
                    bgcolor="#e7c18e",
                )
            )
        if page.route == "/usuarios" or page.route == "/detalhes_usuario":
            usuarios(e)
            page.views.append(
                View(
                    "/usuarios",
                    [
                        AppBar(title=Text("LISTA"), bgcolor="#896d56"),
                        lv_usuario,
                        ElevatedButton(text="Voltar", on_click=lambda _: page.go("/terceira"), bgcolor="#896d56",
                                       color="#ffffff", width=150)
                    ],
                    bgcolor = "#e7c18e",
                    horizontal_alignment = CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/detalhes_usuario":
            page.views.append(
                View(
                    "/detalhes_usuario",
                    [
                        AppBar(title=Text("INFORMAÇÕES"), bgcolor="#896d56"),
                        txt_nome,
                        txt_cpf,
                        txt_endereco,
                    ],
                    bgcolor="#e7c18e",
                )
            )
        if page.route == "/emprestimos" or page.route == "/detalhes_emprestimo":
            emprestimos(e)
            page.views.append(
                View(
                    "/emprestimos",
                    [
                        AppBar(title=Text("LISTA"), bgcolor="#896d56"),
                        lv_emprestimo,
                        ElevatedButton(text="Voltar", on_click=lambda _: page.go("/quarta"), bgcolor="#896d56",
                                       color="#ffffff", width=150)
                    ],
                    bgcolor = "#e7c18e",
                    horizontal_alignment = CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/detalhes_emprestimo":
            page.views.append(
                View(
                    "/detalhes_emprestimo",
                    [
                        AppBar(title=Text("INFORMAÇÕES"), bgcolor="#896d56"),
                        txt_id_usuario,
                        txt_id_livro,
                        txt_data_emprestimo,
                        txt_data_devolucao,
                    ],
                    bgcolor="#e7c18e",
                )
            )

        if page.route == "/novo_livro":
            page.views.append(
                View(
                    "/novo_livro",
                    [
                            AppBar(title=Text("CADASTRO DE LIVRO"), bgcolor="#896d56", color= "#ffffff"),
                            Text(theme_style=ft.TextThemeStyle.TITLE_MEDIUM, value="\n"),
                            input_titulo,
                            input_autor,
                            input_isbn,
                            input_resumo,
                            ElevatedButton(text="Salvar", on_click=lambda _: salvar_livro(e), bgcolor="#896d56",color="#ffffff", width=150),
                            ElevatedButton(text="Voltar", on_click=lambda _: page.go("/segunda"), bgcolor="#896d56",color="#ffffff", width=150)

                    ],
                    bgcolor="#e7c18e",
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/novo_usuario":
            page.views.append(
                View(
                    "/novo_usuario",
                    [
                            AppBar(title=Text("CADASTRO DE USUÁRIO"), bgcolor="#896d56", color= "#ffffff"),
                            Text(theme_style=ft.TextThemeStyle.TITLE_MEDIUM, value="\n"),
                            input_nome,
                            input_cpf,
                            input_endereco,
                            ElevatedButton(text="Salvar", on_click=lambda _: salvar_usuario(e) , bgcolor="#896d56",color="#ffffff", width=150),
                            ElevatedButton(text="Voltar", on_click=lambda _: page.go("/terceira"), bgcolor="#896d56",color="#ffffff", width=150)

                    ],
                    bgcolor="#e7c18e",
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )
        if page.route == "/realizar_emprestimos":
            page.views.append(
                View(
                    "/realizar_emprestimos",
                    [
                            AppBar(title=Text("REALIZAR EMPRÉSTIMO"), bgcolor="#896d56", color= "#ffffff"),
                            Text(theme_style=ft.TextThemeStyle.TITLE_MEDIUM, value=""),
                            input_id_livro,
                            input_id_usuario,
                            input_data_emprestimo,
                            input_data_devolucao,
                            ElevatedButton(text="Adicionar", on_click=lambda _: salvar_emprestimo(e),bgcolor="#896d56", color= "#ffffff", width=150),
                            ElevatedButton(text="Voltar", on_click=lambda _: page.go("/quarta"),bgcolor="#896d56", color= "#ffffff", width=150)

                    ],
                    bgcolor="#e7c18e",
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/atualizar_livro":
            page.views.append(
                View(
                    "/atualizar_livro",
                    [
                            AppBar(title=Text("ATUALIZAR LIVROS"), bgcolor="#896d56", color= "#ffffff"),
                            Text(theme_style=ft.TextThemeStyle.TITLE_MEDIUM, value=""),
                            input_titulo,
                            input_autor,
                            input_isbn,
                            input_resumo,
                            ElevatedButton(text="Salvar", on_click=lambda _: atualiza_livro(e),bgcolor="#896d56", color= "#ffffff", width=150),
                            ElevatedButton(text="Voltar", on_click=lambda _: page.go("/segunda"),bgcolor="#896d56", color= "#ffffff", width=150)

                    ],
                    bgcolor="#e7c18e",
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                )
            )

        if page.route == "/atualizar_usuario":
            page.views.append(
                View(
                    "/atualizar_usuario",
                    [
                            AppBar(title=Text("ATUALIZAR USUÁRIOS"), bgcolor="#896d56", color= "#ffffff"),
                            Text(theme_style=ft.TextThemeStyle.TITLE_MEDIUM, value=""),
                            input_nome,
                            input_cpf,
                            input_endereco,
                            ElevatedButton(text="Salvar", on_click=lambda _: atualiza_usuario(e),bgcolor="#896d56", color= "#ffffff", width=150),
                            ElevatedButton(text="Voltar", on_click=lambda _: page.go("/terceira"),bgcolor="#896d56", color= "#ffffff", width=150)

                    ],
                    bgcolor="#e7c18e",
                    horizontal_alignment=CrossAxisAlignment.CENTER,

                )
            )
        if page.route == "/atualizar_emprestimos":
            page.views.append(
                View(
                    "/atualizar_emprestimos",
                    [
                            AppBar(title=Text("ATUALIZAR EMPRÉSTIMOS"), bgcolor="#896d56", color= "#ffffff"),
                            Text(theme_style=ft.TextThemeStyle.TITLE_MEDIUM, value=""),
                            input_nome,
                            input_cpf,
                            input_endereco,
                            ElevatedButton(text="Salvar", on_click=lambda _: atualiza_emprestimo(e),bgcolor="#896d56", color= "#ffffff", width=150),
                            ElevatedButton(text="Voltar", on_click=lambda _: page.go("/quarta"),bgcolor="#896d56", color= "#ffffff", width=150)

                    ],
                    bgcolor="#e7c18e",
                    horizontal_alignment=CrossAxisAlignment.CENTER,

                )
            )
        page.update()

    def get_lista_livros():
        url = "http://10.135.232.24:5000/livros"
        livro_get = requests.get(url)
        if livro_get.status_code == 200:
            dados_get_livro = livro_get.json()
            return dados_get_livro
        else:
            f"Erro: {livro_get.status_code}"
            return {
                "erro": livro_get.json()
            }

    def livros(e):
        lv_livro.controls.clear()
        lista_resultados = get_lista_livros()
        print(lista_resultados)

        if "error" in lista_resultados:
            print("Erro: ", lista_resultados)
        else:
            print(lista_resultados)

            for livro in lista_resultados['lista_livros']:
                print("aa", lista_resultados)
                lv_livro.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.BOOK),
                        title=ft.Text(f"Titulo: {livro['Titulo']}"),
                        trailing=ft.PopupMenuButton(
                            icon=ft.Icons.REMOVE_RED_EYE,
                            items=[
                                ft.PopupMenuItem(
                                    text="Informações",
                                    on_click=lambda _, l=livro: detalhes_livro(l)
                                )
                            ]
                        )
                    )
                )
        page.update()

    def lista_livros():
        url = "http://10.135.232.24:5000/livros"
        livros_get = requests.get(url)
        if livros_get.status_code == 200:
            dados_get_livros = livros_get.json()
            return dados_get_livros
        else:
            print(f"Erro: {livros_get.status_code}")
            return {
                "erro": livros_get.json()
            }

    def detalhes_livro(lista_livros):
        txt_titulo.value = lista_livros["Titulo"]
        txt_autor.value = lista_livros["Autor"]
        txt_isbn.value = lista_livros["ISBN"]
        txt_resumo.value = lista_livros["Resumo"]
        page.update()
        page.go("/detalhes_livro")

    def salvar_livro(e):
        if input_titulo.value == "" or input_autor.value == "" or input_isbn.value == "" or input_resumo.value == "":
            page.overlay.append(msg_erro1)
            msg_erro1.open = True
            page.update()
        else:
            novo_livro =  {
                "titulo" : input_titulo.value,
                "autor" : input_autor.value,
                "ISBN" : int(input_isbn.value),
                "resumo" : input_resumo.value,
            }

            cadastro_livros(novo_livro)

    def lista_usuarios():
        url = "http://10.135.232.24:5000/usuarios"
        usuario_get = requests.get(url)
        if usuario_get.status_code == 200:
            dados_get_usuario = usuario_get.json()
            return dados_get_usuario
        else:
            print(f"Erro: {usuario_get.status_code}")
            return {
                "erro": usuario_get.json()
            }

    def usuarios(e):
        lv_usuario.controls.clear()
        lista_resultados = lista_usuarios()
        print(lista_resultados)

        if "error" in lista_resultados:
            print("Erro: ", lista_resultados)
        else:
            print(lista_resultados)

            for usuarios in lista_resultados ['lista_usuarios']:
                print("aa", lista_resultados)
                lv_usuario.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.PERSON),
                        title=ft.Text(f"Nome: {usuarios['Nome']}"),
                        trailing=ft.PopupMenuButton(
                            icon=ft.Icons.REMOVE_RED_EYE,
                            items=[
                                ft.PopupMenuItem(
                                    text="Informações",
                                    on_click=lambda _, l=usuarios: detalhes_usuario(l)
                                )
                            ]
                        )
                    )
                )
        page.update()

    def detalhes_usuario(usuarios):
        txt_nome.value = usuarios["Nome"]
        txt_cpf.value = usuarios["CPF"]
        txt_endereco.value = usuarios["Endereco"]
        page.update()
        page.go("/detalhes_usuario")

    def salvar_usuario(e):
        if input_nome.value == "" or input_cpf.value == "" or input_endereco.value == "" :
            page.overlay.append(msg_erro1)
            msg_erro1.open = True
            page.update()
        else:
            novo_usuario = {
                "nome" :input_nome.value,
                "cpf" :input_cpf.value,
                "endereco" :input_endereco.value,
            }
            cadastro_usuarios(novo_usuario)

    def lista_emprestimos():
        url = "http://10.135.232.24:5000/emprestimos"
        emprestimo_get = requests.get(url)
        if emprestimo_get.status_code == 200:
            dados_get_emprestimo = emprestimo_get.json()
            return dados_get_emprestimo
        else:
            print(f"Erro: {emprestimo_get.status_code}")
            return {
                "erro": emprestimo_get.json()
            }

    def emprestimos(e):
        lv_emprestimo.controls.clear()
        lista_resultados = lista_emprestimos()
        print(lista_resultados)

        if "error" in lista_resultados:
            print("Erro: ", lista_resultados)
        else:
            print(lista_resultados)

            for emprestimo in lista_resultados['lista_emprestimos']:
                print("aa", lista_resultados)
                lv_emprestimo.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.BOOK),
                        title=ft.Text(f"Data de emprestimo: {emprestimo["Data_emprestimo"]}"),
                        trailing=ft.PopupMenuButton(
                            icon=ft.Icons.REMOVE_RED_EYE,
                            items=[
                                ft.PopupMenuItem(
                                    text="Informações",
                                    on_click=lambda _, l=emprestimo: detalhes_emprestimo(l)
                                )
                            ]
                        )
                    )
                )
        page.update()

    def detalhes_emprestimo(emprestimos):
        txt_id_usuario.value = emprestimos["id_usuario"]
        txt_id_livro.value = emprestimos["id_livro"]
        txt_data_emprestimo.value = emprestimos["Data_emprestimo"]
        txt_data_devolucao.value = emprestimos["Data_devolucao"]
        page.update()
        page.go("/detalhes_emprestimo")

    def salvar_emprestimo(e):
        if input_id_usuario.value == "" or input_id_livro.value == "" or input_data_emprestimo.value == "" or input_data_devolucao.value == "":
            page.overlay.append(msg_erro1)
            msg_erro1.open = True
            page.update()
        else:
            novo_emprestimo = {
                "id_usuario" :input_id_usuario.value,
                "id_livro" :input_id_livro.value,
                "data_emprestimo" :input_data_emprestimo.value,
                "data_devolucao" :input_data_devolucao.value,
            }
            realizar_emprestimos(novo_emprestimo)
            page.update()

    def cadastro_livros(novo_livro):
        url = "http://10.135.232.24:5000/novo_livro"
        response_livro = requests.post(url, json=novo_livro)

        if response_livro.status_code == 201:
            input_titulo.value = ""
            input_autor.value = ""
            input_isbn.value = ""
            input_resumo.value = ""
            page.overlay.append(msg_sucesso1)
            msg_sucesso1.open = True
            page.update()
        else:
            page.overlay.append(msg_erro2)

    def cadastro_usuarios(novo_usuario):
        url = "http://10.135.232.24:5000/novo_usuario"
        response_usuario = requests.post(url, json=novo_usuario)

        if response_usuario.status_code == 201:
            input_nome.value = ""
            input_cpf.value = ""
            input_endereco.value = ""
            page.overlay.append(msg_sucesso3)
            msg_sucesso3.open = True
            page.update()
        else:
            page.overlay.append(msg_erro3)

    def realizar_emprestimos(novo_emprestimo):
        url = "http://10.135.232.24:5000/realizar_emprestimo"

        response_emprestimo = requests.post(url, json=novo_emprestimo)

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

    def atualiza_livro(e):
        global id_livro_global
        url = f"http://10.135.232.24:5000/atualizar_livro/{id_livro_global}"

        novo_livro = {
            "titulo": input_titulo.value,
            "autor": input_autor.value,
            "isbn": int(input_isbn.value),
            "resumo": input_resumo.value
        }
        response_put = requests.put(url, json=novo_livro)

        if response_put.status_code == 200:
            page.go("/lista_livros")
            page.update()
        else:
            return {
                'error': livros.json()
            }

    def atualiza_usuario(e):
        global id_usuario_global
        url = f"http://10.135.232.24:5000/atualizar_usuario/{id_usuario_global}"
        novo_usuario = {
            "Nome": input_nome.value,
            "CPF": input_cpf.value,
            "Endereço": input_endereco.value,
        }

        response_put = requests.put(url, json=novo_usuario)
        if response_put.status_code == 200:
            page.go("/lista_usuarios")
            page.update()
        else:
            return {
                'error': usuarios.json()
            }

    def atualiza_emprestimo(e):
        global id_emprestimo_global
        url = f"http://10.135.232.24:5000/atualizar_emprestimos/{id_emprestimo_global}"
        novo_emprestimo = {
            "id_livro": input_id_livro.value,
            "id_usuario": input_id_usuario.value,
            "data_devolucao": input_data_devolucao.value,
            "data_emprestimo": input_data_emprestimo.value,
        }

        response_put = requests.put(url, json=novo_emprestimo)
        if response_put.status_code == 200:
            page.go("/lista_emprestimos")
            page.update()
        else:
            return {
                'error': emprestimos.json()
            }

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


    input_titulo = ft.TextField(label="Título", hint_text="Digite o titulo")
    input_autor = ft.TextField(label="Autor", hint_text="Digite o autor")
    input_isbn = ft.TextField(label="ISBN", hint_text="Digite o ISBN")
    input_resumo = ft.TextField(label="Resumo", hint_text="Digite o resumo")
    lv_livro = ft.ListView(
        height=500,
    )

    txt_titulo = ft.Text()
    txt_autor = ft.Text()
    txt_isbn = ft.Text()
    txt_resumo = ft.Text()

    input_nome = ft.TextField(label="Nome", hint_text="Digite o nome")
    input_cpf = ft.TextField(label="CPF", hint_text="Digite o CPF")
    input_endereco = ft.TextField(label="endereco", hint_text="Digite o endereco")

    lv_usuario = ft.ListView(
        height=500,
    )

    txt_nome = ft.Text()
    txt_cpf = ft.Text()
    txt_endereco = ft.Text()

    input_id_usuario = ft.TextField(label="id_usuario", hint_text="Digite o id do usuario")
    input_id_livro = ft.TextField(label="id_livro", hint_text="Digite o id do livro")
    input_data_emprestimo = ft.TextField(label="data_emprestimo", hint_text="Digite o data do emprestimo")
    input_data_devolucao = ft.TextField(label="data_devolucao", hint_text="Digite o data do devolucao")
    titulo_livro = ft.Dropdown(
        label='Titulo dos livros',
        bgcolor="#896d56",
        width=350,
        filled=True,
        fill_color="#e7c18e",
        options=[
            Option('Mansao', 'Mansão'),
            Option('Verao', 'Verão'),
            Option('amor_gelato', 'Amor e gelato')
        ],
    )
    nomes_usuarios = ft.Dropdown(
        label='Nome dos usuários',
        bgcolor="#896d56",
        width = 350,
        filled=True,
        fill_color="#e7c18e",
        options=[
            Option('Julia', 'Júlia'),
            Option('Lucas', 'Lucas'),
            Option('Leticia', 'Leticia')
        ],
    )
    lv_emprestimo = ft.ListView(
        height=500,
    )

    txt_id_usuario = ft.Text()
    txt_id_livro = ft.Text()
    txt_data_emprestimo = ft.Text()
    txt_data_devolucao = ft.Text()

    msg_sucesso1 = ft.SnackBar(content=Text("Livro cadastrado com sucesso!"), bgcolor=Colors.GREEN)
    msg_sucesso2 = ft.SnackBar(content=Text("Livro editado com sucesso!"), bgcolor=Colors.GREEN)
    msg_sucesso3 = ft.SnackBar(content=Text("Usuário cadastrado com sucesso!"), bgcolor=Colors.GREEN)
    msg_sucesso4 = ft.SnackBar(content=Text("Usuário editado com sucesso!"), bgcolor=Colors.GREEN)
    msg_sucesso5 = ft.SnackBar(content=Text("Empréstimo realizado com sucesso!"), bgcolor=Colors.GREEN)

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

# arrumar options
# listar emprestimo(nomes pelo id)
# status
# historico
# arrumar cadastrar emprest imo e usuario
# termina/r atualizar