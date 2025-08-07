# Simulador de Extração Líquido-Líquido - Ácido Acético com Éter

Este projeto é um simulador simples em Python para processos de extração líquido-líquido, onde o ácido acético é extraído com o uso de éter como solvente. A aplicação permite realizar simulações baseadas em entradas fornecidas pelo usuário e salva os resultados em um arquivo `.txt`.

## 📌 Funcionalidades

- Entrada de dados de alimentação e composição de correntes.
- Cálculo da massa de ácido acético extraída no extrato.
- Determinação das correntes de extrato, rafinado e reciclo.
- Salvamento automático dos resultados em um arquivo `.txt`.
- Visualização dos dados da última simulação.

## 📁 Estrutura dos Dados

Os seguintes dados são calculados e armazenados:

| Coluna                                       | Descrição |
|----------------------------------------------|-------------------------------------------------------|
| Alimentação Inicial (kg/h)                   | Vazão mássica da alimentação principal.               |
| Alimentação de Eter (kg/h)                   | Vazão do solvente (éter) adicionado ao sistema.       |
| % Ácido Acético na Alimentação Inicial       | Concentração de ácido acético na alimentação.         |
| % Ácido Acético no Extrato (%)               | Concentração de ácido acético na corrente de extrato. |
| Massa de Ácido Acético na Alimentação (kg/h) | Quantidade total de ácido acético na alimentação.     |
| Ácido Acético Extraído no Extrato (kg/h)     | Quantidade extraída de ácido acético na fase extrato. |
| Total do Extrato (kg/h)                      | Massa total da corrente de extrato.                   |
| Raffinate (kg/h)                             | Massa restante após extração (não extraída).          |
| Saída de Reciclagem (kg/h)                   | Parte da corrente do rafinado reciclada (50%).        |

## ▶️ Como Executar

1. **Pré-requisitos**:
   - Python 3.x instalado.
   - Biblioteca `pandas` instalada (pode ser instalada com `pip install pandas`).

2. **Executando o Script**:

   No terminal ou prompt de comando:

   ```bash
   python simulador_extracao.py
   ```

3. **Menu do Programa**:
   - **Opção 1:** Realiza uma nova simulação com base nos dados inseridos.
   - **Opção 2:** Exibe os dados da simulação realizada (em tempo de execução).
   - **Opção 3:** Encerra o programa.

## 💾 Saída dos Dados

Os dados da simulação são salvos automaticamente no arquivo `Simulacao_Dados.txt` no formato de colunas separadas por tabulação (`.tsv`).

## ⚠️ Validações

- O programa impede a entrada de valores negativos.
- Apenas números são aceitos como entrada.
- Simulações precisam ser realizadas antes de visualizar os dados (opção 2).

## 🛠️ Exemplo de Uso

```text
-----------------------
1 - Realizar simulação.
2 - Ver dados da simulação.
3 - Sair do sistema.
-----------------------
Escolha uma opção do menu do sistema: 1

>>> Você escolheu realizar uma simulação.
Digite a alimentação inicial em kg/h: 100
Digite a alimentação de eter (solvente) em kg/h: 50
Percentagem de ácido acético na alimentação inicial (%): 20
Percentagem de ácido acético no extrato (%): 30
Percentagem de ácido acético extraído no extrato (%): 90

--- Simulação Realizada e Salva com Sucesso! ---
```

## 🧪 Aplicações

- Estudos acadêmicos sobre separação líquido-líquido.
- Avaliação de rendimento de processos de extração.
- Treinamento em balanço de massa com separadores e recicladores.

## 📄 Licença

Este projeto é de uso livre para fins educacionais e acadêmicos.
=======

