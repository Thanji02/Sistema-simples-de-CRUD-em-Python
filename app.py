from db import get_conn, init_db
from models import Contato

#Criar o contato
def criar_contato(nome: str, email: str, telefone: str) -> int:
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO contatos (nome, email, telefone) VALUES (?, ?, ?)",
            (nome, email, telefone)
        )
        return cur.lastrowid


#Listar os contatos
def listar_contatos():
    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM contatos ORDER BY id")
        return [dict(r) for r in cur.fetchall()]


#Buscar contato por ID
def buscar_por_id(contato_id: int):
    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM contatos WHERE id = ?", (contato_id,))
        r = cur.fetchone()
        return dict(r) if r else None


#Atualizar contato
def atualizar_contato(contato_id: int, nome: str, email: str, telefone: str) -> bool:
    with get_conn() as conn:
        cur = conn.execute(
            "UPDATE contatos SET nome = ?, email = ?, telefone = ? WHERE id = ?",
            (nome, email, telefone, contato_id)
        )
        return cur.rowcount > 0


#Deletar contato
def deletar_contato(contato_id: int) -> bool:
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM contatos WHERE id = ?", (contato_id,))
        return cur.rowcount > 0


# Menu de opções
def menu():
    print("\n=== Cadastro de Contatos (SQLite) ===")
    print("1) Criar contato")
    print("2) Listar contatos")
    print("3) Buscar por ID")
    print("4) Atualizar contato")
    print("5) Deletar contato")
    print("0) Sair")


# Função principal
def main():
    init_db()
    while True:
        menu()
        opc = input("Escolha: ").strip()
        if opc == "1":
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            telefone = input("Telefone: ").strip()
            try:
                new_id = criar_contato(nome, email, telefone)
                print(f"✅ Contato criado com ID {new_id}")
            except Exception as e:
                print(f"❌ Erro ao criar contato: {e}")
        elif opc == "2":
            contatos = listar_contatos()
            if not contatos:
                print("Nenhum contato encontrado.")
            for c in contatos:
                print(f"[{c['id']}] {c['nome']} | {c['email']} | {c['telefone']} | {c['criado_em']}")
        elif opc == "3":
            cid = int(input("ID: "))
            c = buscar_por_id(cid)
            print(c if c else "Não encontrado.")
        elif opc == "4":
            cid = int(input("ID para atualizar: "))
            nome = input("Novo nome: ").strip()
            email = input("Novo email: ").strip()
            telefone = input("Novo telefone: ").strip()
            ok = atualizar_contato(cid, nome, email, telefone)
            print("✅ Atualizado." if ok else "❌ ID não encontrado.")
        elif opc == "5":
            cid = int(input("ID para deletar: "))
            ok = deletar_contato(cid)
            print("✅ Deletado." if ok else "❌ ID não encontrado.")
        elif opc == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()