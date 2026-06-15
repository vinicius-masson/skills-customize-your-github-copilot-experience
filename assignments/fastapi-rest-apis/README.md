# 📘 Tarefa: Construindo APIs REST com FastAPI

## 🎯 Objective

Construa uma API REST usando o framework FastAPI em Python. Nesta tarefa, você criará endpoints para gerenciar recursos, entenderá rotas HTTP, parâmetros de consulta, validação de dados e documentação automática.

## 📝 Tasks

### 🛠️ 1. Criar endpoints principais

#### Descrição
Implemente uma API que permita criar, listar, exibir e excluir itens de uma coleção simples, como tarefas ou produtos.

#### Requisitos
O programa completo deve:

- Definir um aplicativo FastAPI com pelo menos quatro rotas:
  - `GET /items`
  - `GET /items/{item_id}`
  - `POST /items`
  - `DELETE /items/{item_id}`
- Usar um modelo Pydantic para validar os dados enviados no `POST`.
- Retornar respostas JSON apropriadas para as operações.

### 🛠️ 2. Trabalhar com parâmetros e validação

#### Descrição
Adicione filtros de consulta e parâmetros opcionais à API.

#### Requisitos
O programa completo deve:

- Permitir consultar itens por campo, como `?q=nome`.
- Usar parâmetros de consulta opcionais e valores padrão.
- Garantir que os tipos de dados recebidos sejam validados automaticamente pelo FastAPI.

### 🛠️ 3. Documentação e teste local

#### Descrição
Teste a API localmente e verifique a documentação automática gerada pelo FastAPI.

#### Requisitos
O programa completo deve:

- Ser executável localmente com `uvicorn`.
- Incluir comentários ou instruções de teste que mostrem como acessar a documentação em `/docs`.
- Funcionar em um ambiente de desenvolvimento Python com FastAPI instalado.
