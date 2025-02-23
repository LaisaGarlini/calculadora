# Calculadora em Python

> Este repositório contém uma aplicação de calculadora desenvolvida em Python. A calculadora realiza operações básicas, como adição, subtração, multiplicação e divisão.

## Estrutura do Projeto

- `calculadora.py`: Contém a implementação das funções da calculadora.
- `teste.py`: Contém os testes para as funções da calculadora.

## Funcionalidades

A calculadora suporta as seguintes operações:

- Adição (`+`)
- Subtração (`-`)
- Multiplicação (`*`)
- Divisão (`/`)

## Como Executar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/LaisaGarlini/calculadora.git

2. **Navegue até o diretório do projeto:**

   ```bash
   cd calculadora

3. **Instale as dependências do projeto:**

   ```bash
   pip install -r requirements.txt

4. **Execute o script da calculadora:**

   ```bash
   python .\calculadora.py

## Testes

   ```bash
   python .\teste.py
   ```

## Pipeline de CI/CD
O pipeline de CI/CD está configurado usando GitHub Actions e é composto por quatro estágios:

1. **Build:**
  Configura o ambiente Python.
  Instala as dependências (pytest, flake8, pytest-cov).

2. **Lint:**
  Executa o flake8 para verificar a qualidade do código.

3. **Test:**
  Executa os testes com pytest e verifica a cobertura de testes.

4. **Deploy:**
  Simula um deploy (apenas uma mensagem de sucesso no momento).

Como Funciona
- O pipeline é acionado automaticamente a cada push ou pull request.

- Você pode ver o status do pipeline na aba Actions do GitHub.
