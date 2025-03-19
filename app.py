import sqlite3

def adicionar_lembrete(descricao, horario):
    conn = sqlite3.connect("care_assistant.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lembretes (descricao, horario) VALUES (?, ?)", (descricao, horario))
    conn.commit()
    conn.close()
    print("✅ Lembrete adicionado com sucesso!")

def listar_lembretes():
    conn = sqlite3.connect("care_assistant.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lembretes")
    lembretes = cursor.fetchall()
    conn.close()

    if not lembretes:
        print("⚠️ Nenhum lembrete encontrado.")
    else:
        print("\n📌 Lembretes:")
        for lembrete in lembretes:
            print(f"🆔 {lembrete[0]} - {lembrete[1]} às {lembrete[2]}")

def excluir_lembrete(id_lembrete):
    conn = sqlite3.connect("care_assistant.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lembretes WHERE id = ?", (id_lembrete,))
    conn.commit()
    conn.close()
    print("🗑️ Lembrete excluído!")

# Menu interativo no terminal
def menu():
    while True:
        print("\n===== Care Assistant =====")
        print("1️⃣ Adicionar lembrete")
        print("2️⃣ Listar lembretes")
        print("3️⃣ Excluir lembrete")
        print("4️⃣ Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição do lembrete: ")
            horario = input("Horário (ex: 14:30): ")
            adicionar_lembrete(descricao, horario)

        elif opcao == "2":
            listar_lembretes()

        elif opcao == "3":
            id_lembrete = input("Informe o ID do lembrete para excluir: ")
            excluir_lembrete(id_lembrete)

        elif opcao == "4":
            print("👋 Saindo... Até mais!")
            break

        else:
            print("⚠️ Opção inválida, tente novamente!")

# Executar o menu
if __name__ == "__main__":
    menu()
