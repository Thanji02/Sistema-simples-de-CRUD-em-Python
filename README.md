# 📘 Cadastro de Contatos – CRUD em Python + SQLite

Um **CRUD de contatos** feito na unha, usando **Python** (padrão da linguagem) e **SQLite** (integrado ao Python via `sqlite3`, sem instalar nada).  
Ideal para praticar **manipulação de dados**, **boas práticas de código** e **organização de projeto**.

---

## ✨ Destaques

- 🧱 **CRUD completo**: criar, listar, buscar por ID, atualizar e deletar  
- 🔎 **Busca por nome ou e-mail** (LIKE)  
- 🔐 **Validações**: e-mail (regex) e telefone (8–15 dígitos)  
- 🗄️ **SQLite** local (arquivo `.db` criado automaticamente)  
- 🧰 **Zero dependências externas** (só biblioteca padrão)  
- 🧪 Pronto para evoluir: CSV, API REST (FastAPI), GUI (Tkinter) e testes

---

## 🗂 Estrutura

```

cadastro\_contatos/
├── app.py        # CLI (menu e fluxo principal)
├── db.py         # Operações no SQLite (CRUD + busca + init)
├── models.py     # Dataclass Contato
└── utils.py      # Validações (e-mail e telefone)

````

> O banco `cadastro.db` é criado na primeira execução, ao lado dos arquivos.

---

## 🚀 Como executar

```bash
# 1) Clone o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPO.git

# 2) Entre na pasta
cd cadastro_contatos

# 3) Rode a aplicação
python app.py
# ou
python3 app.py
````

Você verá um menu no terminal:

    === Cadastro de Contatos (SQLite) ===
    1) Criar contato
    2) Listar contatos
    3) Buscar por ID
    4) Atualizar contato
    5) Deletar contato
    6) Buscar por nome/email
    0) Sair

***

## 🧪 Teste rápido (roteiro)

1.  **Criar** um contato (opção 1)
    *   Nome: `Ana Maria`
    *   Email: `ana@example.com`
    *   Telefone: `11987654321`
2.  **Listar** (opção 2) → confira o registro
3.  **Buscar por ID** (opção 3) → use o ID mostrado
4.  **Atualizar** (opção 4) → altere telefone/e-mail
5.  **Deletar** (opção 5) → remova e verifique
6.  **Buscar por nome/e-mail** (opção 6) → teste com “ana” ou “@example”

> Dica: tente criar um contato com **e-mail repetido** para ver o tratamento do `UNIQUE`.

***

## 🧠 Detalhes técnicos

**Tabela:** `contatos(id, nome, email, telefone, criado_em)`

*   `id` → `INTEGER PRIMARY KEY AUTOINCREMENT`
*   `email` → `UNIQUE NOT NULL`
*   `criado_em` → `TIMESTAMP DEFAULT CURRENT_TIMESTAMP`

**Validações:**

*   `email`: regex simples para formato padrão
*   `telefone`: 8 a 15 dígitos (ignora separadores)

***

## 🧭 Roadmap (ideias de evolução)

*   [ ] Exportar **CSV** (listagem → `contatos.csv`)
*   [ ] **Paginação** na listagem (ex.: 10 por página)
*   [ ] **Testes unitários** com `unittest/pytest`
*   [ ] **API REST** com **FastAPI** reaproveitando `db.py`
*   [ ] Interface **Tkinter** (desktop) ou **Flask/FastAPI** (web)
*   [ ] Busca avançada (telefone, intervalo de datas, ordenação)

***

## 🧹 .gitignore sugerido

> Para evitar subir cache do Python, ambientes virtuais e o banco `.db`.

    __pycache__/
    *.pyc
    *.pyo
    *.pyd
    *.py[cod]
    .venv/
    venv/
    *.db
    .vscode/

> Adicione, depois:
>
> ```bash
> git add .gitignore
> git commit -m "Add .gitignore"
> git push
> ```

***

## 🤝 Contribuições

Sinta-se à vontade para abrir **Issues** e enviar **PRs**.  
Sugestões de features e melhorias são super bem-vindas!

***

## 🪪 Licença

Este projeto está sob a licença **MIT**.  
Crie um arquivo `LICENSE` ou escolha um template no GitHub se desejar.

***

## 📸 (Opcional) Imagem/GIF de demonstração

> Coloque aqui um print da CLI ou um GIF curto.

    docs/cli-demo.png

***

## 📬 Contato

*   **Autor:** Nathan Miyasaki | 
*   **Linkedln:** https://www.linkedin.com/in/nathan-miyasaki/

***




