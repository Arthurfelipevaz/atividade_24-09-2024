# Documentação do Sistema de Gerenciamento de Clientes e Cidades

## Visão Geral

Este projeto é um sistema de gerenciamento de clientes e cidades desenvolvido em Python, utilizando a biblioteca Tkinter para a interface gráfica. O sistema é composto por diversas funcionalidades que permitem o gerenciamento de dados de clientes, cidades e usuários, com operações de CRUD (Create, Read, Update, Delete) para cada uma dessas entidades.

## Estrutura do Projeto

O projeto é dividido em várias partes principais:

1. **Banco de Dados (SQLite)**:
   - O sistema utiliza SQLite como banco de dados. O banco é gerenciado pela classe `Banco`, que cria e mantém as tabelas necessárias: `usuarios`, `cidade` e `cliente`.
   - A tabela `usuarios` armazena informações sobre os usuários que acessam o sistema.
   - A tabela `cidade` armazena as cidades disponíveis para cadastro de clientes, com informações sobre o nome da cidade e a unidade federativa (UF).
   - A tabela `cliente` contém os dados dos clientes, incluindo um relacionamento com a tabela `cidade` por meio do campo `idcid`.

2. **Interface Gráfica (Tkinter)**:
   - A interface gráfica foi desenvolvida utilizando a biblioteca Tkinter, oferecendo uma maneira intuitiva para os usuários interagirem com o sistema.
   - O sistema possui três módulos principais, cada um responsável por uma entidade específica: usuários, clientes e cidades.

3. **Arquivos do Projeto**:
   - **`banco.py`**: Contém a classe `Banco`, responsável pela conexão com o banco de dados e pela criação das tabelas.
   - **`appusu.py`**: Implementa a interface para o cadastro e gerenciamento de usuários.
   - **`appcli.py`**: Implementa a interface para o cadastro e gerenciamento de clientes.
   - **`appcid.py`**: Implementa a interface para o cadastro e gerenciamento de cidades.
   - **`usuarios_model.py`**: Contém a classe `Usuario`, que gerencia as operações de CRUD na tabela `usuarios`.
   - **`clientes.py`** e **`cidades.py`**: Classes responsáveis pelas operações de CRUD nas tabelas `cliente` e `cidade`, respectivamente.

## Funcionalidades

### 1. **Cadastro e Gerenciamento de Usuários** (`appusu.py`)
   - **Buscar Usuário**: Permite buscar um usuário pelo seu ID e exibe as informações associadas.
   - **Inserir Usuário**: Insere um novo usuário no banco de dados.
   - **Alterar Usuário**: Permite alterar as informações de um usuário existente.
   - **Excluir Usuário**: Remove um usuário do banco de dados.

### 2. **Cadastro e Gerenciamento de Clientes** (`appcli.py`)
   - **Buscar Cliente**: Permite buscar um cliente pelo seu ID e exibe as informações associadas.
   - **Inserir Cliente**: Insere um novo cliente no banco de dados, associando-o a uma cidade existente.
   - **Alterar Cliente**: Permite alterar as informações de um cliente existente.
   - **Excluir Cliente**: Remove um cliente do banco de dados.

### 3. **Cadastro e Gerenciamento de Cidades** (`appcid.py`)
   - **Buscar Cidade**: Permite buscar uma cidade pelo seu ID e exibe as informações associadas.
   - **Inserir Cidade**: Insere uma nova cidade no banco de dados.
   - **Alterar Cidade**: Permite alterar as informações de uma cidade existente.
   - **Excluir Cidade**: Remove uma cidade do banco de dados.

## Relacionamentos

- **Clientes e Cidades**: Cada cliente está associado a uma cidade, o que estabelece uma relação de chave estrangeira entre as tabelas `cliente` e `cidade`. Isso permite que o sistema mantenha a integridade dos dados ao garantir que cada cliente esteja vinculado a uma cidade válida.

## Fluxo de Trabalho

1. **Iniciar a Aplicação**: O usuário pode abrir a aplicação e escolher entre os módulos de gerenciamento de usuários, clientes ou cidades.
2. **Operações de CRUD**: Dentro de cada módulo, o usuário pode realizar operações de busca, inserção, alteração e exclusão de dados.
3. **Salvamento e Atualização**: As alterações feitas são salvas no banco de dados SQLite e podem ser consultadas ou alteradas posteriormente.

## Conclusão

Este sistema oferece uma solução completa para o gerenciamento de dados de clientes, cidades e usuários, com uma interface gráfica amigável e um banco de dados robusto. Ele é ideal para aplicações que necessitam de um controle eficiente sobre essas entidades, garantindo a integridade e acessibilidade dos dados.
