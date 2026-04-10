# Sistema de Folha de Pagamento

Projeto desenvolvido em Python para gerenciamento de folha de pagamento de uma pequena empresa.

---

## Funcionalidades

- Cadastro de funcionários:
  - Estagiário
  - CLT
  - Freelancer

- Cálculo automático de salários:
  - INSS (8% para CLT)
  - IRRF (10% para salários acima de R$ 2000)
  - Desconto de 5% para freelancers

- Geração de relatório detalhado

- Salvamento do relatório em arquivo `.txt` dentro da pasta `docs`

---

## Estrutura do Projeto

folha_pagamento/
│
├── src/
│   ├── calculos.py
│   ├── funcionario.py
│   ├── relatorio.py
│
├── tests/
│   ├── test_calculos.py
│
├── docs/
│   └── relatorio_folha.txt
│
├── main.py
├── requirements.txt
└── README.md

---

## Como executar

1. Ativar ambiente virtual

.venv\Scripts\activate

2. Rodar o sistema

python main.py

---

## Testes

Rodar os testes com:

pytest

---

## Exemplo de saída

=== Relatório de Folha de Pagamento ===

Nome: João
Tipo: clt
Salário Bruto: R$ 3000.00
Desconto INSS: R$ 240.00
Desconto IRRF: R$ 300.00
Salário Líquido: R$ 2460.00

---

## Tecnologias utilizadas

- Python 3
- Pytest

---

## Observações

- O sistema utiliza tratamento de erros para entradas inválidas
- Os dados são armazenados em memória durante a execução
- O relatório é salvo automaticamente na pasta `docs`

---

## Autor

Projeto desenvolvido para fins acadêmicos.