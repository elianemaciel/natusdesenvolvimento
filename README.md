# Projeto Django - Natus Desenvolvimento Humano

Este repositório contém um projeto desenvolvido em Django para a empresa **Natus Desenvolvimento Humano**. O objetivo do sistema é fornecer uma plataforma robusta para gerenciamento de conteúdo, eventos e interações com clientes.

## 📌 Funcionalidades
- Gerenciamento de usuários e autenticação
- Cadastro e administração de eventos
- Painel administrativo personalizado

## 🛠 Tecnologias Utilizadas
- **Django** (Backend)
- **HTML, CSS, JavaScript** (Frontend)

## 🚀 Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/seuusuario/natus-django.git
   cd natus-django
   ```

2. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```

5. Crie um superusuário para acessar o painel administrativo:
   ```sh
   python manage.py createsuperuser
   ```

6. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```

## 📜 Como Usar

1. Acesse o sistema em `http://127.0.0.1:8000/`
2. Utilize o painel administrativo em `http://127.0.0.1:8000/admin/`
3. Configure eventos, usuários e demais funcionalidades conforme necessidade

## 🤝 Contribuição
Para sugerir melhorias, abra uma **issue** ou envie um **pull request**.

## 📄 Licença
Este projeto é de propriedade da **Natus Desenvolvimento Humano** e não deve ser compartilhado sem permissão.

