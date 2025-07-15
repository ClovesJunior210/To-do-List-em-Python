# 📝 To-Do List App

Aplicativo de lista de tarefas desenvolvido em **Python**, utilizando **CustomTkinter** para a interface gráfica e **SQLite** como banco de dados local.

---

## 📌 Status do Projeto

**Em desenvolvimento.**  
A aplicação está funcional, porém com ajustes e melhorias em andamento.

---

## ⚙️ Funcionalidades

- Adição de tarefas com título e descrição;
- Remoção de tarefas individualmente;
- Armazenamento persistente com banco de dados SQLite;
- Interface gráfica moderna com CustomTkinter.

---

## 🐞 Bugs Conhecidos

- Quando o **texto da tarefa é muito extenso**, o botão de deletar pode **desaparecer da interface**;
- Se o usuário tentar adicionar uma tarefa **sem título ou descrição**, a tarefa **não é adicionada**, mas **nenhuma mensagem é exibida**.

---

## 💡 Melhorias Futuras

- Exibição de mensagens de erro ao usuário em casos de entrada inválida;
- Melhor adaptação do layout para textos longos;
- Implementação da funcionalidade de editar tarefas;
- Suporte a modo escuro e claro de forma automática.

---

## 📦 Requisitos

- Python 3.x  
- Biblioteca `customtkinter`  
- Módulo `sqlite3` (disponível por padrão com Python)

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repo.git

# Acesse a pasta do projeto
cd seu-repo

# Instale as dependências necessárias
pip install customtkinter

# Execute o arquivo principal
python main.py
