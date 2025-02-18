# Desafio Bancário: Sistema de Gerenciamento de Conta

Este projeto simula as operações básicas de um sistema bancário e foi atualizado para incluir a criação de **usuários** e **contas correntes**. Agora, além das transações de **depósito**, **saque** e **visualização de extrato**, o sistema permite gerenciar clientes e suas contas de forma mais organizada.

## Funcionalidades

O sistema oferece as seguintes operações:

### 1. **Criação de Usuário**
- Permite a criação de novos usuários, incluindo dados como **nome**, **data de nascimento**, **CPF** e **endereço**.
- O CPF dos usuários é validado para garantir que não existam duplicidades no cadastro.

### 2. **Criação de Conta Corrente**
- Após a criação de um usuário, é possível criar uma ou mais **contas correntes** vinculadas a esse usuário.
- Cada conta possui um **número sequencial** e uma **agência fixa** ("0001").

### 3. **Depósito**
- O sistema permite que o usuário **deposite** valores na sua conta, o que aumenta o saldo da conta.

### 4. **Saque**
- O usuário pode realizar saques com as seguintes validações:
  - **Saldo suficiente**: O valor do saque não pode exceder o saldo disponível.
  - **Limite de saque**: O valor do saque não pode exceder o limite definido para saques.
  - **Limitação de saques**: O sistema permite no máximo **3 saques por sessão**.

### 5. **Extrato**
- O sistema exibe um **extrato** detalhado com o histórico de todas as transações realizadas, incluindo depósitos e saques, além do **saldo atual** da conta.

## Requisitos

- O sistema deve garantir que os valores de saque não ultrapassem o saldo ou o limite de saque.
- O extrato deve ser exibido corretamente, mesmo que não haja transações.
- O número máximo de saques por sessão é limitado a **3**.
- O sistema deve permitir a criação de **usuários** e **contas correntes** para cada cliente.

## Tecnologias Utilizadas

- **Linguagem**: Python

