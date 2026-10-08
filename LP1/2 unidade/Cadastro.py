import flet as ft


def main(page: ft.Page):
    page.title = "Cadastro de Alunos"
    page.window.width = 500
    page.window.height = 650
    page.padding = 30

    nome = ft.TextField(
        label="Nome completo",
        hint_text="Digite o nome do aluno",
    )

    matricula = ft.TextField(
        label="Matrícula",
        hint_text="Digite a matrícula",
    )

    idade = ft.TextField(
        label="Idade",
        hint_text="Digite a idade",
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    turma = ft.Dropdown(
        label="Turma",
        options=[
            ft.DropdownOption(key="1", text="1º Ano"),
            ft.DropdownOption(key="2", text="2º Ano"),
            ft.DropdownOption(key="3", text="3º Ano"),
        ],
    )

    curso = ft.Dropdown(
        label="Curso",
        options=[
            ft.DropdownOption(key="informatica", text="Informática"),
            ft.DropdownOption(key="administracao", text="Administração"),
            ft.DropdownOption(key="agropecuaria", text="Agropecuária"),
        ],
    )

    mensagem = ft.Text()

    def cadastrar(e):
        mensagem.value = f"Aluno {nome.value} cadastrado com sucesso!"
        mensagem.color = ft.Colors.GREEN
        page.update()

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Cadastro de Alunos",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    "Preencha os dados abaixo",
                    size=16,
                ),

                nome,
                matricula,

                ft.Row(
                    controls=[
                        idade,
                        turma,
                    ],
                    spacing=10,
                ),

                curso,

                ft.Button(
                    content="Cadastrar aluno",
                    icon=ft.Icons.PERSON_ADD,
                    on_click=cadastrar,
                ),

                mensagem,
            ],
            spacing=15,
        )
    )



ft.run(main)
