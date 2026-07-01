# TP2 — Relatório Gerencial com Google Looker Studio

## Descrição
Construção de um relatório gerencial de vendas com limpeza de dados,
campos calculados, KPIs e filtros interativos no Google Looker Studio.

## Ferramentas Utilizadas
- Google Looker Studio
- Google Sheets

## O que foi feito

### Preparação dos Dados
- Importação do CSV da loja de materiais no Google Sheets
- Conversão para formato de tabela estruturada
- Limpeza e padronização das colunas e tipos de dados

### Relatório — "Relatório Gerencial de Vendas de 2025"
- Fonte de dados reutilizável conectada ao Google Sheets
- Campo calculado **Resultado Líquido do Produto**:
  `(Valor do produto - (Valor do produto × 0,8)) × Quantidade comprada`
- Três KPIs de Visão Geral:
  - Resultado Total Bruto
  - Resultado Total Líquido
  - Quantidade Total de Itens Comprados
- Gráfico de barras: faturamento por cliente
- Gráfico de pizza: quantidade de produtos vendidos
- Tabela detalhada de clientes ordenada por valor comprado
- Filtro interativo por tipo de cliente com subtotal
- Validação cruzada entre Sheets e Looker Studio (3 amostras)

## Aprendizados
- Limpeza e estruturação de dados reais no Google Sheets
- Criação de campos calculados no Looker Studio
- Construção de relatório gerencial com KPIs, gráficos e filtros
- Validação de consistência entre fonte de dados e relatório