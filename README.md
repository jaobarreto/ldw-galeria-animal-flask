# README - Galeria de Gatinhos com Flask

## 📝 Descrição do Projeto

A **Galeria de Gatinhos** é uma aplicação web desenvolvida em Flask que permite:
- Fazer upload de fotos de gatinhos
- Armazenar informações no banco de dados (SQLite)
- Visualizar todas as imagens em uma galeria responsiva
- Gerenciar um álbum virtual de animais fofos

## 🛠 Tecnologias Utilizadas

- Python 3.x
- Flask (microframework web)
- SQLAlchemy (ORM para banco de dados)
- SQLite (banco de dados embutido)
- Bootstrap 5 (estilização e layout responsivo)
- Jinja2 (templating HTML)

## ⚙️ Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:
- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Git (opcional, para controle de versão)

## 🚀 Como Executar o Projeto

### 1. Clone o repositório (ou baixe os arquivos)

```bash
git clone https://github.com/seu-usuario/ldw-galeria-animal-flask.git
cd ldw-galeria-animal-flask
```

### 2. Configure o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o ambiente

Crie um arquivo `.env` na raiz do projeto com:

```env
SECRET_KEY=sua_chave_secreta_aqui
FLASK_DEBUG=True
FLASK_RUN_PORT=4000
FLASK_RUN_HOST=0.0.0.0
```

### 5. Execute a aplicação

```bash
python app.py
```

Ou:

```bash
flask run
```

### 6. Acesse a aplicação

Abra seu navegador e acesse:
```
http://localhost:4000
```

## 🌟 Funcionalidades

### Página Inicial
- Visualização de todos os gatinhos cadastrados
- Layout em grid responsivo
- Exibição de título e descrição de cada imagem

### Upload de Imagens
- Formulário para envio de novas fotos
- Validação de tipos de arquivo (apenas imagens)
- Armazenamento seguro no sistema de arquivos
- Registro no banco de dados

## 📂 Estrutura do Projeto

```
ldw-galeria-animal-flask/
├── .env                    # Configurações de ambiente
├── .gitignore
├── app.py                  # Aplicação principal Flask
├── config.py               # Configurações do projeto
├── requirements.txt        # Dependências do projeto
├── static/
│   ├── uploads/            # Pasta para armazenar as imagens
│   ├── css/                # Estilos CSS 
│   └── js/                 # JavaScript
└── templates/
    ├── base.html           # Template base
    ├── index.html          # Página inicial/galeria
    └── upload.html         # Página de upload
```

## 🔧 Personalização

Você pode facilmente personalizar:
- **Tema**: Alterando as cores no `base.html`
- **Banco de dados**: Modificando `DATABASE_URL` no `.env`
- **Tipos de arquivo permitidos**: Editando `ALLOWED_EXTENSIONS` no `.env`

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
