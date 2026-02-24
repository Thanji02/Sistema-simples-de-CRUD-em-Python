Cadastro de Contatos – CRUD em Python + SQLite
-------------------------------------------------------------
Um sistema simples de CRUD (Create, Read, Update, Delete) criado em Python puro, usando SQLite como banco de dados local.
O objetivo é treinar manipulação de dados, organização de projeto e uso da biblioteca sqlite3.
-------------------------------------------------------------


🚀 Tecnologias utilizadas
-------------------------------------------------------------
Python 3.x
SQLite (builtin — não precisa instalar nada)
Dataclasses
Regex para validações
CLI (Command Line Interface)
-------------------------------------------------------------


📂 Estrutura do projeto
-------------------------------------------------------------
cadastro_contatos/
├── app.py        # Interface do usuário (menu e fluxo principal)
├── db.py         # Funções de banco de dados (CRUD + busca)
├── models.py     # Dataclass Contato
└── utils.py      # Validações de email e telefone
-------------------------------------------------------------


⚙️ Como executar
-------------------------------------------------------------
Clone o repositório:
Shellgit clone https://github.com/SEU_USUARIO/NOME_DO_REPO.gitMostrar mais linhas
-------------------------------------------------------------


Entre na pasta:
-------------------------------------------------------------
Shellcd cadastro_contatosMostrar mais linhas
-------------------------------------------------------------


Execute o programa:
-------------------------------------------------------------
Shellpython app.pyMostrar mais linhas
ou:
Shellpython3 app.pyMostrar mais linhas
-------------------------------------------------------------
Não é necessário instalar dependências — tudo usa biblioteca padrão do Python.


📋 Funcionalidades
-------------------------------------------------------------
➕ Criar novo contato
📄 Listar todos os contatos
🔍 Buscar contato por ID
✏️ Atualizar nome, email e telefone
🗑️ Excluir um contato
🔎 Buscar por nome ou email (usando LIKE)
🔐 Validação de:
- Email (regex)
- Telefone (8–15 dígitos)
-------------------------------------------------------------


🗄️ Banco de Dados
-------------------------------------------------------------
O arquivo cadastro.db é criado automaticamente na primeira execução.
Tabela utilizada:
-------------------------------------------------------------


🧩 Próximas melhorias (ideias)
-------------------------------------------------------------
Exportar contatos para CSV
Interface gráfica com Tkinter
API REST com FastAPI
Paginação na listagem
Deletar múltiplos contatos
Testes unitários (unittest)
-------------------------------------------------------------

-------------------------------------------------------------
📜 Licença
Este projeto é livre para estudo e modificação.
-------------------------------------------------------------
