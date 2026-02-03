# 🏦 Leitor de Retorno Bancário (CNAB 400) - Bradesco

Este projeto é um script em **Python** desenvolvido para automatizar a leitura e análise de arquivos de retorno bancário no padrão **CNAB 400** (especificamente do Banco Bradesco).

O objetivo é permitir uma conferência rápida e programática dos boletos liquidados, baixados ou com ocorrências, servindo como uma ferramenta auxiliar de validação financeira.

## 🚀 Funcionalidades

- **Parsing Posicional:** Leitura de arquivos de texto com largura fixa (layout CNAB 400).
- **Tratamento de Dados:**
  - Conversão automática de datas (formato `DDMMAA` para `YYYY-MM-DD`).
  - Conversão de valores financeiros (tratamento de casas decimais).
  - Tradução de códigos de ocorrência (ex: `06` -> `Liquidação Normal`).
- **Análise de Dados:** Utiliza a biblioteca **Pandas** para estruturar os dados em um DataFrame, facilitando filtros e exportações futuras.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** (Manipulação de dados)
- **Datetime** (Tratamento temporal)

## 📦 Como usar

### 1. Pré-requisitos
Certifique-se de ter o Python instalado e instale a biblioteca `pandas` via terminal:

```bash
pip install pandas
```

### 2. Configuração
Coloque o seu arquivo de retorno (ex: CB310100.RET) na mesma pasta do script ou ajuste a variável arquivo_exemplo dentro do código processar_retorno.py:
arquivo_exemplo = "CB310100.RET"

### 3. Execução
Execute o script via terminal na pasta do projeto:

```bash
python processar_retorno.py
```
### 4. Resultado Esperado
O script exibirá no console um resumo tabular dos pagamentos identificados:

```
--- Resumo dos Pagamentos ---
Nosso Número     Ocorrência              Data Crédito  Valor Pago (R$)
0  00000002650      Liquidação Normal       2026-02-03    100.00
1  00000002672      Liquidação Normal       2026-02-03    125.45
...

```

## Nota de Segurança
Este repositório contém apenas a lógica de processamento. Nenhum arquivo .RET real contendo dados financeiros sensíveis deve ser comitado neste repositório. Recomenda-se o uso de um arquivo .gitignore para excluir extensões como *.RET e *.ret.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.

## Licença
Este projeto é de livre uso para fins de estudo e automação financeira.
Sinta-se à vontade para modificar e adaptar conforme suas necessidades!






