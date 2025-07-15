import customtkinter as ctk
import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def sqlite_defaults():
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        concluida INTEGER NOT NULL DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()

def open_add_window():
    logging.info('OPEN_ADD_WINDOW OPEN')
    add_window_gui()

def add_window_gui():
    add_window = ctk.CTkToplevel(main_window)
    add_window.title("Add To-Do")
    add_window.iconbitmap("./docs/ico.ico")
    add_window.configure(fg_color="#1e1e1e")
    add_window.geometry("425x330")
    add_window.maxsize(425, 330)
    add_window.minsize(425, 330)

    label_add_title = ctk.CTkLabel(
        add_window,
        text="Adicionar Tarefa",
        font=("Segoe UI", 20, "bold"),
        text_color="#FFFFFF"
    )
    label_add_title.place(x=120, y=20)

    entry_add_title = ctk.CTkEntry(
        add_window,
        placeholder_text="Título",
        width=380,
        height=35,
        font=("Segoe UI", 14)
    )
    entry_add_title.place(x=20, y=80)

    entry_add_description = ctk.CTkEntry(
        add_window,
        placeholder_text="Descrição",
        width=380,
        height=100,
        font=("Segoe UI", 13)
    )
    entry_add_description.place(x=20, y=130)

    button_add = ctk.CTkButton(
        add_window,
        text="add",
        width=20,
        height=40,
        corner_radius=20,
        fg_color="#0083CF",
        hover_color="#0079BE",
        text_color="#ffffff",
        font=("Segoe UI", 20, "bold"),
        command=lambda: insert_task_to_db(
            entry_add_title.get(),
            entry_add_description.get(),
            add_window
        )
    )
    button_add.place(x=20, y=250)

    add_window.grab_set()

def window_gui():
    global main_window, task_frame
    main_window = ctk.CTk()
    main_window.title("To-Do List")
    main_window.configure(fg_color="#1e1e1e")
    main_window.geometry("340x423")
    main_window.iconbitmap("./docs/ico.ico")
    main_window.maxsize(340, 423)
    main_window.minsize(340, 423)

    label_title = ctk.CTkLabel(
        main_window,
        text="My To-Do List",
        font=("Segoe UI", 20, "bold"),
        text_color="#FFFFFF"
    )
    label_title.place(x=20, y=20)

    add_function_button = ctk.CTkButton(
        main_window,
        text="+",
        width=20,
        height=20,
        corner_radius=20,
        fg_color="#00A2FF",
        hover_color="#008CDD",
        text_color="#1e1e1e",
        font=("Segoe UI", 18, "bold"),
        command=open_add_window
    )
    add_function_button.place(x=290, y=20)

    task_frame = ctk.CTkScrollableFrame(
        main_window,
        fg_color="#2e2e2e",
        width=290,
        height=330
    )
    task_frame.place(x=20, y=70)

    show_tasks()

    main_window.mainloop()

def insert_task_to_db(title, description, window):
    logging.info('insert_task_to_db')
    if title.strip() == "" or description.strip() == "":
        logging.warning('title & description = nothing')
        return
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tarefas (descricao) VALUES (?)",
        (f"{title}:  {description}",)
    )
    conn.commit()
    conn.close()
    logging.info(f'TASK ADDED task: {title}')
    show_tasks()
    window.destroy()

def fetch_all_tasks():
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, descricao, concluida FROM tarefas")
    tasks = cursor.fetchall()  
    conn.close()
    return tasks

def show_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    tasks = fetch_all_tasks()

    for i, (task_id, descricao, concluida) in enumerate(tasks):
        var = ctk.BooleanVar(value=bool(concluida))
        text_color = "#808080" if var.get() else "#ffffff"
        task_container = ctk.CTkFrame(
            task_frame,
            fg_color="transparent"
        )
        task_container.grid(row=i, column=0, padx=10, pady=(5, 0), sticky="w")

        check = ctk.CTkCheckBox(
            task_container,
            text=descricao,
            font=("Segoe UI", 14),
            text_color=text_color,
            variable=var,
            onvalue=1,
            offvalue=0,
            width=220  # limita largura pra evitar quebra maluca
        )
        check.pack(side="left", fill="both", expand=True)

        delete_btn = ctk.CTkButton(
            task_container,
            text="❌",
            fg_color="#2e2e2e",
            hover_color="#3a3a3a",
            text_color="#a70000",
            font=("Segoe UI", 16, "bold"),
            width=30,
            height=30,
            corner_radius=5,
            command=lambda id=task_id: delete_task(id)
        )
        delete_btn.pack(side="right", padx=(5, 0))

def on_check(var, task_id):
    estado = var.get()
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tarefas SET concluida = ? WHERE id = ?",
        (int(estado), task_id)
    )
    conn.commit()
    conn.close()
    logging.info(f"Tarefa {task_id} atualizada para concluída = {estado}")
    show_tasks()

def delete_task(task_id):
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    logging.info(f'Tarefa {task_id} deletada')
    show_tasks()

sqlite_defaults()
window_gui()
