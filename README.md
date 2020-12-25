# crud-cliente

###Este repositório tem como objetivo cumprir o desafio técnico proposto pela empresa como processo seletivo para vaga de Python.

Tecnologias utilizadas:

- Django==3.1.2
- Python 3.8.2
* Para rodar o projeto:

1. abrir o diretório do projeto no terminal do computador;
1. ativar a virtualenv (```cd .venv\Scripts\activate```);
1. voltar ao diretório principal do projeto e executar o comando ```python manage.py runserver```;
1. copiar o link que aparece (http://127.0.0.1:8000/) e colar no navegador.

* Lógica do Projeto:

Para acessar os clientes cadastrados é necessário ter um login registrado. Caso ainda não possua, no próprio sistema é possível registrar-se.
Ao entrar, é possível cadastrar (CREATE) um cliente no menu "Cadastrar". Ao realizar o cadastro, você será redirecionado à página inicial e poderá ler (READ) as informações dos clientes na ordem do mais atual ao mais antigo cadastrado.
Ao lado dos dados, no ícone de lixeira é possível deletar aquele cliente (DELETE) e, no ícone de pincel, é possível editar os dados do mesmo (UPDATE), finalizando assim o CRUD básico.
Para sair do sistema, basta clicar no menu "Sair".