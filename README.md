# Tutorial de Instalação e Execução de uma Aplicação Desktop Python

A aplicação Estoque tem o objetivo ajudar no gerenciamento de estoque de uma fábrica.

## Como rodar a aplicação? 
A instalação dos requisitos necessários e a execução de uma aplicação desktop Python. 
A aplicação em questão utiliza bibliotecas para a interface gráfica, calendário e conexão com banco de dados local SQLite. 

## Pré-requisitos

Antes de iniciar, é necessário que você tenha o Python instalado em seu sistema. 
Este tutorial está utilizando Python 3.6 ou superior. Você pode verificar a versão do Python instalada executando o seguinte comando no terminal ou prompt de comando:

```bash
python --version
```
## Instalação das Bibliotecas Necessárias
```bash
pip install tk Pillow tkcalendar
```
## Executar aplicação
```bash
python main.py
```


## Estrutura dos arquivos do projeto
```
ESTOQUE/
│
├── .vscode/
│   └── settings.json
├── __pycache__/
│   └── view.cpython-312.pyc
├── README.md
├── criarbd.py
├── dados.db
├── main.py
├── view.py
├── add.png
├── atualizar.png
├── deletar.png
└── inventorio.png
```
- ESTOQUE/: Nome do diretório raiz do projeto.
- .vscode/: Diretório que contém configurações específicas do editor VSCode.
- settings.json: Arquivo de configurações do editor VSCode.
- __pycache__/: Diretório que armazena os arquivos de bytecode compilados que o Python cria para acelerar o tempo de inicialização dos scripts.
- view.cpython-312.pyc: Bytecode compilado para Python 3.12 do módulo view.py.
- README.md: Arquivo Markdown contendo informações sobre o projeto, como um manual ou documentação.
- criarbd.py: Script Python possivelmente usado para criar a base de dados.
- dados.db: Arquivo de banco de dados SQLite.
- main.py: Arquivo Python que provavelmente é o ponto de entrada da aplicação.
- view.py: Arquivo Python que contém a lógica de interface do usuário.
- add.png: Imagem que pode ser usada como ícone de adição na interface.
- atualizar.png: Imagem que pode ser usada como ícone para atualizar informações na interface.
- deletar.png: Imagem que pode ser usada como ícone para deletar ou remover itens na interface.
- inventorio.png: Imagem que pode ser usada na interface, possivelmente relacionada à visualização do inventário.
