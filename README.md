# **Desafio Bancário: Sistema de Gerenciamento de Conta**

Este projeto simula as operações básicas de um **sistema bancário**, permitindo que o usuário realize as seguintes transações:

- **Depósito**: O usuário pode depositar um valor na sua conta, que é adicionado ao saldo.
- **Saque**: O usuário pode sacar valores, respeitando limites de saque e o saldo disponível.
- **Extrato**: O sistema gera um extrato detalhado com o histórico das transações realizadas (**depósitos** e **saques**), além de exibir o saldo atual.

---

## **Funcionalidades:**

- **Depósito** de valores para a conta.
- **Saque** com validações para:
  - **Saldo suficiente**.
  - **Limite de valor**.
  - **Número máximo de saques** (limite de 3 por sessão).
- **Exibição de Extrato** com todas as transações e o saldo atual.
- **Limitação de saques** (máximo de 3 saques por sessão).

---

## **Requisitos:**

- O sistema deve garantir que os valores de **saque** não ultrapassem o saldo ou o limite estabelecido.
- O **extrato** deve ser exibido corretamente, mesmo que não haja transações.

---

## **Tecnologias Utilizadas:**

- **Linguagem**: Python

---

