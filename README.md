# Sistema de Gerenciamento de Produtos
Este projeto consiste em uma aplicação web para gerenciamento de produtos, desenvolvida com Django. A aplicação permite o cadastro de produtos através do painel administrativo do Django e a exibição destes em uma interface simples e funcional.

## https://estoque-ross.onrender.com/

## Características Principais
- **Página Principal**: Exibe uma tabela com todos os produtos cadastrados, contendo nome, preço e quantidade em estoque
- **Página de Produto Individual**: Cada produto possui uma página própria com detalhes completos
- **Área de Contato**: Formulário de exemplo (não armazena dados)
- **Painel Administrativo**: Interface Django Admin para cadastro e gerenciamento de produtos
- **Tratamento de Erros**: Templates personalizados para erros 404 e 500
## Tecnologias Utilizadas
- Django
- HTML/CSS
- Python
## Instalação
1. Clone o repositório:
```bash
git clone https://github.com/DouglasEng/estoque-django.git
cd estoque-django
```
2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Execute as migrações:
```bash
python manage.py migrate
```
5. Crie um superusuário para acessar o painel administrativo:
```bash
python manage.py createsuperuser
```
6. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```
7. Acesse a aplicação em: http://127.0.0.1:8000/
## Uso
### Visualizando Produtos
- Acesse a página principal para ver todos os produtos cadastrados
- Clique no nome de qualquer produto para ver detalhes completos em uma página individual
### Administração
- Acesse o painel admin em: http://127.0.0.1:8000/experience/
- Faça login com as credenciais do superusuário
- No painel, você pode adicionar, editar e remover produtos
### Área de Contato
- A página de contato possui um formulário para demonstração (não funcional para envio)

## Personalização
Para personalizar este projeto para suas necessidades:
1. Modifique o modelo de produto em `core/models.py` para incluir os campos desejados
2. Atualize os templates na pasta `templates/` para alterar o layout e aparência
3. Expanda a funcionalidade de contato em `core/views.py` se deseja implementar envio real de mensagens
