# 📌 Django_session - Sistema de Autenticação com Django

## 📖 Visão Geral
**Django_session** é um sistema de autenticação de usuários desenvolvido com **Django 5.1.6**. Ele permite que usuários realizem cadastro, login seguro e gerenciamento de sessão. O projeto utiliza **PostgreSQL** como banco de dados, armazenamento seguro da `SECRET_KEY` via **`.env`** e hash de senhas com **SHA-256**.

## 🚀 Funcionalidades
- Cadastro de usuários
- Login e autenticação
- Gerenciamento de sessão
- Hash seguro de senhas
- Redirecionamento baseado na autenticação

## 📂 Estrutura do Projeto

```bash
Django_session/
├── manage.py          # Gerenciador do Django
├── setup/             # Configurações do projeto
│   ├── settings.py    # Configurações globais
│   ├── urls.py        # Mapeamento de URLs
│   ├── wsgi.py        # Configuração para WSGI
│   ├── asgi.py        # Configuração para ASGI
├── usuarios/          # App de autenticação de usuários
│   ├── models.py      # Definição dos modelos de dados
│   ├── views.py       # Lógica das views
│   ├── urls.py        # URLs do app
│   ├── templates/     # Templates HTML
├── plataforma/        # App principal
├── templates/         # Templates base
├── .env               # Variáveis de ambiente
├── requirements.txt   # Dependências do projeto
```

## 🛠️ Tecnologias Utilizadas
- **Django 5.1.6**
- **Python 3.12**
- **PostgreSQL**
- **Bootstrap 5.3** (para estilização)
- **python-dotenv** (para variáveis de ambiente)

## 📝 Instalação e Configuração

### 1️⃣ **Clonar o repositório**
```bash
git clone https://github.com/seu-usuario/django_session.git
cd django_session
```

### 2️⃣ **Criar e ativar um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️⃣ **Instalar as dependências**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Configurar o arquivo `.env`**
Crie um arquivo `.env` e adicione a sua chave secreta:
```env
SECRET_KEY="sua_secret_key"
```

### 5️⃣ **Configurar o banco de dados**
Edite `settings.py` para definir suas credenciais do PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_session',
        'USER': 'postgres',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Crie as tabelas no banco:
```bash
python manage.py migrate
```

### 6️⃣ **Criar superusuário (opcional)**
```bash
python manage.py createsuperuser
```

### 7️⃣ **Executar o servidor**
```bash
python manage.py runserver
```
Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🔗 Rotas Disponíveis
| Rota | Método | Descrição |
|------|--------|-----------|
| `/auth/login/` | GET | Página de login |
| `/auth/cadastro/` | GET | Página de cadastro |
| `/auth/valida_cadastro/` | POST | Validação do cadastro |
| `/auth/valida_login/` | POST | Validação do login |
| `/auth/sair/` | GET | Logout do usuário |
| `/plataforma/home/` | GET | Página inicial após login |

## 🛡️ Segurança
✅ **Senhas criptografadas** com SHA-256 antes de serem armazenadas.  
✅ **Variáveis sensíveis protegidas** no `.env`.  
✅ **Proteção contra ataques CSRF** com `{% csrf_token %}` nos formulários.

## 🎯 Melhorias Futuras
- Implementar reset de senha
- Adicionar autenticação por e-mail
- Criar testes automatizados

## 📜 Licença
Este projeto é de código aberto e pode ser modificado conforme necessário. 🚀

