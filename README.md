# seleniumPy-downloadCSV
# WebSrapping - Download Diário e Automático de uma Base de Dados em CSV do Site da Empresa para o Servidor Local

Este projeto consiste em um script que realiza o download diário e automático de uma base de dados em formato CSV do site da empresa e a salva no servidor local. Esse download é necessário para atualizar as informações da base de dados local.

## Funcionalidades

- O script faz o download automático da base de dados em CSV do site da empresa
- O download é realizado diariamente em um horário pré-determinado
- Os dados são salvos no servidor local para atualização da base de dados local

## Como Usar

1. Clone este repositório em seu servidor local;
2. Configure as informações de acesso ao site da empresa no arquivo `csv.py`;
3. Configure as informações de acesso ao servidor local no arquivo `csv.py`;
4. Configure o horário de download no arquivo;
5. Execute o script `csv.py` e depois o agende no Agendador de Tarefas com o horário de interesse;

## Dependências

- Python 3.10 ou superior
- Bibliotecas Python: Selenium e Time
